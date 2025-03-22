"""
    Bash for Python v1.0.0
    This project under MIT License.
    more info:README.md

    This is the Inactive Mode file of the project.
"""

# import modules
import sys
import subprocess
import cmdexec

def interactiveMode(config: dict) -> None:
    """
    Interactive mode function.

    parameters
    ----------
    config : dict
        Configuration parameters
    """

    # interactive mode
    cmd = input(config["prompt"])
    cmdexec.cmdExec(cmd)
    file = open(__file__, encoding='UTF-8')
    exec(file.read())
    exec("interactiveMode(" + str(config) + ")")
    file.close()

    sys.exit(0)
