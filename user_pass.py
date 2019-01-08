from getpass import getpass


def get_user_pass(username, password):
    if not username:
        print("Enter username address:", )
        username = input()
    if not password:
        print("Enter password:")
        password = getpass('Password:')
    return username, password
