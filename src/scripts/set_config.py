import os
import sys

import configparser

airflow_home = os.getenv("AIRFLOW_HOME")

if airflow_home is None:
    print("[] environment variable AIRFLOW_HOME not set. Please set it.")
    exit(-1)

config_file = f"{airflow_home}/airflow.cfg"

config = configparser.ConfigParser()
config.read(config_file)

try:
    section_name, variable_name, variable_value = sys.argv[1:4]
except ValueError:
    print(f"[] Usage : {sys.argv[0]} <section> <name> <value>")
    exit(-1)

if section_name not in config.sections():
    print(f"[] the section {section_name} is not in {config_file}.")
    exit(-1)

config.set(section_name, variable_name, variable_value)

with open(config_file, 'w') as configfile:
    config.write(configfile)

print(f"[] variable {section_name}.{variable_name} set to {variable_value}.")
