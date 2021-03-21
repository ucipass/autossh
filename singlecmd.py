from __future__ import print_function
import paramiko
import csv
import argparse
from getpass import getpass


def get_user_pass():
  #Works in Python 2 and 3:
  try: input = raw_input
  except NameError: pass 
  username = input("Username: ")
  password = getpass('Password: ')
  return username, password


def connect(hostname,ip,port,username,password,command,file):
  try:
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect(ip, port=port, username=username, password=password, timeout=10, allow_agent=False, look_for_keys=False)
    stdin, stdout, stderr = p.exec_command(command)
    result = stdout.readlines()
    result = "".join(result)
  except:
    result = "CONNECTION ERROR\n"
  return result


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file', help='Specify the CSV file for SSH connectivity. Default is hosts.csv in current directory', nargs='?', default="hosts.csv")
  parser.add_argument('-a', '--auth', help='Ask for usuername/password and use that for SSH authentication instead of provided credentials in the CSV file', action='store_true')
  parser.add_argument('-q', '--quiet', help='Do not display results', action='store_true')
  parser.add_argument('-s', '--save', help='Save results to output file as hostname.txt', action='store_true')
  args = parser.parse_args()
  filename = args.file
  localuser = None
  localpass = None

  if args.auth :
    localuser,localpass = get_user_pass()

  with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      ip = row['ip']
      hostname = row['hostname']
      port     = int(row['port']) if "port" in row  else 22
      username = localuser if localuser else row['username']
      password = localpass if localpass else row['password']
      command  = row['command']
      file     = row['file'] if 'file' in row else row['hostname']+".txt"

      result = connect( hostname,ip,port,username,password,command,file )
      print(hostname +"("+ip+"):" + command )
      if not args.quiet:
        print(result)
      if args.save:
        with open( file if file else hostname+".txt" , 'w') as f:
          f.write(result)



