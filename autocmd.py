from netmiko import Netmiko
import re
import time
import os


def run_cmds(host, username, password, cmds):
    homedir = os.path.dirname(os.path.realpath(__file__))
    print(host, username, password)
    net_connect = Netmiko(host=host, username=username, password=password, device_type="cisco_ios", timeout=30)
    hostname = net_connect.find_prompt()
    hostname = re.sub('#', '', hostname)
    net_connect.send_command("term len 0")
    for cmd in cmds:
        print("\t", cmd)
        try:
            cmd_output = net_connect.send_command(cmd, hostname)
            net_connect.read_until_prompt_or_pattern()
            timestr = time.strftime("%Y%m%d-%H%M%S")
            filename = os.path.join(homedir, hostname + "_OUTPUT_" + timestr + ".txt")
            cmd_output = cmd_output.strip()
            if cmd_output != "":
                print(cmd_output.strip())
            """
            if 'hostname' in cmd_output:
                text_file = open(filename, "w")
                text_file.write(cmd_output)
                text_file.close()
                print("  output file saved as:", filename)
            else:
                print("  output file was NOT saved for:", host)
            """
        except Exception as e:
            print("ERROR EXECUTING", cmd, "on host: ",host)
            print(e)
