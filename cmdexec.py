"""
    Bash for Python v1.0.0
    This project under MIT License.
    more info:README.md

    This is the Comand Excute file of the project.
"""

# import third-party modules

import subprocess

# import local modules

import defV
import builtC

def cmdExec(cmd: str) -> None:
    """
    Execute command

    Parameters
    ----------
    cmd : str
        Command to execute
    """
    if cmd == "exit":
        exit(0)
    elif cmd == "bash":
        subprocess.run(["python", "main.py"], shell=True, check=True)
    elif cmd == "bash --version":
        print(defV.VERSION_MSG)
    elif cmd == "bash -c help":
        print(defV.CMD_HELP_MSG)
    elif cmd.startswith("echo"):
        builtC.echo(cmd)
    elif cmd.startswith("cd"):
        builtC.cd(cmd)
    elif cmd.startswith("pwd"):
        builtC.pwd(cmd)
    else:
        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{cmd}\nCommand '{cmd}' not found.")
