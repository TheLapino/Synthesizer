import keyboard
from components.notes.NotesFrequenciesMapper import NotesFrequenciesMapper
from components.NotesContainer import NotesContainer

class NotesController():
    def __init__(self):
        self.NotesFrequenciesMapper = NotesFrequenciesMapper()
        self.notesContainer = NotesContainer()
        self.keysNotes = {
            'z': "C4",
            's': "C#4",
            'x': "D4",
            'd': "D#4",
            'c': "E4",
            'v': "F4",
            'g': "F#4",
            'b': "G4",
            'h': "G#4",
            'n': "A4",
            'j': "A#4",
            'm': "B4",
            ',': "C5"
        }
    def poll(self):
        #todo: ajouter une verif pour voir derniere note joué
        noteFreq = 0
        for i in self.keysNotes.keys():
            note = self.keysNotes[i]
            noteFreq = self.NotesFrequenciesMapper.getFreqFromNote(note)
            
            if keyboard.is_pressed(i):
                self.notesContainer.addNote(noteFreq)
            else:
                self.notesContainer.removeNote(noteFreq)

        return self.notesContainer.getNote()

