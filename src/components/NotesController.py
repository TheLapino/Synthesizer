import keyboard
from components.notes.NotesFrequenciesMapper import NotesFrequenciesMapper
from components.NotesContainer import NotesContainer
from components.notes.NotesOctaveMapper import NotesOctaveMapper

class NotesController():
    def __init__(self, root, octave):

        keyMap = ['z','s','x','d','c','f','v','g','b','h','n','j','m','k',',','l','.',';','é']
        self.NotesFrequenciesMapper = NotesFrequenciesMapper()
        self.notesContainer = NotesContainer()
        self.NotesMapper = NotesOctaveMapper(keyMap, root, octave)
        self.keysNotes = self.NotesMapper.getNotesMapper()


    def poll(self):
        noteFreq = 0
        for i in self.keysNotes.keys():
            note = self.keysNotes[i]
            #noteFreq = self.NotesFrequenciesMapper.getFreqFromNote(note)
            
            if keyboard.is_pressed(i):
                self.notesContainer.addNote(note)
            else:
                self.notesContainer.removeNote(note)

        note = self.notesContainer.getNote()

        if not note:
            return 0, ""
        noteFreq = self.NotesFrequenciesMapper.getFreqFromNote(note)
        return noteFreq, note

