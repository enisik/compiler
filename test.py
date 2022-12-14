import os
import subprocess


def main():
    print("Begin Testing\n")
    for filename in os.listdir("test"):
        print(filename)
        os.system(
            f"python3 main.py -compile test/{filename}")
    print("\nTesting Finished")


if __name__ == '__main__':
    main()
