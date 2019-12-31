#!/bin/bash


# Check if the program is already open and close the duplicated precess.
sudo kill $(ps aux | grep __main__.py | awk '{print $2}'); clear

# Notes: ccrypt is a program to encrypt files.
# Check if the ccrypt program is installed and propose to install it.
if [ "$(which ccrypt)" = "" ]; then
    echo "< You must install ccrypt to run this program >"
    sudo apt install ccrypt


# Once installed it ask for the password and decrypts the program.
else
    clear
    read -s -p "< Enter the program password > : " pass; clear
    for file in scripts/*.cpt; do ccdecrypt -K $pass "$file"; done
    ccdecrypt __main__.py -K $pass; clear
fi


# Run the default program.
# Encrypt with the same password used in the startup and delete it.
if [ $# -lt 1 ]; then
    python3 __main__.py;
    for file in scripts/*.py; do ccencrypt -K $pass "$file"; done
    ccencrypt __main__.py -K $pass; unset -v pass;
    exit
fi


# Start the program in the mode selected by the user.
a=$1
if [ a != "" ]; then
    python3 __main__.py $a
fi


# Encrypt with the same password used in the startup and delete it.
for file in scripts/*.py; do ccencrypt -K $pass "$file"; done
ccencrypt __main__.py -K $pass; unset -v pass
exit

