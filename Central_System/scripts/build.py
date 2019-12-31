# -*- coding: utf-8 -*-
"""
todo: Documentation

    -*- Function: Class Management of Systems and Sensors -*-

    Project name: Central System
    File name: build

    Date created: 20/03/2019
    Date last modified: 31/12/2019
    Status: Stable

    Python version: 3.8
    Modules required: random, string
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


import random
import string


""" Language Tools """
global Lang
Lang = {
    "System name: ": "System name: ",
    "Local: ": "Local: ",
    "None": "None",
    "Kind sensor: ": "Kind sensor: ",
    "Current value: ": "Current value: ",
    "Battery status: ": "Battery status: ",
    "Sampling frequency: ": "Sampling frequency: ",
    "Message frequency: ": "Message frequency: ",
    "Light": "Light",
    "CO2": "CO2",
    "Humidity": "Humidity",
    "Infrared": "Infrared",
    "NFC": "NFC"
}


def lang_build(lang):
    """ Function to send to this file the
    dictionary from 'skeleton' file """
    global Lang
    Lang = lang


class System:
    """ Class of embedded systems
    (each of its objects can contain sensors) """
    def __init__(self):
        self.system_name = ""
        self.local = ""
        self.environment = []

    def output_view(self):
        """ Function to transform object into string and visualize it """
        return Lang["System name: "] + str(self.system_name) +\
               "\n" + Lang["Local: "] + str(self.local)

    def to_dict(self, sys_name):
        """
        Function to transform a complex object into a dictionary
        :param sys_name: Name of the system to locate the sensors well
        :return: A dictionary of dictionaries
        """
        sys = dict(system_name=self.system_name, local=self.local, environment=[])
        for elem in self.environment:
            if elem.system_name == sys_name:
                sys["environment"].append(elem.__dict__)
        return sys


class Sensor:
    """ Class of sensors
    the ID helps to identify the same sensor in
    both lists (list_sensors and list_systems)"""
    def __init__(self, kind=Lang["None"], current_value=Lang["None"], battery_status=True,
                 sampling_freq=Lang["None"], message_freq=Lang["None"], system_name=Lang["None"]):
        self.kind = kind
        self.current_value = current_value
        self.battery_status = battery_status
        self.sampling_freq = sampling_freq
        self.message_freq = message_freq
        self.system_name = system_name
        self.serial_number = self.serial_generator()

    def output_view(self):
        """ Function to transform object into string and visualize it """
        return Lang["Kind sensor: "] + str(self.kind) + \
               "\n" + Lang["Current value: "] + str(self.current_value) + \
               "\n" + Lang["Battery status: "] + str(self.battery_status) + \
               "\n" + Lang["Sampling frequency: "] + str(self.sampling_freq) + \
               "\n" + Lang["Message frequency: "] + str(self.message_freq) + \
               "\n" + Lang["System name: "] + str(self.system_name)

    def to_dict(self):
        """
        Function to transform an object into a dictionary
        :return: A Dictionary
        """
        return dict(kind=self.kind, current_value=self.current_value, battery_status=self.battery_status,
                    sampling_freq=self.sampling_freq, message_freq=self.message_freq, system_name=self.system_name)

    def serial_generator(self, size=64, chars=string.ascii_uppercase+string.ascii_lowercase + string.digits):
        """
        Coding the serial key
        :param size: Size of the key characters
        :param chars: Dictionary
        :return: _
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def get_serial(self):
        """
        Provides serial sensor key
        :return: ID
        """
        return self.serial_number


class Light(Sensor):
    """ Class Light """
    def __init__(self):
        super().__init__()
        self.kind = Lang["Light"]


class CO2(Sensor):
    """ Class CO2 """
    def __init__(self):
        super().__init__()
        self.kind = Lang["CO2"]


class Humidity(Sensor):
    """ Class Humidity """
    def __init__(self):
        super().__init__()
        self.kind = Lang["Humidity"]


class Infrared(Sensor):
    """ Class Infrared """
    def __init__(self):
        super().__init__()
        self.kind = Lang["Infrared"]


class NFC(Sensor):
    """ Class NFC """
    def __init__(self):
        super().__init__()
        self.kind = Lang["NFC"]
