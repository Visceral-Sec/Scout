#!/bin/bash
scoutConfig=""
pathVar="/"
workingDir=$(pwd)
help() # Displays Information about input commands
{
   # Display Help
   echo "SCOUT HELP."
   echo
   echo "Syntax: ./scout [-f] <scoutConfig>" 
   echo "options:"
   echo "-F  Input scoutConfig file, path can also be given else default is working directory 
   "
}

#Start of the Script 
while getopts hu:f:n: option; do
	case $option in
	h)
		help
		exit
		;;
	f)
		scoutConfig=${OPTARG}
		;;
		esac
	done
python3 ${workingDir}/scout.py -f scoutConfig


