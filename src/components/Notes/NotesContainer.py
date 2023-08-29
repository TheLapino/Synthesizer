class NotesContainer:
    def __init__(self):
        self.heldNotes = []

    def addNote(self, note):
        if note not in self.heldNotes:
            self.heldNotes.append(note)

    def removeNote(self, note):
        if note in self.heldNotes:
            if note == self.heldNotes[-1]:
                self.heldNotes.remove(note)
                self.heldNotes.sort()
            else:
                self.heldNotes.remove(note)

    def getNote(self):
        if self.isEmpty():
            return 0
        return self.heldNotes[-1]
        
    def isEmpty(self):
        return not len(self.heldNotes)
    
