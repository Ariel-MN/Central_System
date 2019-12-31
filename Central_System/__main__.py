# -*- coding: utf-8 -*-
"""
todo: Documentation

    Project name: Central System
    File name: __main__

    Date created: 20/03/2019
    Date last modified: 31/12/2019
    Status: Stable

    Python version: 3.8
    Modules required: time, argparse, os
"""
__author__ = 'Ariel Montes Nogueira'
__website__ = 'http://www.montes.ml'
__email__ = 'arielmontes1989@gmail.com'

__copyright__ = 'Copyright © 2019-present Ariel Montes Nogueira'
__credits__ = []
__license__ = '''
                Licensed under the Apache License, Version 2.0 (the "License");
                you may not use this file except in compliance with the License.
                You may obtain a copy of the License at

                    http://www.apache.org/licenses/LICENSE-2.0

                Unless required by applicable law or agreed to in writing, software
                distributed under the License is distributed on an "AS IS" BASIS,
                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
                See the License for the specific language governing permissions and
                limitations under the License.'''
__recovery__ = 'https://github.com/Ariel-MN/Central_System'
__version__ = '1.0'


import time
import argparse
from os import system, name

# scripts:
import scripts.skeleton as skel
import scripts.secure as safe


parser = argparse.ArgumentParser(description="This program allows you to control embedded systems and sensors")
parser.add_argument("-st", "--standard", action="store_true", default=False, help="standard settings")
parser.add_argument("-sf", "--safemode", action="store_true", default=False, help="safe mode - without pre-config")
parser.add_argument("-lg", "--logging", action="store_true", default=False, help="logging, all logs become active")
args = parser.parse_args()

""" Program register, record which file program is active """
program_rec = {"skeleton": False, "secure": False}


def clear():
    """
    Function Clear, clean the screen.
    """
    # Compatibility for Windows
    if name == 'nt':
        _ = system('cls')

    # Compatibility for Mac e Linux(os.name: "posix")
    else:
        _ = system('clear')


def power(shutdown=False):
    """
    Check to close the program correctly.
    :param shutdown: Signal sent by program_file.
    :return: Switch-off status.
    """
    return shutdown


if __name__ == "__main__":
    try:
        """Management of the program-start Mode"""

        if args.standard is True:
            print("< Loading Standard Mode > ...")
            time.sleep(2)
            clear()
            skel.mode_standard()

        elif args.safemode is True:
            print("< Loading Safe Mode > ...")
            time.sleep(2)
            clear()
            safe.program_start()

        elif args.logging is True:
            print("< Loading Logging Mode > ...")
            time.sleep(2)
            clear()
            skel.mode_logging()

        else:
            print("< Loading Program > ...")
            time.sleep(2)
            clear()
            skel.mode_common()

        clear()

        if program_rec["skeleton"] is True:
            """
            Check that the program in 'skeleton' file has been started.
            Then check the shutdown status of the 'skeleton' program.
            """
            if power(shutdown=True):
                print("< System shutdown properly >")
                time.sleep(1.5)
                clear()

            else:
                print("< Error: Forced shutdown >")
                time.sleep(1)
                clear()

        elif program_rec["secure"] is True:
            """
            Check that the program in 'secure' file has been started.
            Then check the shutdown status of the 'secure' program.
            """
            if power(shutdown=True):
                print("< System shutdown properly >")
                time.sleep(1)
                clear()

            else:
                print("< Error: Forced shutdown >")
                time.sleep(1)
                clear()

            """ Error handling: """
    except NameError as Error:
        clear()
        print("< Error: Program File not found >")
        input("< Press enter to exit the program >\n\n>>")
        exit(1)

    except:
        print("< Error: Generic on program start >")
        input("< Press enter to exit the program >\n\n>>")
        exit(1)
