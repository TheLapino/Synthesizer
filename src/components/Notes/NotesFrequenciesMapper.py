import json


class NotesFrequenciesMapper:
    def __init__(self):

        notesFrequenciesJson = open("C:/Users/rempl/OneDrive/Documents/Projets Python/Synthesizer/src/components/Notes/NotesFrequencies.json")
        self.notesFrequenciesMap = json.load(notesFrequenciesJson)
    

    def getFreqFromNote(self, note):
        return self.notesFrequenciesMap[note]