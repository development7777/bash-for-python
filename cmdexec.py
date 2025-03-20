# import module

import subprocess

def cmdExec(cmd: str) -> None:
    """
    Execute command

    Parameters
    ----------
    cmd : str
        Command to execute
    """
    subprocess.run(cmd, shell=True, check=True)
