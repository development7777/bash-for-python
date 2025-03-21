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
    print(cmd[5:])

def cd(cmd: str) -> None:
    """
    Change directory command"
    """
    try:
        os.chdir(cmd[3:])
    except FileNotFoundError:
        print(f"{cmd}\nbash: cd: {cmd[3:]}: No such file or directory.")
    except NotADirectoryError:
        print(f"{cmd}\nNo such file or directory.")
