import json

fh = open('I:\\PythonProjects 2020\\5(PyIO)\\notesDB.json', 'r+') 

print(json.dumps(fh.read(), indent=4))
