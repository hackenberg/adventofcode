import re


def p1(f):
    passports = [s.replace("\n", " ") for s in f.read().split("\n\n")]
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def is_valid(pp):
        return {s[:3] for s in pp.split()}.issuperset(required_fields)

    return sum(map(is_valid, passports))


def p2(f):
    passports = [s.replace("\n", " ") for s in f.read().split("\n\n")]
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def is_valid(pp):
        fields = pp.split()

        if not {f[:3] for f in fields}.issuperset(required_fields):
            return False

        for field in pp.split():
            match field.split(":"):
                case ["byr", value]:
                    if not irange(value, 1920, 2002):
                        return False

                case ["iyr", value]:
                    if not irange(value, 2010, 2020):
                        return False

                case ["eyr", value]:
                    if not irange(value, 2020, 2030):
                        return False

                case ["hgt", value]:
                    if value.endswith("cm"):
                        if not irange(value.replace("cm", ""), 150, 193):
                            return False
                    elif value.endswith("in"):
                        if not irange(value.replace("in", ""), 59, 76):
                            return False
                    else:
                        return False

                case ["hcl", value]:
                    if not re.search(r"^#[0-9a-f]{6}$", value):
                        return False

                case ["ecl", value]:
                    if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        return False

                case ["pid", value]:
                    if not re.search(r"^[0-9]{9}$", value):
                        return False

        else:
            return True

    return sum(map(is_valid, passports))


def irange(n, lb, ub):
    return int(n) in range(lb, ub + 1)
