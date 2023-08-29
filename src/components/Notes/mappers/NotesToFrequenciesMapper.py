import json


class NotesToFrequenciesMapper:
    def __init__(self):
        pathNotesFrequencies = "./src/components/Notes/NotesFrequencies.json"
        notesFrequenciesJson = open(pathNotesFrequencies)
        self.notesFrequenciesMap = json.load(notesFrequenciesJson)
    

    def getFreqFromNote(self, note):
        return self.notesFrequenciesMap[note]