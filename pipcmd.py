import subprocess
import os
import sys
import webbrowser


# made by cayrr.s on discord ^_^
# this is for ppl that are so fucking bad at using a computer they cant handle typing an actual command
# this does get built into an exe using pyinstaller


def pythoncheck():
     for cmd in ['python', 'python3']: # runs both python command versions
          try:
            subprocess.run(['python', '--version']) # runs a command to check the python version
            return True # returns true if no errors
          except: # it aint installed
               print("you dont even have python installed what the fuck bro") 
               webbrowser.open("www.python.org") # opens python.org
               print("this REQUIRES python. why are u using this without it anyway")
               input("press enter to exit ") 




def packageinstall(package):
    command = subprocess.run(['pip', 'install', package], capture_output=True, text=True) # runs the pip install command
    if command.returncode != 0: # if it didnt succeed 
        print(command.stderr)
        print("pip failed")
        rerun()
    else:
         print(f"{package} has successfully installed")
         rerun() # prompts the user to rerun the script
       


def rerun():
     runagain = input("run again? ")
     if runagain == "y": # if the user inputed 'y'
            os.system('cls') # clears console
            os.execv(sys.executable, ['python'] + sys.argv) # reruns the whole fucking script
     else:
          exit() # kills the script
    

def pipupdater():
     result = subprocess.run(['python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'], capture_output=True) # runs a pip update
     output = str(result.stdout) # saves output of the update
     if "Requirement already satisfied:" in output: # gets if pip is alr updated
          print("already up to date")
          return True # continue script
     elif result.returncode != 0: # if it did not succeed
          print("update failed")
          input("press enter to exit ")
     else:
          print("up to date")
          return True # continue script
          
print("pip package dumbass installer")
print("checking if python is even installed")
pythoninstalled = pythoncheck() # runs the python check
if pythoninstalled == True: # gets if it succeeded
     print("python is installed")
     print("\n\n") # 2 new lines (looks better)
print("checking if pip needs an update...")
uptodate = pipupdater() # runs the updater
if uptodate == True: # gets if it returned True (no need for a False handler since i never return False lmao)
    print("\n\n") # 2 new lines
    package = input("pip package: ")
    print(f"installing package: {package}")
    packageinstall(package) # runs the install package function


