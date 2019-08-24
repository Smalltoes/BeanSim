#describes states
#states are essentially part of the game that allows the programmer to modularly add on to a program
#they will help if we want to possibly have stuff like multiple views, multiple maps, or whatever
#more importantly for us, they allow us to define a set of behaviors the engine expects, and still have it kept mostly away from the core

class State:
    #this init function does normal init stuff
    #make sure when creating inherited classes that this function is called
    #through super().__init__()
    def __init__(self, displaysurf, data, switchStatefunction):
        self.displaysurf = displaysurf
        self.data = data
        self.switchStatefunction = switchStatefunction

    #this function handles the code updating stuff, that everything is updated at the same time
    def update(self):
        pass
    #this function actually does screen drawing, calling pygame commands and stuff
    def render(self):
        pass
    #this function processes any events that come through, and probably most likely contains the information related to changing states
    def processEvent(self, event):
        pass

    #this function is just used to close anything needed if the state is changing. For our purposes this might mean saving the current state or something
    def close(self):
        pass
    
#is that it?
#yeah, it essentially just a guideline to ensure that other states have the functions through inheritance
#whenever you want to create a new state just create a class like this (and import this file)
#class MyState (State):