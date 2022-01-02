import os
from FileReadWrite import writeFile as WF
from FileReadWrite import readFile as RF

os.system('cls')

WF('SomeFilePathToWriteTo', 'some test string')
RF('SomeFilePathToWriteTo')

