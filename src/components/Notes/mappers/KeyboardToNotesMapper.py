class KeyboardToNotesMapper:

    def __init__(self, keyMap, root="B", octave=4):
        self.notesTemplate = ["C","C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.notesMap = {}
        self.keyMap = keyMap
        self.root = root
        self.octave = octave

        self.__addExitKey()

        self.__configureNotesMapper()


    def __configureNotesMapper(self):

        noteIdx = self.__getStartingNoteIdx()
        lastNote = self.__getFirstNote()

        for keyIdx in range(len(self.keyMap)):
            
            if self.__lastNoteisBOrE(lastNote):
                lastNote = ""
                continue

            note = self.__assignNoteToKey(keyIdx, noteIdx)

            noteIdx += 1
            lastNote = note


    def __lastNoteisBOrE(self, lastNote):
        if lastNote == f"E{self.octave}" or lastNote == f"B{self.octave}":
            return True
        return False
    
    def __newOctave(self, note):
        if note == f"C{self.octave}":
            return True
        return False
    
    def __getNote(self, noteIdx):
        return self.notesTemplate[noteIdx % len(self.notesTemplate)] + f"{self.octave}"
    
    def __getStartingNoteIdx(self):
        return self.notesTemplate.index(self.root)
    

    def __getFirstNote(self):
        return f"{self.root}{self.octave}"
    

    def __assignNoteToKey(self, keyIdx, noteIdx):
        note = self.__getNote(noteIdx)
        
        if self.__newOctave(note) and keyIdx != 0:
            self.octave += 1
            note = self.__getNote(noteIdx)
        
        self.notesMap[self.keyMap[keyIdx]] = note
        return note

    def getNotesMapper(self):
        return self.notesMap
    

    def showNotesMapper(self):
        for k in self.notesMap.keys():
            print(f"{k}: {self.notesMap[k]}")


    def __addExitKey(self):
        self.notesMap["esc"] = ""

