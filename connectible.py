import argparse
import sys

def windows(width, line):
    iters = []
    for i in range(width):
        iters.append(line[i:])
    return zip(*iters)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=2)
    parser.add_argument('files', type=str, nargs='+')
    slices = set()
    connects = int()
    args = parser.parse_args()
    for file in args.files:
        lines = open(file).readlines()
        print(f"{file} has {len(lines)} lines")
        for i in lines:
            line = i.strip().split()
            for t in windows(args.width, line):
                if t in slices:
                    connects += 1
                slices.add(t)
    print(f"Files have {connects} connections")

try:
    main()
except BaseException as e:
    sys.exit(e)
