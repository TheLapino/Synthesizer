class NotesOctaveMapper:
    def __init__(self, keyMap, root="B", octave=4):

        self.notesTemplate = ["C","C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.notesMap = {}
        self.keyMap = keyMap
        self.root = root
        self.octave = octave

        self._configureNotesMapper()



    def _configureNotesMapper(self):
        startingIdx = self.notesTemplate.index(self.root)
        lastNote = f"{self.root}{self.octave}"


        for i in range(len(self.keyMap)):
            
            note = self.notesTemplate[startingIdx % len(self.notesTemplate)] + f"{self.octave}"

            if lastNote == f"E{self.octave}" or lastNote == f"B{self.octave}":
                lastNote = ""
                continue
            
            if note[0] == "C" and len(note) == 2 and i != 0:
                self.octave += 1
                note = self.notesTemplate[startingIdx % len(self.notesTemplate)] + f"{self.octave}"
            
            self.notesMap[self.keyMap[i]] = note

            startingIdx += 1
            lastNote = note


    def getNotesMapper(self):
        return self.notesMap
    

    def showNotesMapper(self):
        for k in self.notesMap.keys():
            print(f"{k}: {self.notesMap[k]}")

