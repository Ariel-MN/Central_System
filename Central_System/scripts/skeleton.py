# -*- coding: utf-8 -*-
"""
todo: Documentation

    -*- Version: Common, Standard, Logging -*-
    -*- Function: Structure of the program -*-

    Project name: Central System
    File name: skeleton

    Date created: 20/03/2019
    Date last modified: 31/12/2019
    Status: Stable

    Python version: 3.8
    Modules required: pymongo, getpass, logging, pprint, copy, json, time, os
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


import os
import json
import time
import copy
import pprint
import logging
import datetime
from getpass import getpass
from os import system, name
from pymongo import MongoClient

# scripts:
import __main__ as main
import scripts.build as build
from scripts.build import lang_build


""" Language Tools """
Chosen_Language = dict(English=True, Spanish=False, Italian=False)
global Lang
Lang = {
    "< Error: Missing program file 'language' >": "< Error: Missing program file 'language' >",

    "< Error: Missing program file '_spanish.json' or _italian.json' >":
        "< Error: Missing program file '_spanish.json' or _italian.json' >",

    "Management of Sensors": "Management of Sensors",
    "Management of Systems": "Management of Systems",
    "Configuration": "Configuration",
    "Language": "Language",
    "Exit": "Exit",

    "English": "English",
    "Italian": "Italian",
    "Spanish": "Spanish",

    "New     System": "New     System",
    "Delete  System": "Delete  System",
    "Assign  Sensor": "Assign  Sensor",
    "Removal Sensor": "Removal Sensor",
    "Monitoring": "Monitoring",
    "Back": "Back",

    "New    Sensor": "New    Sensor",
    "Delete Sensor": "Delete Sensor",
    "Change Sensor": "Change Sensor",

    "< Choose a System >": "< Choose a System >",
    "< Choose a Sensor >": "< Choose a Sensor >",
    "< Type 0 for go back >": "< Type 0 for go back >",

    "< Enter the name of the system >": "< Enter the name of the system >",
    "< Enter the local of the system >": "< Enter the local of the system >",
    "< Only letters and numbers without spaces or symbols >":
        "< Only letters and numbers without spaces or symbols >",

    "< Error: A system with that name already exists >":
        "< Error: A system with that name already exists >",
    "< Error: You have not entered a valid name for the local >":
        "< Error: You have not entered a valid name for the local >",
    "< Error: You have not entered a valid name for the system >":
        "< Error: You have not entered a valid name for the system >",
    "< System successfully added >": "< System successfully added >",

    "Delete sensor from the embedded system": "Delete sensor from the embedded system",
    "Delete sensor completely": "Delete sensor completely",

    "< Choose a number from the menu >": "< Choose a number from the menu >",

    "Create a sensor of:": "Create a sensor of:",
    "Light": "Light",
    "CO2": "CO2",
    "Humidity": "Humidity",
    "Infrared": "Infrared",
    "NFC": "NFC",

    "< Enter the number of one of the options >": "< Enter the number of one of the options >",
    "< Sensor successfully added >": "< Sensor Sensor successfully added >",

    "< Invalid option >": "< Invalid option >",

    "< Creation performed correctly >": "< Creation performed correctly >",

    "< Insert current value >": "< Insert current value >",
    "< Insert sampling frequency >": "< Insert sampling frequency >",
    "< Insert message frequency >": "< Insert message frequency >",

    "Load default config": "Load default config",
    "Load saved config": "Load saved config",

    "< Configuration loaded successfully >": "< Configuration loaded successfully >",
    "< Configuration saved successfully >": "< Configuration saved successfully >",
    "< Insert the name of the file without extension >": "< Insert the name of the file without extension >",

    "< There is no data to save >": "< No There is no data to save >",
    "< Save the config >": "< Save the config >",
    "< Error saving the file >": "< Error saving the file >",

    "User Name: ": "User Name: ",
    "Password: ": "Password: ",

    "< Choose the name of the DataBase >": "< Choose the name of the DataBase >",
    "< If you write a new name a new DataBase will be created >":
        "< If you write a new name a new DataBase will be created >",

    "< Error: control your internet connection >": "< Error: control your internet connection >",
    "< The information was successfully uploaded to the server >":
        "< The information was successfully uploaded to the server >",
    "< The ID of the file is: ": "< The ID of the file is: ",
    "< Error: can't access to the data base server >": "< Error: can't access to the data base server >",
    "< Control your credentials >": "< Control your credentials >",

    "Show all the config files in DB": "Show all the config files in DB",
    "Download config file from DB": "Download config file from DB",
    "< Files in the database >": "< Files in the database >",
    "File name: ": "File name: ",
    "< List of all the files in the server >": "< List of all the files in the server >",
    "< Insert the name of a file >": "< Insert the name of a file >",
    "New file created: ": "New file created: ",

    "< Your Internet is off, use the safe mode >": "< Your Internet is off, use the safe mode >",
    "< For exit: Ctrl+D >": "< For exit: Ctrl+D >",

    "Welcome!": "Welcome!",
    "< Logging performed correctly >": "< Logging performed correctly >",

    "Common Mode": "Common Mode",
    "Standard Mode": "Standard Mode",
    "Logging Mode": "Logging Mode",
    "Rough Mode": "Rough Mode",

    "< Do you want to exit the program? >": "< Do you want to exit the program? >",
    "< Write 'y' or 'Y' to confirm, other to cancel >": "< Write 'y' or 'Y' to confirm, other to cancel >",
    "y": "y",
    "Y": "Y",
    "< Preparing system for shutdown >": "< Preparing system for shutdown >",

    "< There are no sensors >": "< There are no sensors >",
    "< Cancellation completed successfully >": "< Cancellation completed successfully>",
    "Current value": "Current value",
    "Message frequency": "Message frequency",
    "Sampling frequency": "Sampling frequency",

    "< Which parameter do you want to change? >": "< Which parameter do you want to change? >",
    "< Enter current value >": "< Enter current value >",
    "< Enter Sampling frequency >": "< Enter Sampling frequency >",
    "< Enter Message frequency >": "< Enter Message frequency >",

    "< These are all registered sensors >": "< These are all registered sensors >",
    "< Press enter to go back >": "< Press enter to go back >",

    "< There are no systems >": "< There are no systems >",
    "< The sensor has been inserted into the system: ": "< The sensor has been inserted into the system: ",
    "< The sensor is already assigned to a system >": "< The sensor is already assigned to a system >",
    "< Removal from the system performed correctly >": "< Removal from the system performed correctly >",
    "< Total elimination of the sensor correctly executed >": "< Total elimination of the sensor correctly executed >",
    "< There are no sensors associated with this system >": "< There are no sensors associated with this system >",
    "< The sensor is not associated with a system >": "< The sensor is not associated with a system >",
    "< To delete it use the Sensors menu >": "< To delete it use the Sensors menu >",

    "< These are all registered systems >": "< These are all registered systems >",

    "Load Configuration": "Load Configuration",
    "Save Configuration": "Save Configuration",
    "Load from DataBase": "Load from DataBase",
    "Save  to  DataBase": "Save  to  DataBase",

    "< Error: Type of values entered incorrect >": "< Error: Type of values entered incorrect >",
    "< Error: Incorrect values entered >": "< Error: Incorrect values entered >",
    "< Error: The file already exists >": "< Error: The file already exists >",
    "< Error: Can't access to the file >": "< Error: Can't access to the file >",
    "< Error: Input / Output >": "< Error: Input / Output >",
    "< Attention: The script of the program could be compromised, contact responsible >":
        "< Attention: The script of the program could be compromised, contact responsible >",
    "< Error: Generic >": "< Error: Generic >",

    "System name: ": "System name: ",
    "Local: ": "Local: ",
    "None": "None",
    "Kind sensor: ": "Kind sensor: ",
    "Current value: ": "Current value: ",
    "Battery status: ": "Battery status: ",
    "Sampling frequency: ": "Sampling frequency: ",
    "Message frequency: ": "Message frequency: "
}


""" Lists of Systems and Sensors. """
list_systems = []
list_sensors = []


""" Record the starting mode of the program """
program_rec = {"mode_common": False, "mode_standard": False, "mode_logging": False}


def clear():
    """
    Function Clear, clean the screen.
    """
    # Compatibility for Windows:
    if name == 'nt':
        _ = system('cls')

    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        _ = system('clear')


def del_lists():
    """
    Delete the list content for reset the configuration before load a new config file.
    """
    del list_systems[:]
    del list_sensors[:]


def load_lang_choice():
    """ Load Last Language Choice Config from file Json: """
    try:
        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\language\\" + "languages.json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/language/" + "languages.json"

        with open(dir_name, "r") as j:
            data = json.load(j)
            Chosen_Language["English"] = data["English"]
            Chosen_Language["Spanish"] = data["Spanish"]
            Chosen_Language["Italian"] = data["Italian"]
    except:
        clear()
        print("\n" + Lang["< Error: Missing program file 'language' >"] + " ...")
        time.sleep(2)
        return


def save_lang_choice():
    """ Save New Language Choice Config in file Json: """
    # Compatibility for Windows:
    if name == 'nt':
        dir_name = os.getcwd() + "\\language\\" + "languages.json"

    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        dir_name = os.getcwd() + "/language/" + "languages.json"

    with open(dir_name, "w") as file:
        json.dump(dict(Chosen_Language), file)


def load_lang():
    """ Load Language Json Program Config: """
    try:
        global Lang

        if Chosen_Language["English"] is True:
            # Compatibility for Windows:
            if name == 'nt':
                dir_name = os.getcwd() + "\\language\\" + "_english.json"

            # Compatibility for Mac and Linux(os.name: "posix"):
            else:
                dir_name = os.getcwd() + "/language/" + "_english.json"
            with open(dir_name, "r") as j:
                data = json.load(j)
                if data != {}:
                    Lang = data["lang_skel"]  # load language dict in this file
                    lang_build(lang=data["lang_build"])  # load language dict in build file

        elif Chosen_Language["Italian"] is True:
            # Compatibility for Windows:
            if name == 'nt':
                dir_name = os.getcwd() + "\\language\\" + "_italian.json"

            # Compatibility for Mac and Linux(os.name: "posix"):
            else:
                dir_name = os.getcwd() + "/language/" + "_italian.json"
            with open(dir_name, "r") as j:
                data = json.load(j)
                if data != {}:
                    Lang = data["lang_skel"]
                    lang_build(lang=data["lang_build"])

        elif Chosen_Language["Spanish"] is True:
            # Compatibility for Windows:
            if name == 'nt':
                dir_name = os.getcwd() + "\\language\\" + "_spanish.json"

            # Compatibility for Mac and Linux(os.name: "posix"):
            else:
                dir_name = os.getcwd() + "/language/" + "_spanish.json"

            with open(dir_name, "r") as j:
                data = json.load(j)
                if data != {}:
                    Lang = data["lang_skel"]
                    lang_build(lang=data["lang_build"])

    except:
        clear()
        print("\n" + Lang["< Error: Missing program file '_spanish.json' or _italian.json' >"] + " ...")
        time.sleep(2)
        return


def program_state():
    """
    Notify if the program has been started to the file '__main__'.
    """
    main.program_rec["skeleton"] = True


def main_menu():
    """
    Function to create the main menu.
    """
    print("")
    menu = [
        dict(number_menu=1, label_menu=Lang["Management of Sensors"]),
        dict(number_menu=2, label_menu=Lang["Management of Systems"]),
        dict(number_menu=3, label_menu=Lang["Configuration"]),
        dict(number_menu=4, label_menu=Lang["Language"]),
        dict(number_menu=0, label_menu=Lang["Exit"]),
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def language_menu():
    """
    Function to create the language menu.
    """
    print("")
    menu = [
        dict(number_menu=1, label_menu=Lang["English"]),
        dict(number_menu=2, label_menu=Lang["Italian"]),
        dict(number_menu=3, label_menu=Lang["Spanish"]),
        dict(number_menu=0, label_menu=Lang["Back"]),
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def system_change_menu():
    """
    Function to create the systems management menu.
    """
    print("")
    menu = [
        dict(number_menu=1, label_menu=Lang["New     System"]),
        dict(number_menu=2, label_menu=Lang["Delete  System"]),
        dict(number_menu=3, label_menu=Lang["Assign  Sensor"]),
        dict(number_menu=4, label_menu=Lang["Removal Sensor"]),
        dict(number_menu=5, label_menu=Lang["Monitoring"]),
        dict(number_menu=0, label_menu=Lang["Back"]),
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def sensor_change_menu():
    """
    Function to create the sensor management menu.
    """
    print("")
    menu = [

        dict(number_menu=1, label_menu=Lang["New    Sensor"]),
        dict(number_menu=2, label_menu=Lang["Delete Sensor"]),
        dict(number_menu=3, label_menu=Lang["Change Sensor"]),
        dict(number_menu=4, label_menu=Lang["Monitoring"]),
        dict(number_menu=0, label_menu=Lang["Back"]),
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def choose_system():
    """
    Display a numeric list of the systems included in the list: "list_systems".
    :return: Index of the object or False
    """
    clear()
    print("")
    for index in range(0, len(list_systems)):
        print("\n" + str(index+1) + " ) " + list_systems[index].output_view())

    choice = int(input("\n" + Lang["< Choose a System >"] + "\n" +
                       Lang["< Type 0 for go back >"] + "\n\n>>"))
    if choice == 0:
        return False
    else:
        return choice - 1


def choose_sensor():
    """
    Displays a numeric list of sensors inserted in the list: "list_sensors".
    :return: Index of the object or False
    """
    clear()
    print("")
    for index in range(0, len(list_sensors)):
        print("\n" + str(index+1) + " ) " + list_sensors[index].output_view())

    choice = int(input("\n" + Lang["< Choose a Sensor >"] + "\n" +
                       Lang["< Type 0 for go back >"] + "\n\n>>"))
    if choice == 0:
        return False
    else:
        return choice - 1


def eliminate_sensor(choice_sen):
    """ Deletes Sensor Completely """
    for systems in list_systems:
        if list_sensors[choice_sen].system_name == systems.system_name:
            for sensor in systems.environment:
                # Control if the sensors in both list are the same:
                if list_sensors[choice_sen].serial_number == sensor.serial_number:
                    if list_sensors[choice_sen].kind == sensor.kind:
                        # Get the index of the sensor in the obj environment list:
                        index = systems.environment.index(sensor)
                        # Delete the sensor from the system in list_systems:
                        systems.environment.remove(systems.environment[index])
                        clear()
                        print("")
                        print("\n" + Lang["< Removal from the system performed correctly >"] + " ...")
                        time.sleep(1.5)

    clear()
    # Delete the sensor from the list_sensors
    list_sensors.remove(list_sensors[choice_sen])
    logging_point(kind="info", message="Sensor deleted") or print("")
    print("\n" + Lang["< Cancellation completed successfully >"] + " ...")
    time.sleep(1.5)


def eliminate_system(choice):
    """ Disassociates the sensors from the system before removing it completely """
    for sensors in list_systems[choice].environment:
        sensors.system_name = Lang["None"]
    for sensors in list_systems[choice].environment:
        list_systems[choice].environment.remove(sensors)

    """ Delete the system """
    list_systems.remove(list_systems[choice])
    clear()
    logging_point(kind="info", message="System eliminated")
    print("\n" + Lang["< Cancellation completed successfully >"] + " ...")
    time.sleep(1)


def eliminate_sen_from_sys(choice_sys):
    """ Eliminate one sensor from a system environment """
    if list_systems[choice_sys].environment == []:
        print(Lang["< There are no sensors associated with this system >"])
        time.sleep(1)

    else:
        """ Choose the sensor from inside the system obj """
        for index in range(0, len(list_systems[choice_sys].environment)):
            print("\n" + str(index + 1) + " ) " +
                  list_systems[choice_sys].environment[index].output_view())

        choice = int(input("\n" + Lang["< Choose a Sensor >"] + "\n" +
                           Lang["< Type 0 for go back >"] + "\n\n>>"))

        if choice == 0:
            clear()

        else:
            try:
                # Eliminate the sensor system_name attribute in both lists:
                list_systems[choice_sys].environment[choice - 1].system_name = Lang["None"]
                # Eliminate the sensor from the system:
                list_systems[choice_sys].environment.remove(list_systems[choice_sys].environment[choice - 1])
                clear()
                logging_point(kind="info", message="Sensor removal from a system")
                print("\n" + Lang["< Removal from the system performed correctly >"] +
                      " ...")
                time.sleep(2)

            except:
                print("\n" + Lang["< The sensor is not associated with a system >"] + " ...")
                time.sleep(2)


def create_system():
    """
    Create an embedded system.
    """
    temp = build.System()
    temp.system_name = input("\n" + Lang["< Enter the name of the system >"] + "\n" +
                             Lang["< Only letters and numbers without spaces or symbols >"]+"\n\n>>")

    # Prevents the use of words that are used to specify the absence of systems:
    if temp.system_name == "None" or temp.system_name == "Nessuno" or temp.system_name == "Ninguno":
        print("\n" + Lang["< Error: You have not entered a valid name for the system >"] + " ...")
        temp = None
        time.sleep(1.5)

    # Prevents system names from being duplicated:
    for any_system in list_systems:
        if any_system.system_name == temp.system_name:
            print(Lang["< Error: A system with that name already exists >"] + " ...")
            time.sleep(1)
            return

    # Prevents the use of spaces and symbols:
    if temp.system_name.isalpha() or temp.system_name.isalnum():
        clear()

        temp.local = input("\n" + Lang["< Enter the local of the system >"] + "\n" +
                           Lang["< Only letters and numbers without spaces or symbols >"] + "\n\n>>")

        if temp.local.isalpha() or temp.local.isalnum():
            clear()

        else:
            clear()
            print("\n"+Lang["< Error: You have not entered a valid name for the local >"] + " ...")
            temp = None
            time.sleep(1)
    else:
        clear()
        print("\n"+Lang["< Error: You have not entered a valid name for the system >"] + " ...")
        temp = None
        time.sleep(1)

    if temp is None:
        return

    else:
        # Save the system:
        list_systems.append(temp)
        clear()
        logging_point(kind="info", message="System created")
        print("\n" + Lang["< System successfully added >"] + " ...")
        time.sleep(2)
        clear()


def create_sensor(mode):
    """
    Menu: choice a kind of sensor to create.
    Save in "list_sensors" all the sensors created.
    """
    while True:
        clear()
        print("  MENU °°*       " + mode)
        print("\n" + Lang["Create a sensor of:"] + "\n")
        menu = [
            dict(number_menu=1, label_menu=Lang["Light"]),
            dict(number_menu=2, label_menu=Lang["CO2"]),
            dict(number_menu=3, label_menu=Lang["Humidity"]),
            dict(number_menu=4, label_menu=Lang["Infrared"]),
            dict(number_menu=5, label_menu=Lang["NFC"]),
            dict(number_menu=0, label_menu=Lang["Back"])
        ]

        for line in menu:
            print(str(line["number_menu"]) + ". " + line["label_menu"])

        choice2 = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))
        clear()

        if choice2 == 1:
            new_sensor = create_light_sensor()
            list_sensors.append(new_sensor)
            clear()
            logging_point(kind="info", message="Sensor created")
            print("\n" + Lang["< Creation performed correctly >"] + " ...")
            time.sleep(2)

        elif choice2 == 2:
            new_sensor = create_co2_sensor()
            list_sensors.append(new_sensor)
            clear()
            logging_point(kind="info", message="Sensor created")
            print("\n" + Lang["< Creation performed correctly >"] + " ...")
            time.sleep(2)

        elif choice2 == 3:
            new_sensor = create_humidity_sensor()
            list_sensors.append(new_sensor)
            clear()
            logging_point(kind="info", message="Sensor created")
            print("\n" + Lang["< Creation performed correctly >"] + " ...")
            time.sleep(2)

        elif choice2 == 4:
            new_sensor = create_infrared_sensor()
            list_sensors.append(new_sensor)
            clear()
            logging_point(kind="info", message="Sensor created")
            print("\n" + Lang["< Creation performed correctly >"] + " ...")
            time.sleep(2)

        elif choice2 == 5:
            new_sensor = create_nfc_sensor()
            list_sensors.append(new_sensor)
            clear()
            logging_point(kind="info", message="Sensor created")
            print("\n" + Lang["< Creation performed correctly >"] + " ...")
            time.sleep(1.5)

        elif choice2 == 0:
            clear()
            break

        else:
            clear()
            print("\n" + Lang["< Invalid option >"] + " ...")
            time.sleep(1)


def create_light_sensor():
    """
    Create a new light sensor.
    :return: New sensor object.
    """
    temp = build.Light()
    temp.current_value = float(input("\n" + Lang["< Insert current value >"] + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + Lang["< Insert sampling frequency >"] + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + Lang["< Insert message frequency >"] + "\n\n>>"))
    return temp


def create_co2_sensor():
    """
    Create a new CO2 sensor.
    :return: New sensor object.
    """
    temp = build.CO2()
    temp.current_value = float(input("\n" + Lang["< Insert current value >"] + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + Lang["< Insert sampling frequency >"] + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + Lang["< Insert message frequency >"] + "\n\n>>"))
    return temp


def create_humidity_sensor():
    """
    Create a new humidity sensor.
    :return: New sensor object.
    """
    temp = build.Humidity()
    temp.current_value = float(input("\n" + Lang["< Insert current value >"] + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + Lang["< Insert sampling frequency >"] + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + Lang["< Insert message frequency >"] + "\n\n>>"))
    return temp


def create_infrared_sensor():
    """
    Create a new infrared sensor.
    :return: New sensor object.
    """
    temp = build.Infrared()
    temp.current_value = float(input("\n" + Lang["< Insert current value >"] + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + Lang["< Insert sampling frequency >"] + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + Lang["< Insert message frequency >"] + "\n\n>>"))
    return temp


def create_nfc_sensor():
    """
    Create a new NFC sensor.
    :return: New sensor object.
    """
    temp = build.NFC()
    temp.current_value = float(input("\n" + Lang["< Insert current value >"] + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + Lang["< Insert sampling frequency >"] + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + Lang["< Insert message frequency >"] + "\n\n>>"))
    return temp


def load_json():
    """
    Opens a json file and loads all the data.
    Option 1 loads automatically the correct file for the mode in use.
    Option 2 the user must enter the file name.
    """
    menu_load = [
        dict(number_menu=1, label_menu=Lang["Load default config"]),
        dict(number_menu=2, label_menu=Lang["Load saved config"]),
        dict(number_menu=0, label_menu=Lang["Back"]),
    ]

    for line in menu_load:
        print(str(line["number_menu"]) + ". " + line["label_menu"])

    choice = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))
    clear()

    if choice == 1:
        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\config\\default\\" + "config.json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/config/default/" + "config.json"

        with open(dir_name, "r") as j:
            data = json.load(j)

            # Empty the lists, thus eliminating the previous configuration:
            del_lists()

            # Save all the systems in list_systems ignoring the environment list of each system obj:
            for one_system in data["systems"]:
                temp_system = build.System()
                temp_system.system_name = one_system["system_name"]
                temp_system.local = one_system["local"]
                temp_system.environment = []
                list_systems.append(temp_system)

            # Load the sensors in list_sensors and generate a new ID code for each one:
            for sensor in data["sensors"]:
                if sensor["kind"] == "Light" or sensor["kind"] == "Luz" or sensor["kind"] == "Luce":
                    temp_object = build.Light()  # New ID generate here
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "co2" or sensor["kind"] == "CO2":
                    temp_object = build.CO2()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "Humidity" or sensor["kind"] == "Humedad" or sensor["kind"] == "Umidita":
                    temp_object = build.Humidity()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "Infrared" or sensor["kind"] == "Infrarrojo" or sensor["kind"] == "Infrarossi":
                    temp_object = build.Infrared()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "NFC" or sensor["kind"] == "nfc":
                    temp_object = build.NFC()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

            # The new sensors from list_sensors get add into the environment of system obj:
            for systems in list_systems:
                for sensors in list_sensors:
                    if sensors.system_name == systems.system_name:  # Recognizes the system of belonging of each sensor.
                        systems.environment.append(sensors)
                        # Makes an intelligent copy that keeps both objects linked to the respective changes...
                        # excluding deletion, which disassociates objects:
                        for each_sensor in systems.environment:
                            each_sensor = copy.copy(sensors)

            logging_point(kind="info", message="New configuration loaded")
            print("\n" + Lang["< Configuration loaded successfully >"] + " ...")
            time.sleep(2)

    if choice == 2:
        nome_file = input("\n" + Lang["< Insert the name of the file without extension >"] + "\n\n>>")
        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\config\\" + nome_file + ".json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/config/" + nome_file + ".json"

        with open(dir_name, "r") as j:
            data = json.load(j)

            # Empty the lists, thus eliminating the previous configuration:
            del_lists()

            # Save all the systems in list_systems ignoring the environment list of each system obj:
            for one_system in data["systems"]:
                temp_system = build.System()
                temp_system.system_name = one_system["system_name"]
                temp_system.local = one_system["local"]
                temp_system.environment = []
                list_systems.append(temp_system)

            # Load the sensors in list_sensors and generate a new ID code for each one:
            for sensor in data["sensors"]:
                if sensor["kind"] == "Light" or sensor["kind"] == "Luz" or sensor["kind"] == "Luce":
                    temp_object = build.Light()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "co2" or sensor["kind"] == "CO2":
                    temp_object = build.CO2()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "Humidity" or sensor["kind"] == "Humedad" or sensor["kind"] == "Umidita":
                    temp_object = build.Humidity()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "Infrared" or sensor["kind"] == "Infrarrojo" or sensor["kind"] == "Infrarossi":
                    temp_object = build.Infrared()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

                elif sensor["kind"] == "NFC" or sensor["kind"] == "nfc":
                    temp_object = build.NFC()
                    temp_object.kind = sensor["kind"]
                    temp_object.current_value = sensor["current_value"]
                    temp_object.battery_status = sensor["battery_status"]
                    temp_object.message_freq = sensor["message_freq"]
                    temp_object.sampling_freq = sensor["sampling_freq"]
                    temp_object.system_name = sensor["system_name"]
                    list_sensors.append(temp_object)

            # The new sensors from list_sensors get add into the environment of system obj:
            for systems in list_systems:
                for sensors in list_sensors:
                    if sensors.system_name == systems.system_name:  # Recognizes the system of belonging of each sensor.
                        systems.environment.append(sensors)
                        # Makes an intelligent copy that keeps both objects linked to the respective changes...
                        # excluding deletion, which disassociates objects:
                        for each_sensor in systems.environment:
                            each_sensor = copy.copy(sensors)

            logging_point(kind="info", message="New configuration loaded")
            print("\n" + Lang["< Configuration loaded successfully >"] + " ...")
            time.sleep(2)

    if choice == 0:
        clear()
        return


def load_json_auto(file_name):
    """
    Automatically upload the config file.
    """
    # Compatibility for Windows:
    if name == 'nt':
        dir_name = os.getcwd() + "\\config\\default\\"+file_name+".json"

    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        dir_name = os.getcwd() + "/config/default/"+file_name+".json"

    with open(dir_name, "r") as j:
        data = json.load(j)

        # Empty the lists, thus eliminating the previous configuration:
        del_lists()

        # Save all the systems in list_systems ignoring the environment list of each system obj:
        for one_system in data["systems"]:
            temp_system = build.System()
            temp_system.system_name = one_system["system_name"]
            temp_system.local = one_system["local"]
            temp_system.environment = []
            list_systems.append(temp_system)

        # Load the sensors in list_sensors and generate a new ID code for each one:
        for sensor in data["sensors"]:
            if sensor["kind"] == "Light" or sensor["kind"] == "Luz" or sensor["kind"] == "Luce":
                temp_object = build.Light()
                temp_object.kind = sensor["kind"]
                temp_object.current_value = sensor["current_value"]
                temp_object.battery_status = sensor["battery_status"]
                temp_object.message_freq = sensor["message_freq"]
                temp_object.sampling_freq = sensor["sampling_freq"]
                temp_object.system_name = sensor["system_name"]
                list_sensors.append(temp_object)

            elif sensor["kind"] == "co2" or sensor["kind"] == "CO2":
                temp_object = build.CO2()
                temp_object.kind = sensor["kind"]
                temp_object.current_value = sensor["current_value"]
                temp_object.battery_status = sensor["battery_status"]
                temp_object.message_freq = sensor["message_freq"]
                temp_object.sampling_freq = sensor["sampling_freq"]
                temp_object.system_name = sensor["system_name"]
                list_sensors.append(temp_object)

            elif sensor["kind"] == "Humidity" or sensor["kind"] == "Humedad" or sensor["kind"] == "Umidita":
                temp_object = build.Humidity()
                temp_object.kind = sensor["kind"]
                temp_object.current_value = sensor["current_value"]
                temp_object.battery_status = sensor["battery_status"]
                temp_object.message_freq = sensor["message_freq"]
                temp_object.sampling_freq = sensor["sampling_freq"]
                temp_object.system_name = sensor["system_name"]
                list_sensors.append(temp_object)

            elif sensor["kind"] == "Infrared" or sensor["kind"] == "Infrarrojo" or sensor["kind"] == "Infrarossi":
                temp_object = build.Infrared()
                temp_object.kind = sensor["kind"]
                temp_object.current_value = sensor["current_value"]
                temp_object.battery_status = sensor["battery_status"]
                temp_object.message_freq = sensor["message_freq"]
                temp_object.sampling_freq = sensor["sampling_freq"]
                temp_object.system_name = sensor["system_name"]
                list_sensors.append(temp_object)

            elif sensor["kind"] == "NFC" or sensor["kind"] == "nfc":
                temp_object = build.NFC()
                temp_object.kind = sensor["kind"]
                temp_object.current_value = sensor["current_value"]
                temp_object.battery_status = sensor["battery_status"]
                temp_object.message_freq = sensor["message_freq"]
                temp_object.sampling_freq = sensor["sampling_freq"]
                temp_object.system_name = sensor["system_name"]
                list_sensors.append(temp_object)

        # The new sensors from list_sensors get add into the environment of system obj:
        for systems in list_systems:
            for sensors in list_sensors:
                if sensors.system_name == systems.system_name:  # Recognizes the system of belonging of each sensor.
                    systems.environment.append(sensors)
                    # Makes an intelligent copy that keeps both objects linked to the respective changes...
                    # excluding deletion, which disassociates objects:
                    for each_sensor in systems.environment:
                        each_sensor = copy.copy(sensors)

        logging_point(kind="info", message="Configuration restored")


def save_json():
    """
    Create a json file and save all data.
    The user must enter the file name.
    """
    try:
        if list_systems == [] and list_sensors == []:
            clear()
            print("\n" + Lang["< There is no data to save >"])

        list_temp_systems = []
        list_temp_sensors = []

        if list_systems != "":
            # Transform Python object into dictionary:
            for systems in list_systems:
                # sys_name is a parameter of to_dict function, helps to identify the sensors systems location right.
                sys_name = systems.system_name
                list_temp_systems.append(systems.to_dict(sys_name))

        if list_sensors != "":
            # Transform Python object into dictionary:
            list_temp_sensors = []
            for elem in list_sensors:
                list_temp_sensors.append(elem.to_dict())

        file_name = input("\n" + Lang["< Save the config >"] + "\n" +
                          Lang["< Insert the name of the file without extension >"] + "\n\n>>")
        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\config\\" + file_name + ".json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/config/" + file_name + ".json"

        with open(dir_name, "w") as file:
            json.dump(dict(systems=list_temp_systems, sensors=list_temp_sensors), file)
            clear()
            print("\n" + Lang["< Configuration saved successfully >"] + " ...")
            time.sleep(2)

    except:
        clear()
        print("\n" + Lang["< Error saving the file >"])


def save_json_auto(file_name):
    """
    Automatically save the config file.
    """
    try:

        if list_systems == [] and list_sensors == []:
            clear()
            print("\n" + Lang["< There is no data to save >"])

        list_temp_systems = []
        list_temp_sensors = []

        if list_systems != "":
            # Transform Python object into dictionary:
            for systems in list_systems:
                # sys_name is a parameter of to_dict function, helps to identify the sensors systems location right.
                sys_name = systems.system_name
                list_temp_systems.append(systems.to_dict(sys_name))

        if list_sensors != "":
            # Transform Python object into dictionary:
            list_temp_sensors = []
            for elem in list_sensors:
                list_temp_sensors.append(elem.to_dict())

        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\config\\default\\" + file_name + ".json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/config/default/" + file_name + ".json"

        with open(dir_name, "w") as file:
            json.dump(dict(systems=list_temp_systems, sensors=list_temp_sensors), file)

    except:
        clear()
        print("\n" + Lang["< Error saving the file >"])


def save_in_database():
    """
    Save the config in a database online.
    """
    try:
        print("")
        # User of the database cloud:
        user = input(Lang["User Name: "])
        clear()
        print("")
        # Password of the database cloud:
        password = getpass(Lang["Password: "])
        clear()
        clear()
        client = MongoClient("mongodb+srv://" + user + ":" + password +
                             "@db-cloud-a14d2.gcp.mongodb.net/test?retryWrites=true")
        clear()
        db = client["Central_System"]
        db_name = input("\n" + Lang["< Choose the name of the DataBase >"] + "\n" +
                        Lang["< If you write a new name a new DataBase will be created >"] + "\n\n>>")
        database = db[db_name]

    except:
        clear()
        print("\n" + Lang["< Error: control your internet connection >"] + " ...")
        time.sleep(2)
        return

    list_temp_sys = []
    list_temp_sen = []

    if list_systems != "":
        # Transform Python object into dictionary:
        for systems in list_systems:
            # sys_name is a parameter of to_dict function, helps to identify the sensors systems location right.
            sys_name = systems.system_name
            list_temp_sys.append(systems.to_dict(sys_name))

    if list_sensors != "":
        # Transform Python object into dictionary:
        for elem in list_sensors:
            list_temp_sen.append(elem.to_dict())

    try:
        result = database.insert_one(dict(systems=list_temp_sys, sensors=list_temp_sen))
        print("\n" + Lang["< The information was successfully uploaded to the server >"] + " ...")
        time.sleep(2)
        clear()
        input("\n" + Lang["< The ID of the file is: "] + str(result.inserted_id) + " >" + "\n\n" +
              Lang["< Press enter to go back >"] + "\n\n>>")

    except:
        clear()
        print("\n" + Lang["< Error: can't access to the data base server >"] + "\n" +
              Lang["< Control your credentials >"] + " ...")
        time.sleep(2)


def load_from_database(mode):
    """
    Load the config from a database online.
    :param mode: For view what's the Program mode in the menu
    :return: (except) exit from function
    """
    try:
        print("")
        # User of the database cloud:
        user = input(Lang["User Name: "])
        clear()
        print("")
        # Password of the database cloud:
        password = getpass(Lang["Password: "])
        clear()
        clear()
        client = MongoClient("mongodb+srv://" + user + ":" + password +
                             "@db-cloud-a14d2.gcp.mongodb.net/test?retryWrites=true")
        db = client["Central_System"]

    except:
        clear()
        print("\n" + Lang["< Error: control your internet connection >"] + " ...")
        time.sleep(2)
        return

    while True:
        clear()
        print("  MENU °°*       " + mode)
        print("")
        menu = [
            dict(number_menu=1, label_menu=Lang["Show all the config files in DB"]),
            dict(number_menu=2, label_menu=Lang["Download config file from DB"]),
            dict(number_menu=0, label_menu=Lang["Back"]),
        ]
        for line in menu:
            print(str(line["number_menu"]) + ". " + line["label_menu"])
        choice = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))

        try:
            if choice == 1:
                """Show all the documents in the database"""
                clear()
                print("\n" + Lang["< Files in the database >"])
                for collection_name in db.list_collection_names({}):
                    print("\n")
                    print("-"*60)
                    print(Lang["File name: "] + collection_name + "\n")
                    for document in db[collection_name].find():
                        pprint.pprint(document)
                input(Lang["< Press enter to go back >"] + "\n\n>>")
                clear()

            elif choice == 2:
                """Print the name of all the files in the server"""
                clear()
                print("\n" + Lang["< List of all the files in the server >"] + "\n")
                for collection_name in db.list_collection_names({}):
                    print(collection_name)

                """Select one DataBase by input and save it in a Json file"""
                db_name = input("\n" + Lang["< Insert the name of a file >"] + "\n\n>>")
                for collection_name in db.list_collection_names({}):
                    if collection_name == db_name:
                        database = db[db_name]
                        for doc in database.find():

                            # Compatibility for Windows:
                            if name == 'nt':
                                dir_name = os.getcwd() + "\\config\\" + db_name + ".json"

                            # Compatibility for Mac and Linux(os.name: "posix"):
                            else:
                                dir_name = os.getcwd() + "/config/" + db_name + ".json"

                            with open(dir_name, "w") as file:
                                json.dump(dict(systems=doc["systems"], sensors=doc["sensors"]), file)
                                clear()
                                print(Lang["New file created: "]+db_name+".json" + " ...")
                                time.sleep(2)

            elif choice == 0:
                clear()
                break

        except:
            clear()
            print("\n" + Lang["< Error: can't access to the data base server >"] + "\n" +
                  Lang["< Control your credentials >"] + " ...")
            time.sleep(2)
            break


def structure_m(user, pwd, recipient, subject, body):
    """
    Function that creates the structure to send communications via email.
    :param user: User account
    :param pwd: Password account
    :param recipient: Address to send the email
    :param subject: Subject of the message
    :param body: Message
    """
    import smtplib
    _gmail_user = user
    _gmail_pass = pwd
    _from = user
    _to = recipient if type(recipient) is list else [recipient]
    _subject = subject
    _text = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (_from, ", ".join(_to), _subject, _text)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(_gmail_user, _gmail_pass)
        server.sendmail(_from, _to, message)
        server.close()

    except:
        clear()
        print(Lang["< Your Internet is off, use the safe mode >"] + " ...")
        time.sleep(5)
        print("\n\n" + Lang["< For exit: Ctrl+D >"])
        breakpoint()


def format_m(value):
    """
    Fill the email details.
    :param value: Message of the email
    """

    # For send only some notifications:
    actualdate = datetime.datetime.now().strftime("Day: " + "%Y-%m-%d" + " - Time: " + "%H:%M:%S")
    data = "Log captured at: \n" + actualdate + "\n\nSome one is using my program." +\
           "\n\n\nMessaggio: \n" + value + "\n\n\n" + "All Data: \n" + str(data_lg())
    structure_m("email_from@gmail.com", "password_email_from", "email_to@gmail.com",
                "Alert: New entry - " + actualdate, data)


def data_lg():
    """
    Read the system_log file with all the logging info.
    :return: text in system_log file
    """
    # Compatibility for Windows:
    if name == 'nt':
        dir_name = os.getcwd() + "\\log\\" + "system_log"

    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        dir_name = os.getcwd() + "/log/" + "system_log"

    """ The system_log file is created by the logging module. """
    with open(dir_name, "r") as txt:
        text = txt.read().splitlines()
        txt.close()

    if text != "":
        return text
    else:
        return "Empty Data"


def logging_function():
    """ Create system_log file and insert a whole series of information. """
    # Compatibility for Windows:
    if name == 'nt':
        logging.basicConfig(filename=os.getcwd() + "\\log\\" + "system_log", level=logging.DEBUG,
                            format="%(levelname)s: %(message)s    |    Data: %(asctime)s")
        filename = os.getcwd() + "\\log\\" + "system_log"
    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        logging.basicConfig(filename=os.getcwd() + "/log/" + "system_log", level=logging.DEBUG,
                            format="%(message)s    |    Data: %(asctime)s")
        filename = os.getcwd() + "/log/" + "system_log"

    """ Data entry. """
    name_user = str(input("Insert your name: "))
    logging.info("User: " + name_user)
    clear()

    """ Read the system_log file created by the logging module. """
    with open(filename, "r") as txt:
        line = txt.read().splitlines()
        txt.close()

    """ Print the last user entered in log_person. """
    print("\n" + Lang["Welcome!"] + "\n\n" + line[-1])
    time.sleep(1.5)
    clear()
    print("\n" + Lang["< Logging performed correctly >"])
    # format_m(value="User: "+str(name_user)+"\n"+"Program: "+str(program_mode()) + " ...")   # Send Email
    time.sleep(3)


def logging_last_line():
    """ Create system_log file and insert a whole series of information. """
    # Compatibility for Windows:
    if name == 'nt':
        logging.basicConfig(filename=os.getcwd() + "\\log\\" + "system_log", level=logging.DEBUG,
                            format="%(message)s    |    Data: %(asctime)s")
        filename = os.getcwd() + "\\log\\" + "system_log"
    # Compatibility for Mac and Linux(os.name: "posix"):
    else:
        logging.basicConfig(filename=os.getcwd() + "/log/" + "system_log", level=logging.DEBUG,
                            format="%(message)s    |    Data: %(asctime)s")
        filename = os.getcwd() + "/log/" + "system_log"

    with open(filename, "r") as txt:
        line = txt.read().splitlines()
        # format_m(value=line[-1])   # Send Email
        txt.close()

    # Print the last data entered in system_log:
    if line[-1] != "":
        print(line[-1])


def logging_point(kind, message):
    """ Logging Point: """
    # Control if the logging mode is in use:
    if program_rec["mode_logging"] is True:

        # Activate the log:
        if kind == "debug":
            logger = logging.getLogger()
            logger.debug(message)
            logging_last_line()
            time.sleep(2)

        if kind == "info":
            logger = logging.getLogger()
            logger.info(message)
            logging_last_line()
            time.sleep(2)

        if kind == "warning":
            logger = logging.getLogger()
            logger.warning(message)
            logging_last_line()
            time.sleep(2)

        if kind == "error":
            logger = logging.getLogger()
            logger.error(message)
            logging_last_line()
            time.sleep(2)

        if kind == "critical":
            logger = logging.getLogger()
            logger.critical(message)
            logging_last_line()
            time.sleep(2)

    else:
        return


def mode_common():
    """
    Upload the changes for the program's common launch mode.
    """
    load_json_auto(file_name="common")
    program_rec["mode_common"] = True
    program_start()


def mode_standard():
    """
    Upload the changes for the program's standard launch mode.
    """
    load_json_auto(file_name="standard")
    program_rec["mode_standard"] = True
    program_start()


def mode_logging():
    """
    Upload changes for the program's logging launch mode.
    """
    load_json_auto(file_name="config")
    program_rec["mode_logging"] = True
    logging_function()
    program_start()


def program_mode():
    """
    Determines the mode of program launch made.
    :return: mode is used in the print of the menu
    """
    if program_rec["mode_common"] is True:
        mode = Lang["Common Mode"]
    elif program_rec["mode_standard"] is True:
        mode = Lang["Standard Mode"]
    elif program_rec["mode_logging"] is True:
        mode = Lang["Logging Mode"]
    else:
        mode = Lang["Rough Mode"]
    return mode


def program_start():
    """
    --Structure of the Program--
    Recall the functions entered above and interacts
    with System and Sensor classes in the file: "build".
    """
    program_state()  # Notify program start to the file '__main__'
    # format_m(value="Program Start")   # Send Email
    load_lang_choice()  # Load the last choice of language
    """ Load the last selected language """
    if Chosen_Language["English"] is False:
        load_lang()

    program_mode()  # Determines the launch mode of the program
    clear()
    while True:
        mode = program_mode()  # keeps the variable updated in case the language changes
        try:
            """ Main Menu """
            clear()
            print("  MENU *°°       " + mode)
            main_menu()
            choice_mp = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))

            if choice_mp == 0:
                """ Shutdown """
                clear()
                print(Lang["< Do you want to exit the program? >"])
                shutdown = input("\n\n" + Lang["< Write 'y' or 'Y' to confirm, other to cancel >"] + "\n\n>>")

                if shutdown == Lang["y"] or shutdown == Lang["Y"]:
                    clear()
                    logging_point(kind="info", message=str(shutdown))
                    print(Lang["< Preparing system for shutdown >"] + " ...")

                    """ Auto save the config only in common mode """
                    if program_rec["mode_common"] is True:
                        save_json_auto("common")

                    """ Informs that the program is closing 
                        correctly to the 'main' file """
                    main.power(True)
                    time.sleep(1.5)
                    break

                elif shutdown != Lang["y"] and shutdown != Lang["Y"]:
                    continue

            elif choice_mp == 1:
                """
                Menu to interact with the sensors.
                """
                while True:
                    clear()
                    print("  MENU °*°       "+mode)
                    sensor_change_menu()
                    choice_ms = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))

                    if choice_ms == 0:
                        clear()
                        break

                    elif choice_ms == 1:
                        """
                        Create a sensor.
                        """
                        create_sensor(mode)

                    elif choice_ms == 2:
                        """
                        Eliminate a sensor.
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + Lang["< There are no sensors >"] + " ...")
                            time.sleep(1)

                        else:
                            choice_sen = choose_sensor()

                            if choice_sen is False:
                                """ Go back option """
                                clear()
                                break

                            else:
                                eliminate_sensor(choice_sen)

                    elif choice_ms == 3:
                        """
                        Change the parameters of a sensor.
                        """
                        clear()

                        if list_sensors == []:
                            print("\n" + Lang["< There are no sensors >"] + " ...")
                            time.sleep(1)

                        else:
                            choosen_sensor = choose_sensor()

                            if choosen_sensor is False:
                                """ Go back option """
                                clear()

                            else:
                                """ Sensors from list_sensors and list_systems are 
                                    slightly connected with copy.copy library """
                                while True:
                                    clear()
                                    print("  MENU °°*       "+mode)
                                    change_menu_sen = [
                                        dict(number_menu=1, label_menu=Lang["Current value"]),
                                        dict(number_menu=2, label_menu=Lang["Message frequency"]),
                                        dict(number_menu=3, label_menu=Lang["Sampling frequency"]),
                                        dict(number_menu=0, label_menu=Lang["Back"]),
                                    ]
                                    print("")
                                    for line in change_menu_sen:
                                        print(str(line["number_menu"]) + ". " + line["label_menu"])

                                    choice_mod_sen = int(input("\n" +
                                                               Lang["< Which parameter do you want to change? >"] +
                                                               "\n\n>>"))

                                    if choice_mod_sen == 0:
                                        clear()
                                        break

                                    elif choice_mod_sen == 1:
                                        clear()
                                        temp_num = float(input("\n" + Lang["< Enter current value >"] + "\n\n>>"))
                                        list_sensors[choosen_sensor].current_value = temp_num

                                    elif choice_mod_sen == 2:
                                        clear()
                                        temp_num = float(input("\n" + Lang["< Enter Sampling frequency >"] + "\n\n>>"))
                                        list_sensors[choosen_sensor].message_freq = temp_num

                                    elif choice_mod_sen == 3:
                                        clear()
                                        temp_num = float(input("\n" + Lang["< Enter Message frequency >"] + "\n\n>>"))
                                        list_sensors[choosen_sensor].sampling_freq = temp_num

                                    else:
                                        clear()
                                        print("\n" + Lang["< Invalid option >"] + " ...")
                                        time.sleep(1)

                    elif choice_ms == 4:
                        """
                        Monitoring sensors.
                        View all the sensors.
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + Lang["< There are no sensors >"] + " ...")
                            time.sleep(1)

                        else:
                            clear()
                            for index in range(0, len(list_sensors)):
                                print("\n" + str(index+1) + " ) " + list_sensors[index].output_view())
                            print("\n" + Lang["< These are all registered sensors >"])
                            input(Lang["< Press enter to go back >"] + "\n\n>>")

                    else:
                        clear()
                        print("\n" + Lang["< Invalid option >"] + " ...")
                        time.sleep(1)

            elif choice_mp == 2:
                """
                Menu for interacting with systems.
                """
                while True:
                    clear()
                    print("  MENU °*°       "+mode)
                    system_change_menu()
                    choice_mod_sys = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))

                    if choice_mod_sys == 0:
                        clear()
                        break

                    elif choice_mod_sys == 1:
                        """
                        Create a system.
                        """
                        clear()
                        create_system()

                    elif choice_mod_sys == 2:
                        """
                        Eliminate a system:
                        """
                        clear()
                        if list_systems == []:
                            print("\n" + Lang["< There are no systems >"] + " ...")
                            time.sleep(1)

                        else:
                            choice = choose_system()

                            if choice is False:
                                """ Go back option """
                                clear()

                            else:
                                eliminate_system(choice)

                    elif choice_mod_sys == 3:
                        """
                        Assign a sensor to the system.
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + Lang["< There are no sensors >"] + " ...")
                            time.sleep(1)

                        else:
                            clear()
                            sensor = choose_sensor()

                            if sensor is False:
                                """ Go back option """
                                clear()

                            else:
                                """ Controls that the sensor is not in a system """
                                if list_sensors[sensor].system_name == "None" or \
                                        list_sensors[sensor].system_name == "Nessuno" or \
                                        list_sensors[sensor].system_name == "Ninguno":

                                    # Controls that at least one system exist:
                                    if list_systems == []:
                                        print("\n" + Lang["< There are no systems >"] + " ...")
                                        time.sleep(1.5)

                                    else:
                                        # Select the system:
                                        one_system = choose_system()

                                        if one_system is False:
                                            """ Go back option """
                                            clear()

                                        else:
                                            # Add the sensor to the system environment:
                                            list_systems[one_system].environment.append(list_sensors[sensor])
                                            # Assign the sensor from inside of the sistem to a variable:
                                            sensor1 = list_systems[one_system].environment[-1]
                                            # Connect the sensor from list_sensors with the sensor of in the system:
                                            sensor1 = copy.copy(list_sensors[sensor])
                                            # Modifies the name of the system to which the sensor belongs, ...
                                            # it is no longer necessary to apply the modifies also to the other:
                                            list_sensors[sensor].system_name = list_systems[one_system].system_name
                                            clear()
                                            logging_point(kind="info", message="Sensor inserted in system")
                                            print("\n" + Lang["< The sensor has been inserted into the system: "] +
                                                  list_systems[one_system].system_name + " ...")
                                            time.sleep(2)

                                else:
                                    print(Lang["< The sensor is already assigned to a system >"] + " ...")
                                    time.sleep(2)

                    elif choice_mod_sys == 4:
                        """
                        Removes sensor from a system.
                        The sensor continues to be in "list_sensors".
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + Lang["< There are no sensors >"] + " ...")
                            time.sleep(1)

                        elif list_systems == []:
                            print("\n" + Lang["< There are no systems >"] + " ...")
                            time.sleep(1)

                        else:
                            clear()

                            """ Choose the system """
                            choice_sys = choose_system()

                            if choice_sys is False:
                                """ Go back option """
                                clear()

                            else:
                                clear()
                                eliminate_sen_from_sys(choice_sys)

                    elif choice_mod_sys == 5:
                        """
                        System monitoring.
                        View all inserted systems.
                        """
                        clear()
                        if list_systems == []:
                            print("\n" + Lang["< There are no systems >"] + " ...")
                            time.sleep(1)

                        else:
                            clear()
                            for index in range(0, len(list_systems)):
                                print("\n" + str(index+1) + " ) " + list_systems[index].output_view())
                            print("\n" + Lang["< These are all registered systems >"])
                            input(Lang["< Press enter to go back >"] + "\n\n>>")

                    else:
                        clear()
                        print("\n" + Lang["< Invalid option >"] + " ...")
                        time.sleep(1)

            elif choice_mp == 3:
                """
                Save or load configuration menu.
                """
                clear()
                print("  MENU °*°       "+mode)
                menu_config = [
                    dict(number_menu=1, label_menu=Lang["Load Configuration"]),
                    dict(number_menu=2, label_menu=Lang["Save Configuration"]),
                    dict(number_menu=3, label_menu=Lang["Load from DataBase"]),
                    dict(number_menu=4, label_menu=Lang["Save  to  DataBase"]),
                    dict(number_menu=0, label_menu=Lang["Back"]),
                ]
                print("")
                for line in menu_config:
                    print(str(line["number_menu"]) + ". " + line["label_menu"])
                choice_m_conf = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))

                if choice_m_conf == 0:
                    clear()

                elif choice_m_conf == 1:
                    """ Load Json Config """
                    clear()
                    print("")
                    load_json()

                elif choice_m_conf == 2:
                    """ Save Json Config """
                    clear()
                    save_json()

                elif choice_m_conf == 3:
                    """ Load config from Database """
                    clear()
                    load_from_database(mode=mode)
                    time.sleep(1)

                elif choice_m_conf == 4:
                    """ Save config to Database """
                    clear()
                    save_in_database()

                else:
                    clear()
                    print("\n" + Lang["< Invalid option >"] + " ...")
                    time.sleep(1)

            elif choice_mp == 4:
                """ Language Options """
                clear()
                print("  MENU °*°       " + mode)
                language_menu()
                choice_lang = int(input("\n" + Lang["< Choose a number from the menu >"] + "\n\n>>"))
                if choice_lang == 0:
                    clear()

                elif choice_lang == 1:
                    Chosen_Language["English"] = True
                    Chosen_Language["Spanish"] = False
                    Chosen_Language["Italian"] = False
                    save_lang_choice()
                    load_lang()

                elif choice_lang == 2:
                    Chosen_Language["English"] = False
                    Chosen_Language["Spanish"] = False
                    Chosen_Language["Italian"] = True
                    save_lang_choice()
                    load_lang()

                elif choice_lang == 3:
                    Chosen_Language["English"] = False
                    Chosen_Language["Spanish"] = True
                    Chosen_Language["Italian"] = False
                    save_lang_choice()
                    load_lang()

                else:
                    clear()
                    print("\n" + Lang["< Invalid option >"] + " ...")
                    time.sleep(1)

            else:
                clear()
                print("\n" + Lang["< Invalid option >"] + " ...")
                time.sleep(1)

            """ Error handling: """
        except TypeError:
            clear()
            logging_point(kind="error", message="< Type of values entered incorrect >")
            print(Lang["< Error: Type of values entered incorrect >"] + " ...")
            time.sleep(2)
            continue

        except ValueError:
            clear()
            logging_point(kind="error", message="< Error: Incorrect values entered >")
            print(Lang["< Error: Incorrect values entered >"] + " ...")
            time.sleep(2)
            continue

        except FileExistsError:
            clear()
            logging_point(kind="error", message="< The file already exists >")
            print(Lang["< Error: The file already exists >"] + " ...")
            time.sleep(2)
            continue

        except FileNotFoundError:
            clear()
            logging_point(kind="error", message="< Error: Can't access to the file >")
            print(Lang["< Error: Can't access to the file >"] + " ...")
            time.sleep(2)
            continue

        except IOError:
            clear()
            logging_point(kind="error", message="< Input / Output >")
            print(Lang["< Error: Input / Output >"] + " ...")
            time.sleep(2)
            continue

        except SyntaxError:
            clear()
            logging_point(kind="critical", message="< Script of the program could be compromised >")
            print(Lang["< Attention: The script of the program could be compromised, contact responsible >"] + " ...")
            time.sleep(4)
            exit(1)

        except:
            clear()
            logging_point(kind="error", message="< Generic  >") and print("")
            print(Lang["< Error: Generic >"] + " ...")
            time.sleep(2)
            break
