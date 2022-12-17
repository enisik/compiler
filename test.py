import os
import sys


def main(arg):
    print("Begin Testing\n")
    for filename in os.listdir(arg):
        print(filename)
        os.system(
            f"python3 main.py -compile {arg}/{filename}")
        print("")
    print("\nTesting Finished")


if __name__ == '__main__':
    main(sys.argv[1])
