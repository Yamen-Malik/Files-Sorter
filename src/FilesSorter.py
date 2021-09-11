from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, os, shutil, sys
sys.path.append("c:/users/yamen/appdata/local/programs/python/python38-32/lib/site-packages")
from colorama import init, Fore, Back, Style

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        time.sleep(2)
        print (f"{Fore.GREEN}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nGot event for file {event.src_path} \n{Fore.BLUE}Processing... {Fore.RESET}")
        for fileName in os.listdir(folderToTrack):
            print(f"\t{fileName}")
            ProcessFile(folderToTrack + "/" + fileName)
        print(Fore.GREEN +"Done\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + Fore.RESET)

def ProcessFile(filePath):
    fileName, fileExtension = os.path.splitext(filePath)
    fileExtension = fileExtension.replace(".", "")
    for key in extensionsToPathDict:
        if fileExtension in key.split(","):
            MoveFile(filePath, extensionsToPathDict[key])
            return
    print(f"{Fore.YELLOW}\tThere is no folder attached to the file type \".{fileExtension}\" {Fore.RESET}\n")

def MoveFile(filePath, destination):
    try:
        shutil.move(filePath, destination)
        print(f"{Fore.GREEN}\t[32m Moved  \"{os.path.basename(filePath)}\"  to  \"{destination}\"\n {Fore.RESET}")
    except :
        print(Fore.RED +" █████[[ERROR]] an ERROR happned while moving the file to the new destination█████"+ Fore.RESET)

def PrintAnimation(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == " ": continue
        time.sleep(0.05)
def StopApp():
    input(Fore.MAGENTA +"Press Enter to Exit"+ Fore.RESET)
    sys.exit(0)

extensionsToPathDict = {} #Stores the extensions as keys and destination as values (to set the new path for each file)
dataLines = [] #Stores the lines that are in data.txt file
folderToTrack = ""
isLoading = False

init()
#Load data
try:
    dataFile = open("data.txt", "r")
except IOError:
    dataFile = open("data.txt", "w+")
    dataFile.write("<folder to watch>\n<extensions> :: <destination>")
    dataFile.seek(0)
finally:
    dataLines = dataFile.readlines()
    dataFile.close()

pathLine = dataLines[0].strip()
if os.path.exists(pathLine):
    folderToTrack = pathLine
else:
    PrintAnimation(f"{Fore.RED}The folder {pathLine} doesn't exist{Fore.RESET}")
    StopApp()

for line in range(1, len(dataLines)):
    extensions, destination = dataLines[line].split("::")
    destination = destination.strip()
    if not os.path.exists(destination):
        print(f"{Fore.CYAN}The folder {destination} doesn't exist and for that the following line will be ignored: \"{dataLines[line]}\"{Fore.RESET}")
        break
    extensionsToPathDict.update({extensions.replace(" ","").replace(".","") : destination})

observer = Observer()
event_handler = Handler() # create event handler
observer.schedule(event_handler, path = folderToTrack)
observer.start()
PrintAnimation("<=======Ready=======>".center(os.get_terminal_size().columns))

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# sys.stdout.write("\r/")
# sys.stdout.flush()
# time.sleep(0.5)
