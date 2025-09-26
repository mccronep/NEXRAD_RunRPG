#!/bin/bash
#
# zenitylistselect.sh
choice=$(zenity --list --title="Excel Tabs" --column="Tabs from Excel file" "Cool (A) NandC both on or off" "Warm (B) NandC both on or off" "Cool (C) NandC cross on or off" "Warm (D) NandC cross on or off" )
echo $choice
