#!/bin/bash

selected_directory=$(zenity  --file-selection --directory --width=475 --height=550 --title="Select the specific directory to make the KSH files." --filename="/import/frb_archive/pmccrone/Scripts/runrpg/")

# Check if a directory was selected (user didn't click Cancel
if [ -n "$selected_directory" ]; then
        echo $selected_directory
        #echo "You selected: $selected_directory"
	CORRAL=($selected_directory)
else
	echo "No directory selected"
fi

