import numpy as np


class EnveloppeADSR:
    def __init__(self, attackTime=0.001, decayTime=0.005, releaseTime=0.4, sustainAmp=0.8, sampleRate=44100):
        self.attackTime = attackTime
        self.decayTime = self.attackTime + decayTime
        self.releaseTime = releaseTime
        self.sustainAmp = sustainAmp
        self.sampleRate = sampleRate

        self.maxAttackAmp = 1.0


        self.attackSlope = self.getAttackSlope()
        self.decaySlope = self.getDecaySlope()
        self.releaseSlope = 0

        self.lastAmp = 0
        self.notePressed = False
        self.t = 0
        self.releaseBeginTime = 0
        self.releaseEndTime = 0

    def generateEnveloppeAmps(self):
        while True:
            if self.t < self.attackTime and self.notePressed:
                self.lastAmp = self.getAttackValue()
                yield self.lastAmp
            
            if self.t >= self.attackTime and self.t < self.decayTime and self.notePressed:
                self.lastAmp = self.getDecayValue()
                yield self.lastAmp
            
            if self.t >= self.decayTime and self.notePressed:
                self.lastAmp = self.getSustainValue()
                yield self.lastAmp

            if self.t < self.releaseEndTime and not self.notePressed:
                yield self.getReleaseValue()
            
            yield 0
            self.t += 1.0 / self.sampleRate


    def getAttackSlope(self):
        return (self.maxAttackAmp - 0) / (self.attackTime - 0)


    def getDecaySlope(self):
        return (self.sustainAmp - self.maxAttackAmp) / (self.decayTime - self.attackTime)
    

    def getReleaseSlope(self):
        return -(self.lastAmp) / (self.releaseTime)
    

    def getAttackValue(self):
        return self.attackSlope * self.t
    

    def getDecayValue(self):
        return self.maxAttackAmp + (self.decaySlope * (self.t - self.attackTime))
    

    def getSustainValue(self):
        return self.sustainAmp


    def getReleaseValue(self):
        return self.lastAmp + (self.releaseSlope * (self.t - self.releaseBeginTime))
    


    def resetEnveloppe(self):
        self.t = 0
        self.releaseEndTime = 0


    def noteIsPressed(self):
        self.notePressed = True


    def noteIsNotPressed(self):
        self.notePressed = False
        self.releaseEndTime = self.t + self.releaseTime
        self.releaseBeginTime = self.t
        self.releaseSlope = self.getReleaseSlope()


    def releaseEnded(self):
        if self.t >= self.releaseEndTime:
            return True
        return False