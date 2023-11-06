Procedures for Python program RUNRPG

Information:

This information is provided as background. My hope is that you will not need to run this.

All python programs use pmccrone’s python (anaconda) resources. 

cd /home/pmccrone/anaconda3/bin

The python binary is:
/home/pmccrone/anaconda3/bin/python 

This is python 3.8. Do not use an earlier version (No earlier than 3.6.8).

The source code is located in:
/home/pmccrone/python/src/runrpg

There is a backup copy in:
/import/frb_archive/pmccrone/Scripts/runrpg

Instructions:

To run the runrpg source code, perform these commands.

For the Warm, season:
/home/pmccrone/anaconda3/bin/python  /home/pmccrone/python/src/runrpg/Py_nexrad_runrpg__v4.py
For the Cool, season:
/home/pmccrone/anaconda3/bin/python  /home/pmccrone/python/src/runrpg/Py_nexrad_runrpg__v5.py

Watch the output for errors. Make necessary changes if needed.

These python programs process the excel worksheets (below) and make the “case scripts” needed to run the rpg.

The Warm season output “case scripts” will be found in:
/import/frb_archive/pmccrone/Scripts/runrpg/ksh_scripts2023A/
The Cool season “case scripts” will be in:
/import/frb_archive/pmccrone/Scripts/runrpg/ksh_scripts2023B/

To run the “case scripts”, see procedures V14 (A and B).

This code processes an Excel file:
/home/pmccrone/python/src/runrpg/F-Shield-Testing-Cases.xlsx

This Excel file is an excel version of the following Google sheet file:
https://docs.google.com/spreadsheets/d/1v1e_QkvO13eX0Z5oQ7JTWchpqyfT0767auj8baQsihY/edit#gid=141543009

IF THIS GOOGLE Sheet changes, then my work is invalid. You will need to rerun the runrpg program.  

Specifically, if any of the contents of the following columns, or the order in which they appear in the Google sheet change. DO NOT CHANGE THE ORDER THAT COLUMNS APPEAR. You can change the contents of the cells:

Column B - 	Radar site
Column G - 	Level II Directory.
Column M - 	Level III Directory.
Column O - 	ISDP
Column AD - 	Max Range (only needs a number)
Column AE - 	Job Number
Column AF - 	Execute?

I read column “B” in Column “B”. I assume it doesn’t change. So, do not make the second column become the third column. You can add as many columns as you want after the “AF” column. The contents can change, and the runrpg program will run.  If the order of the columns change, I do not check for this and the program will crash. I will make an error checking section for this. 

I do have error checking in the runrpg program. I check for:
Radar site: I make sure the four letter identifier is a valid NEXRAD site.
Level II directory: It must exist. I do not check to see if there is data in it.
Level III Directory: It must exist. If it doesn’t, I will try to make it. I report if I can make it. I then try to make it writeable. If it doesn’t make it writable, it states an error.
There is an “execute” setting in column “AF”. If this is set to ‘yes’ (only ‘yes’), the “case script” will be made. If it is set to anything other than ‘yes’, it will not be made. This allows you to choose some to be made, and exclude the ones you don’t want. 
If there are any errors, the “case script” will not be made. 


BEFORE RERUNNING THE RUNRPG (Note: the below is specific for F-Shield Testing): 
Make sure all changes to “F-Shield Testing Cases” in Google sheets are complete.
MAKE NO CHANGES TO THE LOCATIONS OF COLUMNS OR NAMES OF TABS.
Delete all case scripts in:
/import/frb_archive/pmccrone/Scripts/runrpg/ksh_scripts2023A/
/import/frb_archive/pmccrone/Scripts/runrpg/ksh_scripts2023B/
Download the Google sheet to Linux as:
/home/pmccrone/python/src/runrpg/F-Shield-Testing-Cases.xlsx
To run the runrpg source code, perform these commands.
For the Warm, season:
/home/pmccrone/anaconda3/bin/python  /home/pmccrone/python/src/runrpg/Py_nexrad_runrpg__v4.py
For the Cool, season:
/home/pmccrone/anaconda3/bin/python  /home/pmccrone/python/src/runrpg/Py_nexrad_runrpg__v5.py

Watch the output for errors. Make necessary changes if needed.



My cell is: 
831-224-2701
paul@mccrones.com 
