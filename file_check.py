import os
import sys


dir_root = os.path.dirname(os.path.realpath(__file__))
host_file_path = os.path.join(dir_root, "host.txt")
cmd_file_path = os.path.join(dir_root, "cmd.txt")


def read_file_lines(filename):
    lines = []
    try:
        with open(filename, 'r') as stream:
            next_line = True
            while next_line:
                line = stream.readline()
                if line == "":
                    next_line = False
                else:
                    lines.append(line.strip())
    except FileNotFoundError:
        print("Reading file", filename,  "failed!")
        sys.exit(1)
    except Exception as e:
        print("Unexpected error:", e)
        sys.exit(1)
    return lines


def read_host_file():
    return read_file_lines("host.txt")


def read_cmd_file():
    return read_file_lines("cmd.txt")


