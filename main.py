import argparse
from file_check import read_host_file, read_cmd_file
from user_pass import get_user_pass
from autocmd import run_cmds


def verify_cmd_txt():
    return True


def verify_host_txt():
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verify", help="verify hosts are accessible", action="store_true")
    parser.add_argument('-u', '--username', help='Login username', nargs='?', default="")
    parser.add_argument('-p', '--password', help='Login password', nargs='?', default="")
    args = parser.parse_args()
    hosts = read_host_file()
    cmds = read_cmd_file()
    username, password = get_user_pass(args.username, args.password)
    for host in hosts:
            run_cmds(host, username, password, cmds)


if __name__ == '__main__':
    main()
