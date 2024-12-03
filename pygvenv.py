#!/usr/bin/env python3

import sys
import subprocess
import os

from typing import List

def run_commands(commands: List[List[str]]):
    for command in commands:
        print("Running command", command)
        res = subprocess.run(command, capture_output=True, text=True)

        if res.returncode:
            print(f"An error occured {res.stderr}")
            return

DEFAULT_PATH = os.path.expanduser("~/.pygvenv")
DEFAULT_VENV_DIR = ".venv"
DEFAULT_FULL_VENV_PATH = f"{DEFAULT_PATH}/{DEFAULT_VENV_DIR}"

def main():
    args = sys.argv

    if len(args) < 2:
        print("No arguments supplied!")
        return

    match args[1]:

        case "help":
            print(
                "pygvenv (Python Global Virtual Environments) is usefull when you want to use global-wide pip packages without interfering with system dependencies and packages."\
                "\nIt will also help avoid this annoying warning: error: externally-managed-environment"\
                "\n\nAvailable commands:\n"\
                "create - Create virtual environment, by defualt in directory: (~/.pygvenv)\n"\
                "pip - Wrap pip commands within virtual environment\n"\
                "run - run specied command within virtual environment\n"
                "activate - activates venv"
            )

        case "create":
            run_commands( [
                ["mkdir", "-p", DEFAULT_PATH],
                ["python3", "-m", "venv", DEFAULT_FULL_VENV_PATH]
            ])

        case "pip":
            command  = f"bash -c 'source {DEFAULT_FULL_VENV_PATH}/bin/activate && "
            command += "pip " + " ".join(args[2:]) + "'"

            print("Running command", command)
            os.system(command)

            command = "exit"
            print("Running command", command)
            os.system(command)


        case "run":
            commands = [
                ["bash", "-c", "source", "activate", f"{DEFAULT_FULL_VENV_PATH}/bin/activate"],
                [arg for arg in args[2:]],
                ["deactivate"]
            ]

            run_commands(commands)

        case "activate":
            command = f"bash -c 'source {DEFAULT_FULL_VENV_PATH}/bin/activate && export PS1=\"(.pygvenv) $PS1\" && exec bash'"
            print("Running command:", command)

            # Run the command in a new shell
            subprocess.call(command, shell=True)

        case _:
            print(f"unrecognized argument {args[1]}")

if __name__ == "__main__":
    main()
    