"""
    Bash for Python v1.0.0
    This project under MIT License.
    more info:README.md

    This is the Main file of the project.
"""

# third-party modules import
import os
import sys
import yaml  # config file

# local modules import
import interactiveM

# variables
args = None
config = None

# main
def main():
    """
    Main function of the project.
    """

    # global variables
    global args
    global config

    # .bashprc.yaml file check
    try:
        with open("./config/.bashprc.yaml", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("Error: .bashprc.yaml file not found.")
        sys.exit(1)
    except PermissionError:
        print("Error: .bashprc.yaml file permission denied.")
        sys.exit(1)
    except yaml.YAMLError as e:
        if hasattr(e, "problem_mark"):
            mark = e.problem_mark
            print(f"Error: .bashprc.yaml syntax error in line {mark.line + 1}, column {mark.column + 1}.")
        else:
            print("Error: .bashprc.yaml syntax error.")
        sys.exit(1)

    # set current directory
    default_directory = config["carent_directory"].replace("${HOMEDIR}", os.path.expanduser("~"))
    os.chdir(default_directory)

    # arguments check
    args = sys.argv
    if len(args) == 1:
        interactiveM.interactiveMode(config)
    else:
        print("command options coming soon.")
        sys.exit(1)

try:
    main()
except KeyboardInterrupt:
    exit(0)
