import sys

def main():
    if len(sys.argv) != 3:
        raise Exception("only 2 args supported")
    first = open(sys.argv[1]).readlines()
    second = open(sys.argv[2]).readlines()
    pairs = set()
    connects = int()
    for i in first:
        line = i.split()
        for t in zip(line, line[1:]):
            pairs.add(t)

    for i in second:
        line = i.split()
        for t in zip(line, line[1:]):
            if t in pairs:
                connects += 1
    print(f"First  file contains {len(first)} lines")
    print(f"Secons file contains {len(second)} lines")
    print(f"Files has {connects} connections")

try:
    main()
except BaseException as e:
    sys.exit(e)
