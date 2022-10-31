import os
import sys
from pathlib import Path

def main(argv=None):
    # print(sys.argv[:])
    # print(os.path.basename(argv[0]))

    print(Path(__file__).resolve().parent.parent)


if __name__ == '__main__':
    main(sys.argv)
