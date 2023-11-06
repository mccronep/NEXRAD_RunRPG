#!/home/pmccrone/anaconda3/bin
# -*- coding: utf-8 -*-
#==============================================================
#
#==============================================================
#
#
#
#==-ROC/FRB PYTHON PROGRAM DEFINITION-==========================================
#
#/home/pmccrone/python/src/runrpg
#
# NAME:
# :::::::::::::::::::::::::::::::::::::::::::::::
# Py_nexrad_rpg_runcases_read.py
# :::::::::::::::::::::::::::::::::::::::::::::::
#
#  PROGRAM OVERVIEW:
#       (0) The PYTHON CODE reads case information from an FRB google sheet.
#       (1) The information is used to run NEXRAD RPG cases for further post analysis.
#
#--------------------------------------------------------------------------------------------------
# PARAMETER TABLE:
#--------------------------------------------------------------------------------------------------
#
# I/O           NAME                               TYPE            FUNCTION
#--------------------------------------------------------------------------------------------------
#  I            FRB google sheet address           input           INPUT DATA FROM ROC/FRB
#  O            Formatted table of data            output          case information
#_________________________________________________________________________________________________
#=================================================================================================
#
#=================================================================================================
#-
#
# Programmer: Mr. Paul McCrone     23 August 2023
# Modification  :  BELOW
#========================================================================================
#  Version 1.0   , Dated 2016-Aug-11
#                  Initial Build.
#========================================================================================
#  NOTE: THIS PROGRAM ASSUMES THE USE OF Python version 3.8.8+ for RHEL.
#---------------------------------------------------------------
#
#  PYTHON MODULES USED: numpy, scipy, matplotlib, datetime, 
#                       os, sys, math, warnings, socket, subprocess(commands)
#
#---------------------------------------------------------------#
#---------------------------------------------------------------#
#
try:
    import numpy as NP
    from numpy.random import randn
#
    from matplotlib import use
    use("agg")
#
    import scipy as S
    import matplotlib as MPL
    import pandas as PD
    import datetime
    import os as OS
    import sys as SYS
    import math as MATH
    import warnings as WARNINGS
    import socket
    import subprocess # commands
    import matplotlib.pyplot as plt
    import json

    #import cartopy.crs as ccrs
    #import pyart
    #import matplotlib.pyplot as plt
    #import mpl_toolkits.basemap as bm
    #import plotly as PLY
except:
    print("Error loading modules!")

#
WARNING_INIT_ERROR=1

#
DADASHES='-----------------------------------------------------'
dadash='-----------------------------------------------------'
#
DAEQUALS='==--==--==--==--==--==--==--==--==--==--==--==--==--'
#

current_working_directory='/home/pmccrone/python/src/runrpg'
##current_working_directory=my_RADAR_BASEPATH
#
#
CWD_PATH=current_working_directory+'/'
#
#
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
this_return_value = 0
valid_thispath=OS.path.exists(CWD_PATH)
if valid_thispath:
    print(dadash)
    print("This path is VALID and EXISTS:: "+CWD_PATH)
    this_return_value = 1
    WARNING_INIT_ERROR=1
    print(dadash)
    #
else:
    #
    print("--CAUTION--")
    print("You are requesting the validity of this path: "+CWD_PATH)
    print("-------The indicated path is INVALID! NEED TO CHECK THIS!!!!!!!! -----------------")
    this_return_value = 0
    WARNING_INIT_ERROR=0
    #-----------------------------------------------------------
    # End of if block
    #-----------------------------------------------------------
#
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
program_name="Py_nexrad_rpg_runcases_read.py"
#
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

ALL_call_signs= \
["PGUA","RKSG","RKJK","RODN","KABR","KENX","KABX","KFDR","KAMA","PAHG", \
"KEWX","KBBX","PABC","KBLX","KBGM","KBMX","KBIS","KCBX","KBOX","KBRO", \
"KBUF","KCXX","KFDX","KICX","KCLX","KRLX","KCYS","KLOT","KILN","KCLE", \
"KCAE","KGWX","KCRP","KFWS","KDVN","KFTG","KDMX","KDTX","KDDC","KDOX", \
"KDLH","KDYX","KEYX","KEVX","KEPZ","KLRX","KBHX","PAPD","KFSX","KHPX", \
"KGRK","KPOE","KEOX","KSRX","KIWX","KAPX","KGGW","KGLD","KMVX","KGJX", \
"KGRR","KTFX","KGRB","KGSP","KRMX","KUEX","KHDX","KCBW","KHGX","KHTX", \
"KIND","KJKL","KJAN","KJAX","PHKN","KEAX","KBYX","PAKC","KMRX","KARX", \
"LPLA","KLCH","KESX","KDFX","KILX","KLZK","KVTX","KLVX","KLBB","KMQT", \
"KMXX","KMAX","KMLB","KNQA","KAMX","PAIH","KMAF","KMKX","KMPX","KMBX", \
"KMSX","KMOB","PHMO","KVAX","KMHX","KOHX","KLIX","KOKX","PAEC","KAKQ", \
"KLNX","KTLX","KOAX","KPAH","KPDT","KDIX","KIWA","KPBZ","KSFX","KGYX", \
"KRTX","KPUX","KRAX","KUDX","KRGX","KRIW","KFCX","KJGX","KDAX","KLSX", \
"KMTX","KSJT","KNKX","KMUX","KHNX","TJUA","KSOX","KATX","KSHV","KFSD", \
"PACG","PHKI","PHWA","KOTX","KSGF","KCCX","KLWX","KTLH","KTBW","KTWX", \
"KEMX","KINX","KVNX","KVBX","KICT","KLTX","KFFC","KYUX","KLGX"]
#

#
dict_call_signs={"KABR":"Aberdeen_SD", "KABX":"Albuquerque_NM", "KAKQ":"Norfolk-VA", \
"KAMA":"Amarillo_TX", "KBBX":"Beale-AFB_CA", \
"KAMX":"Miami-FL", "KAPX":"Gaylord_MI", "KARX":"La-Crosse_WI", "KATX":"Seattle-Tacoma_WA", \
"KBGM":"Binghamton_NY", "KBHX":"Eureka_CA", "KBIS":"Bismarck_ND", "KBLX":"Billings_MT", \
"KBMX":"Birmingham_AL", "KCAE":"Columbia_SC", \
"KBOX":"Boston-MA", "KBRO":"Brownsville-TX", "KBUF":"Buffalo_NY", "KBYX":"Key-West-FL", \
"KCBW":"Houlton-Maine", "KCBX":"Boise_ID", "KCCX":"State-College_PA", "KCLE":"Cleveland_OH", \
"KCLX":"Charleston-SC", "KDDC":"Dodge-City_KS", \
"KCRP":"Corpus-Christi-TX", "KCXX":"Burlington_VT", "KCYS":"Cheyenne_WY", "KDAX":"Sacramento_CA", \
"KDFX":"Laughlin-AFB_TX", "KDIX":"Philadelphia-PA", "KDLH":"Duluth_MN", "KDMX":"Des-Moines_IA", \
"KDOX":"Dover-AFB-DE", "KEMX":"Tucson_AZ", \
"KDTX":"Detroit_MI", "KDVN":"Davenport_IA", "KDYX":"Dyess-AFB_TX", "KEAX":"Kansas-City_MO", \
"KENX":"Albany_NY", "KEOX":"Fort-Rucker_AL", "KEPZ":"El-Paso_TX", "KESX":"Las-Vegas_NV", \
"KEVX":"Eglin-AFB-FL", "KFDX":"Cannon-AFB_NM", \
"KEWX":"Austin-San-Antonio_TX", "KEYX":"Edwards-AFB_CA", "KFCX":"Roanoke_VA", "KFDR":"Altus-AFB_OK", \
"KFFC":"Atlanta_GA", "KFSD":"Sioux-Falls_SD", "KFSX":"Flagstaff_AZ","KFTG":"Denver_CO", \
"KFWS":"Dallas-Ft.Worth_TX", "KGRK":"Fort-Hood_TX", \
"KGGW":"Glasgow_MT", "KGJX":"Grand-Junction_Co", "KGLD":"Goodland_KS", "KGRB":"Green-Bay_WI", \
"KGRR":"Grand-Rapids_MI", "KGSP":"Greer_SC", "KGWX":"Columbus-AFB,_ MS", "KGYX":"Portland-Maine", \
"KHDX":"Holloman-AFB_NM", "KHTX":"Huntsville_AL",  \
"KHGX":"Houston-Galveston-TX", "KHNX":"San-Joaquin-Valley_CA", "KHPX":"Fort-Campbell_KY", \
"KICT":"Wichita_KS", "KICX":"Cedar-City_UT", "KILN":"Cincinnati_OH", "KILX":"Lincoln_IL", \
"KIND":"Indianapolis_IN", "KJAX":"Jacksonville-FL", \
"KINX":"Tulsa_OK", "KIWA":"Phoenix_AZ", "KIWX":"Fort-Wayne_IN", "KJAN":"Jackson_MS", \
"KJGX":"Robins-AFB_GA", "KJKL":"Jackson_KY", "KLBB":"Lubbock_TX", "KLCH":"Lake-Charles-LA", \
"KLIX":"New-Orleans-LA", "KLTX":"Wilmington-NC", \
"KLNX":"North-Platte_NE", "KLOT":"Chicago_IL", "KLRX":"Elko_NV", "KLSX":"Saint-Louis_ MO", \
"KLVX":"Louisville_KY", "KLWX":"Sterling-VA", "KLZK":"Little-Rock_AR", "KMAF":"Midland-Odessa_TX", \
"KMAX":"Medford_OR", "KMOB":"Mobile-AL", \
"KMBX":"Minot-AFB_ND", "KMHX":"Morehead-City-NC", "KMKX":"Milwaukee_WI", "KMLB":"Melbourne-FL", \
"KMPX":"Minneapolis-St.Paul_MN", "KMQT":"Marquette_MI", "KMRX":"Knoxville-Tri-Cities_TN", \
"KMSX":"Missoula_MT", "KNKX":"San-Diego-CA", \
"KMTX":"Salt-Lake-City_UT", "KMUX":"San-Francisco_CA", "KMVX":"Grand-Forks_ND", "KMXX":"Maxwell-AFB_AL", \
"KNQA":"Memphis_TN", "KOAX":"Omaha_NE", "KOHX":"Nashville_TN", "KOKX":"New-York-City-NY", \
"KOTX":"Spokane_WA", "KPAH":"Paducah_KY", \
"KPBZ":"Pittsburgh_PA", "KPDT":"Pendleton_OR", "KPOE":"Fort-Polk_LA", "KPUX":"Pueblo_CO", \
"KRAX":"Raleigh-Durham_NC", "KRGX":"Reno-NV", "KSFX":"Pocatello-Idaho-Falls_ID", \
"KRIW":"Riverton_WY", "KRLX":"Charleston_WV", "KRMX":"Griffiss-AFB_NY", "KRTX":"Portland_OR", \
"KSGF":"Springfield_MO", "KSHV":"Shreveport_LA", "KSJT":"San-Angelo_TX", \
"KSOX":"Santa-Ana_Mountains_CA", "KTLX":"Oklahoma-City_OK", \
"KSRX":"Fort-Smith_AR", "KTBW":"Tampa-FL", "KTFX":"Great-Falls_MT", "KTLH":"Tallahassee-FL", \
"KTWX":"Topeka_KS", "KUDX":"Rapid-City_SD", "KUEX":"Hastings_NE", "KVAX":"Moody-AFB_GA", \
"KVBX":"Vandenberg-AFB_CA", "PABC":"Bethel_AK", \
"KVNX":"Vance-AFB_OK", "KVTX":"Los_Angeles_CA", "KYUX":"Yuma_AZ", "LPLA":"Lajes-AB_Azores", \
"PACG":"Sitka_AK", "PAEC":"Nome_AK", "PAHG":"Anchorage_AK", "PAIH":"Middleton-Island_AK",
"PAKC":"King-Salmon_AK", "PHKM":'Kamuela-Kohala-HI', \
"PAPD":"Fairbanks_AK", "PGUA":"Anderson-AFB-Guam", "PHKI":"South-Kauai-HI", \
"PHKN":"Kamuela_HI", "PHMO":"Molokai-HI", "PHWA":"South-Shore-HI", "RKJK":"Kunsan-AB-Korea", \
"RKSG":"Camp-Humphreys-Korea", "RODN":"Kadena_Okinawa", "TJUA":"San-Juan-Puerto-Rico", \
"KLGX":"Langley-Hill_WA"}

#
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#
#sheet_id = “1XqOtPkiE_Q0dfGSoyxrH730RkwrTczcRbDeJJpqRByQ”
#sheet_name = “sample_1”
#url = f”https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
#
#url=f"https://docs.google.com/spreadsheets/d/1hg1rNsRpEIz8CBTPW2q3fhcVfiGm7dOYk-ZRupnBqEQ/edit#gid=1817848148"

file=CWD_PATH+'ISDP_RA_Test_5_PM.xlsx'
#file=CWD_PATH+'ISDP_RA_Test.xlsx'

#file=CWD_PATH+'ISDP_RA_Test_2_PM.xlsx'
#
# Check thisfile
#
valid_thisfile=OS.path.isfile(file)
#
if valid_thisfile:
    print(dadash)
    print("This file is VALID and EXISTS:: "+file)
    this_return_value = 1
    print(dadash)
    WARNING_INIT_ERROR=1
    #
else:
    #
    print("---CAUTION---")
    print("---The indicated file is INVALID! NEED TO CHECK THIS!: "+file)
    this_return_value = 0
    WARNING_INIT_ERROR=0
    #-----------------------------------------------------------
    # End of if block
    #-----------------------------------------------------------

#
this_return_value = 0
#
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
try:
    dataset=PD.read_excel(file, sheet_name="Test ver - Pauls Warm Season 9R")
    print('Read excel file. Successful!')
    # Alternatively, you can specify the sheet indices instead of the sheet names
    #df1 = pd.read_excel("file.xlsx", sheet_name=0)
except:
    print("WARNING--- The file read was not successful\n\n")
    WARNING_INIT_ERROR=0
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


sp='==>'

print (DADASHES)
print("We will print the dataset from the Excel file. Then we will print the first row, then one more.")

#
print(dataset)
##print(dataset.loc[0])
##print(dataset.loc[[0,1]])

#Get a quick overview by printing the first 10 rows of the DataFrame:
print (DADASHES)
print("Printing the first 10 rows -using the head option- of the DataFrame:")
print(dataset.head(10))

# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
print (DADASHES)
print("Printing the last 10 rows -using the tail method- of the Dataset:") 
print(dataset.tail(10))

# Print information about the data:
print (DADASHES)
print("Print info about the data:")
print(dataset.info())

#Return a new Data Frame with no empty cells
#new_df =dataset.dropna()

# If you want to change the original DataFrame, use the inplace = True argument
#dataset.dropna(inplace = True)

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:
#dataset.fillna(130, inplace = True)

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.
# To only replace empty values for one column, specify the column name for the DataFrame
#df["Calories"].fillna(130, inplace = True)

# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450",  and we could just insert "45" in row 7'
#df.loc[7, 'Duration'] = 45

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.
# Delete rows where "Duration" is higher than 120:
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)


# pandas Get Column Names
# You can get the column names from pandas DataFrame using df.columns.values, 
# and pass this to python list() function to get it as list, once you have the data you can print it using print() statement.
print (DADASHES)
print("We will print the column names:")
print(dataset.columns.values)

# You can also use df.columns.values.tolist() to get the DataFrame column names.
colmn_list=dataset.columns.values.tolist()
num_cols=len(colmn_list)

print (DADASHES)
print("This is the last column - This is its name:")
last_col=colmn_list[num_cols-1]
print(colmn_list[num_cols-1])

# Our dataset has 'Max Range for R(A) usage (km)' for the last column. How do we get the entry of this column from the 7th row?
#dataset.loc[7,last_col]

# Note, for our data set the following columns are important:
# I ASSUME THE EXCEL SHEET HAS THESE COLUMNS IN THIS ORDER! 
#
#  1 - 'Radar Site'
#  6 - 'File Location Level-II Data (Linux)'
# 12 - 'File Location  Level-III Products (Linux)'
# 14 - 'Est. ISDP pulled from ASP log, use with "show_isdp" command.'
# 29 - 'Max Range for R(A) usage (km)'
# 30 - 'Job Number' - This is the job number for scripts.
# 31 - 'Execute?'   - This tells the program if the scripts
#                     should actually be built. If 'no', the
#                     script won't be built, and will not run.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# We do not care about the contents of columns 0, 2-5, 7-11, 13, etc.
#

col_radar_site=colmn_list[1]
col_levelII=colmn_list[6]
col_level3=colmn_list[12]
col_ISDP=colmn_list[14]
col_maxrange=colmn_list[29]
#
col_Job_number=colmn_list[30]
col_execute=colmn_list[31]


# Print all the level II directories
print (DADASHES)
print("These are the level II directories:")
for x in dataset.index:
    print(dataset.loc[x,col_levelII])

# Print all the level 3 directories
print (DADASHES)
print("These are the level 3 directories:")
# Print all the level 3 directories
for x in dataset.index:
    print(dataset.loc[x,col_level3])

# Print all the Radar stations:
print (DADASHES)
print("These are the Radar stations")
for x in dataset.index:
    print(dataset.loc[x,col_radar_site])

#Print all the Estimated ISDP values
print (DADASHES)
print("These are the estimated ISDP vals:")
for x in dataset.index:
    print(dataset.loc[x,col_ISDP])

#Print the max range for each row:
print (DADASHES)
print("These are the maximum range values:")
for x in dataset.index:
    print(dataset.loc[x,col_maxrange])

#Print the job number for each row:
print (DADASHES)
print("These are the Job number:")
for x in dataset.index:
    print(dataset.loc[x,col_Job_number])

#Print the execute for each row:
print (DADASHES)
print("These are the execution setting values for each row:")
for x in dataset.index:
    print(dataset.loc[x,col_execute])



#
# Get example of data from row 5:
#

rowx=5

row5_radarsite = dataset.loc[rowx,col_radar_site]

row5_levelII   = dataset.loc[rowx,col_levelII]

row5_level3    = dataset.loc[rowx,col_level3]

row5_ISDP      = dataset.loc[rowx,col_ISDP]

row5_max_range = dataset.loc[rowx,col_maxrange]
#
row5_Job_number = dataset.loc[rowx,col_Job_number]

row5_execute = dataset.loc[rowx,col_execute]

print('row5_radarsite= '+str(row5_radarsite))
print('row5_levelII  = '+str(row5_levelII))
print('row5_level3   = '+str(row5_level3))
print('row5_ISDP     = '+str(row5_ISDP))
print('row5_max_range= '+str(row5_max_range))  
#
print('row5_Job_number   = '+str(row5_Job_number))
print('row5_execute   = '+str(row5_execute))
##
## Contruct KSH to run mrpg.
#

print(DADASHES)
print(DADASHES)
print(DADASHES)
print("Example of playback instructions from row 5\n")
print("mrpg cleanup\n")
print("cad "+row5_radarsite.lower()+" 1\n")
print("mrpg -p startup\n")
print("show_isdp -i "+str(row5_ISDP)+"\n")
print("hci &\n")

DADOTS=". . . . . . . . . . . . . . ."

#Print all  the command sequences for all the playbacks

for x in dataset.index:
    print(DADASHES)
    print(DADASHES)
    print(DADASHES)
   #rowx=x
    rowx_radarsite = dataset.loc[   x,col_radar_site]
    rowx_levelII   = dataset.loc[   x,col_levelII]
    rowx_level3    = dataset.loc[   x,col_level3]
    rowx_ISDP      = dataset.loc[   x,col_ISDP]
    rowx_max_range = dataset.loc[   x,col_maxrange]
    #
    rox_Job_number = dataset.loc[   x,col_Job_number]
    #     
    rwx_Job_number= str(int(rox_Job_number)) 
    #
    rowx_Job_number=str(rwx_Job_number)

    if rox_Job_number < 100:
        rowx_Job_number="0"+rwx_Job_number
    if rox_Job_number < 10:
        rowx_Job_number="00"+rwx_Job_number    

     
    rowx_execute    = dataset.loc[   x,col_execute]
    #
    print("Screen 3:  playback instructions from row "+str(x))
    print("Will we execute? Setting:"+str(rowx_execute)+"\n")
    print("Job Number: "+str(rowx_Job_number)+"\n\n")
    print("mrpg cleanup\n")
    print("cad "+rowx_radarsite.lower()+" 1\n")
    print("mrpg -p startup\n")
    ## The [:2] is to remove the decimal from the ISDP.
    rowx_ISDP2 = str(rowx_ISDP)[:2]
    print("show_isdp -i "+str(rowx_ISDP2)+"\n")
    print("hci &\n")
    print("\n\n")
    #
    print(DADOTS+" 2")
    print("Screen 2:  Playback instructions from row "+str(x))
    print("ecl 1 "+str(rowx_level3))
    #
    print("\n")
    print(DADOTS+" 0")
    print("Screen 0:  Playback instructions from row "+str(x))
    print("cd "+str(rowx_levelII))
    print("play_a2 -i\n")
    print("\n")
    #
    print(DADOTS+" 4")
    print("Screen 4:  Playback instructions from row "+str(x))
    print("script lem_capture.txt\n")
    print("capture\n")
    #End loop







print(dadash)
#print("-------Program END EXECUTION - {} -----------------").format(program_name)                                        
print("-------Program END EXECUTION - "+str(program_name)+" -----------------")
print(dadash)

#-------------------------------------------------------------------------------
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--
##--## END OF PYTHON CODE       





