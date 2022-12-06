#!/usr/bin/env python3
"""Run Advent of Code solutions.

Heavily inspired by:
https://github.com/oliver-ni/advent-of-code/blob/master/run.py
"""
import argparse
import os.path
import requests
import time
import traceback
from datetime import datetime, timedelta, timezone
from importlib import import_module, reload


def run(func, filename="filename"):
    try:
        with open(filename) as f:
            try:
                start = time.monotonic_ns()
                print(func(f), end="\t")
                end = time.monotonic_ns()
                print(f"[{(end-start) / 10**6:.3f} ms]")
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
    url = f'https://adventofcode.com/2022/day/{day}/input'
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
        "sample": f"day{args.day:02}/input_sample.txt",
        "input": f"day{args.day:02}/input.txt",
    }

    if not os.path.exists(input_paths["input"]):
        with open(input_paths["input"], "w") as f:
            f.write(fetch_input(day=args.day, year=args.year))

    module_name = f"day{args.day:02}.day{args.day:02}"
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
        run(getattr(module, func), input_paths["input"])
