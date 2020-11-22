import os
import json
from pathlib import Path
from autoflow.defaults import defaultDirectory, defaultTextEditor

#selects slash type depending on OS
slash = ''
if os.name == 'posix':
    slash = '/'
else:
    slash = '\\'

#defines name of the global config folder
configFolderName = '.autoflow'
#defines name of the config file
configFileName = 'af-config.json'

#path for home directory
home = str(Path.home())
#path for .autoflow folder
configFolder = home + slash + configFolderName
#filepath for af-config
configFilePath = configFolder + slash + configFileName

#creates a dict for default data
defaultData = {
    'defaultDirectory': defaultDirectory,
    'defaultTextEditor': defaultTextEditor
}

#contains the default directory of projects
projectsDir = ''

#checks if autoflow config folder exists
isDir = os.path.isdir(configFolder)

#creates a folder if it doesn't
if not isDir:
    os.mkdir(configFolder)

#checks if af-config exists
isFile = os.path.isfile(configFilePath)

#creates and adds default data if doesn't
if not isFile:
    with open(configFilePath,"w") as file:
        data = json.dumps(defaultData,sort_keys=True,indent=4)
        file.write(data)
        file.close()
        
#opens af-config file to get global data
with open(configFilePath) as file:
    data = json.load(file)
    projectsDir = data['defaultDirectory']
    file.close()