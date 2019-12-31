# -*- coding: utf-8 -*-
"""
todo: Documentation

    -*- Version: Safe -*-
    -*- Function: Structure of the program -*-

    Project name: Central System
    File name: secure

    Date created: 20/03/2019
    Date last modified: 31/12/2019
    Status: Stable

    Python version: 3.8
    Modules required: pymongo, pprint, copy, json, time, os
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
from os import system, name
from pymongo import MongoClient

# scripts:
import scripts.build as build
import __main__ as main


""" Lists of Systems and Sensors. """
list_systems = []
list_sensors = []


""" Record the starting mode of the program """
program_reg = {"mode_safe": True}


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


def program_state():
    """
    Notify if the program has been started or not to the file '__main__'.
    """
    main.program_rec["secure"] = True


def main_menu():
    """
    Function to create the main menu.
    """
    print("")
    menu = [
        dict(number_menu=1, label_menu="Management of Sensors"),
        dict(number_menu=2, label_menu="Management of Systems"),
        dict(number_menu=3, label_menu="Configuration"),
        dict(number_menu=0, label_menu="Exit")
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def system_change_menu():
    """
    Function to create the systems management menu.
    """
    print("")
    menu = [
        dict(number_menu=1, label_menu="New     System"),
        dict(number_menu=2, label_menu="Delete  System"),
        dict(number_menu=3, label_menu="Assign  Sensor"),
        dict(number_menu=4, label_menu="Removal Sensor"),
        dict(number_menu=5, label_menu="Monitoring"),
        dict(number_menu=0, label_menu="Back"),
    ]
    for line in menu:
        print(str(line["number_menu"]) + ". " + line["label_menu"])


def sensor_change_menu():
    """
    Function to create the sensor management menu.
    """
    print("")
    menu = [

        dict(number_menu=1, label_menu="New    Sensor"),
        dict(number_menu=2, label_menu="Delete Sensor"),
        dict(number_menu=3, label_menu="Change Sensor"),
        dict(number_menu=4, label_menu="Monitoring"),
        dict(number_menu=0, label_menu="Back"),
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

    choice = int(input("\n" + "< Choose a System >" + "\n" +
                       "< Type 0 for go back >" + "\n\n>>"))
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

    choice = int(input("\n" + "< Choose a Sensor >" + "\n" +
                       "< Type 0 for go back >" + "\n\n>>"))
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
                        print("\n" + "< Removal from the system performed correctly >" + " ...")
                        time.sleep(1.5)

    clear()
    # Delete the sensor from the list_sensors
    list_sensors.remove(list_sensors[choice_sen])
    print("\n" + "< Cancellation completed successfully >" + " ...")
    time.sleep(1.5)


def eliminate_system(choice):
    """ Disassociates the sensors from the system before removing it completely """
    for sensors in list_systems[choice].environment:
        sensors.system_name = "None"
    for sensors in list_systems[choice].environment:
        list_systems[choice].environment.remove(sensors)

    """ Delete the system """
    list_systems.remove(list_systems[choice])
    clear()
    print("\n" + "< Cancellation completed successfully >" + " ...")
    time.sleep(1)


def eliminate_sen_from_sys(choice_sys):
    """ Eliminate one sensor from a system environment """
    if list_systems[choice_sys].environment == []:
        print("< There are no sensors associated with this system >")
        time.sleep(1)

    else:
        """ Choose the sensor from inside the system obj """
        for index in range(0, len(list_systems[choice_sys].environment)):
            print("\n" + str(index + 1) + " ) " +
                  list_systems[choice_sys].environment[index].output_view())

        choice = int(input("\n" + "< Choose a Sensor >" + "\n" +
                           "< Type 0 for go back >" + "\n\n>>"))

        if choice == 0:
            clear()

        else:
            try:
                # Eliminate the sensor system_name attribute in both lists:
                list_systems[choice_sys].environment[choice - 1].system_name = "None"
                # Eliminate the sensor from the system:
                list_systems[choice_sys].environment.remove(list_systems[choice_sys].environment[choice - 1])
                clear()
                print("\n" + "< Removal from the system performed correctly >" + " ...")
                time.sleep(2)

            except:
                print("\n" + "< The sensor is not associated with a system >" + " ...")
                time.sleep(2)


def create_system():
    """
    Create an embedded system.
    """
    temp = build.System()

    temp.system_name = input("\n" + "< Enter the name of the system >" + "\n" +
                             "< Only letters and numbers without spaces or symbols >"+"\n\n>>")

    # Prevents the use of words that are used to specify the absence of systems:
    if temp.system_name == "None" or temp.system_name == "Nessuno" or temp.system_name == "Ninguno":
        print("\n" + "< Error: You have not entered a valid name for the system >" + " ...")
        temp = None
        time.sleep(1)

    # Prevents system names from being duplicated:
    for any_system in list_systems:
        if any_system.system_name == temp.system_name:
            print("< Error: A system with that name already exists >" + " ...")
            time.sleep(1)
            return

    # Prevents the use of spaces and symbols:
    if temp.system_name.isalpha() or temp.system_name.isalnum():
        clear()

        temp.local = input("\n" + "< Enter the local of the system >" + "\n" +
                           "< Only letters and numbers without spaces or symbols >" + "\n\n>>")
        if temp.local.isalpha() or temp.local.isalnum():
            clear()

        else:
            clear()
            print("\n"+"< Error: You have not entered a valid name for the local >" + " ...")
            temp = None
            time.sleep(1)
    else:
        clear()
        print("\n"+"< Error: You have not entered a valid name for the system >" + " ...")
        temp = None
        time.sleep(1)

    if temp is None:
        return

    else:
        # Save the system:
        list_systems.append(temp)
        clear()
        print("\n" + "< System successfully added >" + " ...")
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
        print("\n" + "Create a sensor of:" + "\n")
        menu = [
            dict(number_menu=1, label_menu="Light"),
            dict(number_menu=2, label_menu="CO2"),
            dict(number_menu=3, label_menu="Humidity"),
            dict(number_menu=4, label_menu="Infrared"),
            dict(number_menu=5, label_menu="NFC"),
            dict(number_menu=0, label_menu="Back")
        ]

        for line in menu:
            print(str(line["number_menu"]) + ". " + line["label_menu"])

        choice2 = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))
        clear()

        if choice2 == 1:
            new_sensor = create_light_sensor()
            list_sensors.append(new_sensor)
            clear()
            print("\n" + "< Creation performed correctly >" + " ...")
            time.sleep(2)

        elif choice2 == 2:
            new_sensor = create_co2_sensor()
            list_sensors.append(new_sensor)
            clear()
            print("\n" + "< Creation performed correctly >" + " ...")
            time.sleep(2)

        elif choice2 == 3:
            new_sensor = create_humidity_sensor()
            list_sensors.append(new_sensor)
            clear()
            print("\n" + "< Creation performed correctly >" + " ...")
            time.sleep(2)

        elif choice2 == 4:
            new_sensor = create_infrared_sensor()
            list_sensors.append(new_sensor)
            clear()
            print("\n" + "< Creation performed correctly >" + " ...")
            time.sleep(2)

        elif choice2 == 5:
            new_sensor = create_nfc_sensor()
            list_sensors.append(new_sensor)
            clear()
            print("\n" + "< Creation performed correctly >" + " ...")
            time.sleep(1.5)

        elif choice2 == 0:
            clear()
            break

        else:
            clear()
            print("\n" + "< Invalid option >" + " ...")
            time.sleep(1)


def create_light_sensor():
    """
    Create a new light sensor.
    :return: New sensor object.
    """
    temp = build.Light()
    temp.current_value = float(input("\n" + "< Insert current value >" + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + "< Insert sampling frequency >" + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + "< Insert message frequency >" + "\n\n>>"))
    return temp


def create_co2_sensor():
    """
    Create a new CO2 sensor.
    :return: New sensor object.
    """
    temp = build.CO2()
    temp.current_value = float(input("\n" + "< Insert current value >" + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + "< Insert sampling frequency >" + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + "< Insert message frequency >" + "\n\n>>"))
    return temp


def create_humidity_sensor():
    """
    Create a new humidity sensor.
    :return: New sensor object.
    """
    temp = build.Humidity()
    temp.current_value = float(input("\n" + "< Insert current value >" + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + "< Insert sampling frequency >" + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + "< Insert message frequency >" + "\n\n>>"))
    return temp


def create_infrared_sensor():
    """
    Create a new infrared sensor.
    :return: New sensor object.
    """
    temp = build.Infrared()
    temp.current_value = float(input("\n" + "< Insert current value >" + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + "< Insert sampling frequency >" + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + "< Insert message frequency >" + "\n\n>>"))
    return temp


def create_nfc_sensor():
    """
    Create a new NFC sensor.
    :return: New sensor object.
    """
    temp = build.NFC()
    temp.current_value = float(input("\n" + "< Insert current value >" + "\n\n>>"))
    clear()
    temp.sampling_freq = float(input("\n" + "< Insert sampling frequency >" + "\n\n>>"))
    clear()
    temp.message_freq = float(input("\n" + "< Insert message frequency >" + "\n\n>>"))
    return temp


def load_json():
    """
    Opens a json file and loads all the data.
    Option 1 loads automatically the correct file for the mode in use.
    Option 2 the user must enter the file name.
    """
    menu_load = [
        dict(number_menu=1, label_menu="Load default config"),
        dict(number_menu=2, label_menu="Load saved config"),
        dict(number_menu=0, label_menu="Back"),
    ]

    for line in menu_load:
        print(str(line["number_menu"]) + ". " + line["label_menu"])

    choice = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))
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
                    if sensors.system_name == systems.system_name:
                        systems.environment.append(sensors)
                        # Makes an intelligent copy that keeps both objects linked to the respective changes...
                        # excluding deletion, which disassociates objects:
                        for each_sensor in systems.environment:
                            each_sensor = copy.copy(sensors)

            print("\n" + "< Configuration loaded successfully >" + " ...")
            time.sleep(2)

    if choice == 2:
        nome_file = input("\n" + "< Insert the name of the file without extension >" + "\n\n>>")
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
                    if sensors.system_name == systems.system_name:
                        systems.environment.append(sensors)
                        # Makes an intelligent copy that keeps both objects linked to the respective changes...
                        # excluding deletion, which disassociates objects:
                        for each_sensor in systems.environment:
                            each_sensor = copy.copy(sensors)

            print("\n" + "< Configuration loaded successfully >" + " ...")
            time.sleep(2)

    if choice == 0:
        clear()
        return


def save_json():
    """
    Create a json file and save all data.
    The user must enter the file name.
    """
    try:
        if list_systems == [] and list_sensors == []:
            clear()
            print("\n" + "< There is no data to save >")

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

        file_name = input("\n" + "< Save the config >" + "\n" +
                          "< Insert the name of the file without extension >" + "\n\n>>")
        # Compatibility for Windows:
        if name == 'nt':
            dir_name = os.getcwd() + "\\config\\" + file_name + ".json"

        # Compatibility for Mac and Linux(os.name: "posix"):
        else:
            dir_name = os.getcwd() + "/config/" + file_name + ".json"

        with open(dir_name, "w") as file:
            json.dump(dict(systems=list_temp_systems, sensors=list_temp_sensors), file)
            clear()
            print("\n" + "< Configuration saved successfully >" + " ...")
            time.sleep(2)

    except:
        clear()
        print("\n" + "< Error saving the file >")


def save_in_database():
    """
    Save the config in a database online.
    """
    try:
        print("")
        # User of the database cloud:
        user = input("User Name: ")
        clear()
        print("")
        # Password of the database cloud:
        password = input("Password: ")
        clear()
        clear()
        client = MongoClient("mongodb+srv://" + user + ":" + password +
                             "@db-cloud-a14d2.gcp.mongodb.net/test?retryWrites=true")
        clear()
        db = client["Central_System"]
        db_name = input("\n" + "< Choose the name of the DataBase >" + "\n" +
                        "< If you write a new name a new DataBase will be created >\n\n>>")
        database = db[db_name]

    except:
        clear()
        print("\n" + "< Error: control your internet connection >" + " ...")
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
        print("\n" + "< The information was successfully uploaded to the server >" + " ...")
        time.sleep(2)
        clear()
        input("\n" + "< The ID of the file is: " + str(result.inserted_id) + " >" + "\n\n" +
              "< Press enter to go back >" + "\n\n>>")

    except:
        clear()
        print("\n" + "< Error: can't access to the data base server >" + "\n" +
              "< Control your credentials >" + " ...")
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
        user = input("User Name: ")
        clear()
        print("")
        # Password of the database cloud:
        password = input("Password: ")
        clear()
        clear()
        client = MongoClient("mongodb+srv://" + user + ":" + password +
                             "@db-cloud-a14d2.gcp.mongodb.net/test?retryWrites=true")
        db = client["Central_System"]

    except:
        clear()
        print("\n" + "< Error: control your internet connection >" + " ...")
        time.sleep(2)
        return

    while True:
        clear()
        print("  MENU °°*       " + mode)
        print("")
        menu = [
            dict(number_menu=1, label_menu="Show all the config files in DB"),
            dict(number_menu=2, label_menu="Download config file from DB"),
            dict(number_menu=0, label_menu="Back"),
        ]
        for line in menu:
            print(str(line["number_menu"]) + ". " + line["label_menu"])
        choice = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))

        try:
            if choice == 1:
                """Show all the documents in the database"""
                clear()
                print("\n" + "< Files in the database >")
                for collection_name in db.list_collection_names({}):
                    print("\n")
                    print("-"*60)
                    print("File name: " + collection_name + "\n")
                    for document in db[collection_name].find():
                        pprint.pprint(document)
                input("< Press enter to go back >" + "\n\n>>")
                clear()

            elif choice == 2:
                """Print the name of all the files in the server"""
                clear()
                print("\n" + "< List of all the files in the server >" + "\n")
                for collection_name in db.list_collection_names({}):
                    print(collection_name)

                """Select one DataBase by input and save it in a Json file"""
                db_name = input("\n" + "< Insert the name of a file >" + "\n\n>>")
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
                                print("New file created: "+db_name+".json" + " ...")
                                time.sleep(2)

            elif choice == 0:
                clear()
                break

        except:
            clear()
            print("\n" + "< Error: can't access to the data base server >" + "\n" +
                  "< Control your credentials >" + " ...")
            time.sleep(2)
            break


def program_start():
    """
    --Structure of the Program--
    Recall the functions entered above and interacts
    with System and Sensor classes in the file: "build".
    """
    program_state()  # Notify program start to the file '__main__'
    mode = "Safe Mode"  # Determines the launch mode of the program
    clear()
    while True:
        try:
            clear()
            print("  MENU *°°       "+mode)
            main_menu()
            choice_mp = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))

            if choice_mp == 0:
                """ Shutdown """
                clear()
                print("< Do you want to exit the program? >")
                shutdown = input("\n\n" + "< Write 'y' or 'Y' to confirm, other to cancel >" + "\n\n>>")

                if shutdown == "y" or shutdown == "Y":
                    clear()
                    print("< Preparing system for shutdown >" + " ...")

                    """ Informs that the program is closing 
                        correctly to the 'main' file """
                    main.power(True)
                    time.sleep(1.5)
                    break

                elif shutdown != "y" and shutdown != "Y":
                    continue

            elif choice_mp == 1:
                """
                Menu to interact with the sensors.
                """
                while True:
                    clear()
                    print("  MENU °*°       "+mode)
                    sensor_change_menu()
                    choice_ms = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))

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
                            print("\n" + "< There are no sensors >" + " ...")
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
                            print("\n" + "< There are no sensors >" + " ...")
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
                                        dict(number_menu=1, label_menu="Current value"),
                                        dict(number_menu=2, label_menu="Message frequency"),
                                        dict(number_menu=3, label_menu="Sampling frequency"),
                                        dict(number_menu=0, label_menu="Back"),
                                    ]
                                    print("")

                                    for line in change_menu_sen:
                                        print(str(line["number_menu"]) + " ) " + line["label_menu"])

                                    choice_mod_sen = int(input("\n" + "< Which parameter do you want to change? >" +
                                                               "\n\n>>"))

                                    if choice_mod_sen == 0:
                                        clear()
                                        break

                                    elif choice_mod_sen == 1:
                                        clear()
                                        temp_num = float(input("\n" + "< Enter current value >" + "\n\n>>"))
                                        list_sensors[choosen_sensor].current_value = temp_num

                                    elif choice_mod_sen == 2:
                                        clear()
                                        temp_num = float(input("\n" + "< Enter Sampling frequency >" + "\n\n>>"))
                                        list_sensors[choosen_sensor].message_freq = temp_num

                                    elif choice_mod_sen == 3:
                                        clear()
                                        temp_num = float(input("\n" + "< Enter Message frequency >" + "\n\n>>"))
                                        list_sensors[choosen_sensor].sampling_freq = temp_num

                                    else:
                                        clear()
                                        print("\n" + "< Invalid option >" + " ...")
                                        time.sleep(1)

                    elif choice_ms == 4:
                        """
                        Monitoring sensors.
                        View all the sensors.
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + "< There are no sensors >" + " ...")
                            time.sleep(1)

                        else:
                            clear()
                            for index in range(0, len(list_sensors)):
                                print("\n" + str(index + 1) + " ) " + list_sensors[index].output_view())
                            print("\n" + "< These are all registered sensors >")
                            input("< Press enter to go back >" + "\n\n>>")

                    else:
                        clear()
                        print("\n" + "< Invalid option >" + " ...")
                        time.sleep(1)

            elif choice_mp == 2:
                """
                Menu for interacting with systems.
                """
                while True:
                    clear()
                    print("  MENU °*°       "+mode)
                    system_change_menu()
                    choice_mod_sys = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))

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
                            print("\n" + "< There are no systems >" + " ...")
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
                            print("\n" + "< There are no sensors >" + " ...")
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
                                        print("\n" + "< There are no systems >" + " ...")
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
                                            print("\n" + "< The sensor has been inserted into the system: " +
                                                  list_systems[one_system].system_name + " ...")
                                            time.sleep(2)

                                else:
                                    print("< The sensor is already assigned to a system >" + " ...")
                                    time.sleep(2)

                    elif choice_mod_sys == 4:
                        """
                        Removes sensor from a system.
                        The sensor continues to be in "list_sensors".
                        """
                        clear()
                        if list_sensors == []:
                            print("\n" + "< There are no sensors >" + " ...")
                            time.sleep(1)

                        elif list_systems == []:
                            print("\n" + "< There are no systems >" + " ...")
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
                            print("\n" + "< There are no systems >" + " ...")
                            time.sleep(1)

                        else:
                            clear()
                            for index in range(0, len(list_systems)):
                                print("\n" + str(index + 1) + " ) " + list_systems[index].output_view())
                            print("\n" + "< These are all registered systems >")
                            input("< Press enter to go back >" + "\n\n>>")

                    else:
                        clear()
                        print("\n" + "< Invalid option >" + " ...")
                        time.sleep(1)

            elif choice_mp == 3:
                """
                Save or load configuration menu.
                """
                clear()
                print("  MENU °*°       "+mode)
                menu_config = [
                    dict(number_menu=1, label_menu="Load Configuration"),
                    dict(number_menu=2, label_menu="Save Configuration"),
                    dict(number_menu=3, label_menu="Load from DataBase"),
                    dict(number_menu=4, label_menu="Save  to  DataBase"),
                    dict(number_menu=0, label_menu="Back"),
                ]
                print("")

                for line in menu_config:
                    print(str(line["number_menu"]) + " ) " + line["label_menu"])
                choice_m_conf = int(input("\n" + "< Choose a number from the menu >" + "\n\n>>"))

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
                    print("\n" + "< Invalid option >" + " ...")
                    time.sleep(1)

            else:
                clear()
                print("\n" + "< Invalid option >" + " ...")
                time.sleep(1)

            """ Error handling: """
        except TypeError:
            print("< Error: Type of values entered incorrect >" + " ...")
            time.sleep(1)
            continue

        except ValueError:
            print("< Error: Incorrect values entered >" + " ...")
            time.sleep(1)
            continue

        except FileExistsError:
            print("< Error: The file already exists >" + " ...")
            time.sleep(1)
            continue

        except FileNotFoundError:
            print("< Error: Can't access to the file >" + " ...")
            time.sleep(1)
            continue

        except IOError:
            print("< Error: Input / Output >" + " ...")
            time.sleep(1)
            continue

        except SyntaxError:
            print("< Attention: The script of the program could be compromised, contact responsible >" + " ...")
            time.sleep(4)
            exit(1)

        except:
            print("< Error: Generic >" + " ...")
            time.sleep(1)
            break
