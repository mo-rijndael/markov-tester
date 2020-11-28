import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', type=str, nargs='+')
    pairs = set()
    connects = int()
    args = parser.parse_args()
    for file in args.files:
        lines = open(file).readlines()
        print(f"{file} has {len(lines)} lines")
        for i in lines:
            line = i.strip().split()
            for t in zip(line, line[1:]):
                if t in pairs:
                    connects += 1
                pairs.add(t)
    print(f"Files have {connects} connections")

try:
    main()
except BaseException as e:
    sys.exit(e)
