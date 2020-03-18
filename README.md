# BeanSim

bean bean bean bean bean

bean bean bean bean bean bean bean 

A natural selection simulation of blobs or something. Beans

As of now the program is split into a fairly simple basic structure.

The actual sim code is in "simulation"
As of right now, this code contains organism.py, map.py, and simulation.py

The file organism.py has an Organism (or whatever name you want)
This handles our singular organism that we will begin the sim with.
As it gets more complex, we might have to have to create one or two other files, depending on how we want to differentiate the organisms.

The file map.py contains information about the creation of the map.

The file simulation.py runs how organisms and the map are stored and processes game updates.

The graphics handling portion suprisingly enough is in the folder called "graphics"

The file engine.py in it runs the creation of a pygame window and handling that window.
It does through the use of the state.py file, which describes states, essentially something that encapsulates code so you dont have to know about the window and stuff and prettyness.

The main file patches these two parts together. Ideally, it should be the only file to know that both sides of the equation exist.
It takes the graphics engine from graphics and state definitions, and uses this to display the updates that simulation.py processes.

This program requires (besides standard python packages) pygame and probably numpy.
