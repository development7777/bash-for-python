"""
    Bash for Python v1.0.0
    This project under MIT License.
    more info:README.md

    This is the Built-in Command file of the project.
"""

# import modules
import os

def echo(cmd: str) -> None:
    """
    Echo command

    Parameters
    ----------
    cmd : str
        Command to execute
    """
    if cmd == "echo":
        print("echo\n")
    else:
        print(cmd[5:])

def cd(cmd: str) -> None:
    """
    Change directory command.

    Parameters
    ----------
    cmd : str
        Command to execute
    """
    print(cmd)
    if cmd == "cd":
        os.chdir(os.path.expanduser("~"))
    else:
        try:
            os.chdir(cmd[3:])
        except FileNotFoundError:
            print(f"bash: cd: {cmd[3:]}: No such file or directory.")
        except NotADirectoryError:
            print(f"bash: cd: {cmd[3:]}: No such file or directory.")

def pwd(cmd: str) -> None:
    """
    Print working directory command.
    Parameters
    ----------
    cmd : str
        Command to execute
    """
    print(cmd)
    print(os.getcwd())
