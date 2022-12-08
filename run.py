#!/usr/bin/env python3
"""Run Advent of Code solutions.

Heavily inspired by:
https://github.com/oliver-ni/advent-of-code/blob/master/run.py
"""
import argparse
import os.path
import pyperclip
import requests
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload


def run(func, filename="filename", copy_to_clipboard=False):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                solution = func(f)
                end = time.monotonic_ns()
                print(solution, end="\t")
                print(f"[{(end-start) / 10**6:.3f} ms]")
                if copy_to_clipboard and solution is not None:
                    pyperclip.copy(solution)
            except:
                traceback.print_exc()
    except FileNotFoundError:
        print()


def fetch_input(day, year=2022):
    """Fetches input files for Advent of Code challenges.

    Since inputs differ by user, provide the session cookie in a file
    called 'session'.
    """
    assert day > 0 and day <= 25
    assert year >= 2016
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    with open('session', 'r') as f:
        cookies = dict(session=f.read().strip())
    r = requests.get(url, cookies=cookies)
    return r.text


if __name__ == "__main__":
    now = datetime.now(timezone(timedelta(hours=-5)))
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--extra", "-e", help="Choose a different solution to run.")
    args = parser.parse_args()

    input_paths = {
        "sample": f"input/{args.year}/day{args.day:02}_sample.txt",
        "input": f"input/{args.year}/day{args.day:02}.txt",
    }

    if not os.path.exists(input_paths["input"]):
        with open(input_paths["input"], "w") as f:
            f.write(fetch_input(day=args.day, year=args.year))

    module_name = f"{args.year}.day{args.day:02}"
    if args.extra:
        module_name += f"_{args.extra}"

    print(f"{module_name}")

    module = import_module(module_name)

    for func in ("p1", "p2"):
        if not hasattr(module, func):
            continue
        print(f"--- {func} ---")
        print("sample:", end="\t")
        run(getattr(module, func), input_paths["sample"])
        reload(module)
        print("input:", end="\t")
        run(getattr(module, func), input_paths["input"], copy_to_clipboard=True)
