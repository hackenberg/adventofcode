#!/usr/bin/env python3
"""Run Advent of Code solutions.

Heavily inspired by:
https://github.com/oliver-ni/advent-of-code/blob/master/run.py
"""
import argparse
import cProfile, pstats, io
import os
import pyperclip
import requests
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload
from pathlib import Path
from typing import Callable


def run(func: Callable[[str], any], filepath: Path = Path("filename"), copy_to_clipboard: bool = False) -> None:
    try:
        start = time.monotonic_ns()
        solution = func(filepath.read_text())
        end = time.monotonic_ns()
        print(solution, end="\t")
        print(f"[{(end-start) / 10**6:.3f} ms]")
        if copy_to_clipboard and solution is not None:
            pyperclip.copy(solution)
    except FileNotFoundError:
        print()
    except:
        traceback.print_exc()


def fetch_input(day: int, year: int = 2022) -> str:
    """Fetches input files for Advent of Code challenges.

    Since inputs differ by user, provide the session cookie in a file
    called 'session'.
    """
    assert 0 < day <= 25
    assert year >= 2016
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    with open("session", "r") as f:
        cookies = dict(session=f.read().strip())
    r = requests.get(url, cookies=cookies)
    return r.text


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    parser.add_argument("--profile", "-p", action="store_true", help="Collect performance metrics.")
    parser.add_argument("--sample", "-s", action="store_true", help="Run on sample input only.")
    args = parser.parse_args()

    input_paths = {
        "sample": Path(f"input/{args.year}/day{args.day:02}_sample.txt"),
        "input": Path(f"input/{args.year}/day{args.day:02}.txt"),
    }

    input_paths["input"].parent.mkdir(parents=True, exist_ok=True)
    if not args.sample and not os.path.exists(input_paths["input"]):
        input_paths["input"].write_text(fetch_input(day=args.day, year=args.year))

    # TODO error in case sample input does not exist

    module_name = f"{args.year}.day{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    if args.profile:
        pr = cProfile.Profile()

    for func in ("p1", "p2"):
        if not hasattr(module, func):
            continue
        print(f"--- {func} ---")
        print("sample:", end="\t")
        args.profile and pr.enable()
        run(getattr(module, func), input_paths["sample"])
        args.profile and pr.disable()
        if args.sample:
            continue
        reload(module)
        print("input:", end="\t")
        args.profile and pr.enable()
        run(getattr(module, func), input_paths["input"], copy_to_clipboard=True)
        args.profile and pr.disable()

    if args.profile:
        s = io.StringIO()
        sortby = pstats.SortKey.CUMULATIVE
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
