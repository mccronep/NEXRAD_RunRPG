#
# Notes on subprocess
#

import subprocess


#
# Popen
#

rs=subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True )

output, errors = rs.communicate()

print(output)

#
# Call example:
#

return_code = subprocess.call(["python", "--version"])

if return_code == 0:

    print("Command executed successfully.")

else
    
    print("Command failed with return code", return_code)

#
# Pipes - the output of ls goes to the input for another 

ls_process = subprocess.Popen(["ls"],stdout=subprocess.PIPE, text=True)

grep_process = subprocess.Popen(["grep","sample"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)

output, error = grep_process.communicate()

print(output)
print(error)

#
# 

result = subprocess.run(["ls"], stdout=subprocess.PIPE)

print(result.stdout.decode())

#
# How do I run a command in the background using subprocess

subprocess.Popen(["ls"], start_new_session=True)

#
# How else can I check the reurn code of a command run using subprocess

result = subprocess.run(["ls"])

if result.returncode == 0:
    print("Command ran successfully")
else:
    print("Command failed with error code", result.returncode)


#on Windows 
# will work on Linux
result = subprocess.run(["ls"], shell=True)

#
subprocess.run(["ls"], shell=True)
#
subprocess.run(["ls -la"], shell=True)
#
subprocess.run(["ls", "-la"])
#
p2 = subprocess.run(["ls", "-la"])   #Still prints to screen
print(p2)
#CompletedProcess(args=['ls', '-la'], returncode=0)
print(p2.args)
#['ls', '-la']  # prints the arguements of the run.
print(p2.returncode)
#0    # 0 means success
print(p2.stdout)
#None    # 
# to capture the output of the command
p2 = subprocess.run(["ls", "-la"], capture_output=True)   #

print(p2.stdout)
# Will print, but needs to be converted to string.
print(p2.stdout.decode())
# Will print like normal

#also
p2 = subprocess.run(["ls", "-la"], capture_output=True, text=True)   #
print(p2.stdout)
#will print normal

#capture_output sets the stdout and stderr to PIPE.
p2 = subprocess.run(["ls", "-la"], stdout=subprocess.PIPE, text=True)   # 


#What about puting the outout to a file
with open('output.txt', 'w') as f:
    p2 = subprocess.run(["ls", "-la"], stdout=f, text=True)
 

#
# I want to see errors. Show error code.
p2 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True)   # 
# This is like doing ls -la dne. As long as dne does not exist, there will be an error, but not in python.
# python will just record the code.
print(p2.returncode)
#2

p2 = subprocess.run(["ls", "-la", "dne"], capture_output=True, text=True, check=True)   # 
#This will make python fail.

 


















