import keyboard
from src.components.notes.NotesFrequenciesMapper import NotesFrequenciesMapper
from src.components.NotesContainer import NotesContainer
from src.components.notes.NotesOctaveMapper import NotesOctaveMapper

class NotesController():
    def __init__(self, root, octave):

        keyMap = ['z','s','x','d','c','f','v','g','b','h','n','j','m','k',',','l','.',';','é']

        self.NotesFrequenciesMapper = NotesFrequenciesMapper()
        self.notesContainer = NotesContainer()
        self.NotesMapper = NotesOctaveMapper(keyMap, root, octave)
        self.keysNotes = self.NotesMapper.getNotesMapper()

        self.NotesMapper.showNotesMapper()

    def poll(self):
        noteFreq = 0
        for i in self.keysNotes.keys():
            note = self.keysNotes[i]
            
            if keyboard.is_pressed(i):
                self.notesContainer.addNote(note)
            else:
                self.notesContainer.removeNote(note)

        note = self.notesContainer.getNote()

        if note == "":
            return -1, ""

        if not note:
            return 0, ""
        noteFreq = self.NotesFrequenciesMapper.getFreqFromNote(note)
        return noteFreq, note

