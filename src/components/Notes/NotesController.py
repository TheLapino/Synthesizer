import keyboard
from src.components.notes.mappers.NotesToFrequenciesMapper import NotesToFrequenciesMapper
from src.components.notes.NotesContainer import NotesContainer
from src.components.notes.mappers.KeyboardToNotesMapper import KeyboardToNotesMapper
from src.components.notes.Note import Note

class NotesController():
    def __init__(self, root, octave):

        keyMap = ['z','s','x','d','c','f','v','g','b','h','n','j','m','k',',','l','.',';','é']

        self.NotesFrequenciesMapper = NotesToFrequenciesMapper()
        self.notesContainer = NotesContainer()
        self.NotesMapper = KeyboardToNotesMapper(keyMap, root, octave)
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
            return Note("exit Note", -1)

        if not note:
            return Note("No note", 0)
        
        noteFreq = self.NotesFrequenciesMapper.getFreqFromNote(note)
        return Note(note, noteFreq)

