# NEXRAD_RunRPG
#==-ROC/FRB PYTHON PROGRAM DEFINITION-==========================================
#/home/pmccrone/python/src/runrpg
# NAME:
# :::::::::::::::::::::::::::::::::::::::::::::::
# Py_nexrad_runrpg__v4.py 
# :::::::::::::::::::::::::::::::::::::::::::::::
#  PROGRAM OVERVIEW:
#       (0) The PYTHON CODE reads case information from an FRB google sheet.
#       (1) The information is used to run NEXRAD RPG cases for further post analysis.
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
# Programmer: Mr. Paul McCrone     23 August 2023
# Modification  :  BELOW
#========================================================================================
#  NOTE: THIS PROGRAM ASSUMES THE USE OF Python version 3.8.8+ for RHEL.
#---------------------------------------------------------------
#
#  PYTHON MODULES USED: numpy, scipy, matplotlib, datetime, 
#                       os, sys, math, pandas, warnings, socket, subprocess(commands)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# THIS IS MEANT TO EXPLAIN HOW I GET THE DATA FROM THE FILE:
#
# Note, for our data set the following columns are important:
# I ASSUME THE EXCEL SHEET HAS THESE COLUMNS IN THIS ORDER! 
# Note: In Python, The first column in column Zero (0).
# I leave column zeo for notes.
# Col
# No.  Name: 
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
# If I do not specify a column, I do not use it. 
# We do not care about the contents of columns 0, 2-5, 7-11, 13, etc.
