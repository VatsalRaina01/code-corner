import sys

line = sys.stdin.readline().strip()
if "," in line:
    first, second = line.split(",", 1)

    # Remove whitespace, convert to lowercase, and sort the characters
    first_sorted = sorted(first.lower().replace(" ", ""))
    second_sorted = sorted(second.lower().replace(" ", ""))

    if first_sorted == second_sorted:
        print("true")
    else:
        print("false")
