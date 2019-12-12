# Sy1_Pt1_UKLineEvaluator
A repository for code drafted together on the subject of power flow modelling in national networks using pandapower.

The first batch of programs pertain to a sample network linked to france, whilst the second is in relation to the UKs power network.

The line evaluator has been drafted, so that in addition to running powerflow models for simulated networks, they may also be strength tested. Weak links in the network may be ascertained by finding which cables are the most prone to failure in the event of extra high loads.

I have just uploaded a number of folders, each of them contains a different part of my work on this project.
The intial work began in the plotting_design folder, where basic networks were plotted using a variety of different methods, including built in pandapower functions and mapbox type methods.

The work then moved onto the french network (french_system) and how to iterate through it, removing lines individually and checking what changes this made to the system at each iteration. This was where the bulk of the code was developed.

The parameters of the task changed, and so I moved to the english grid system (english_system), which has a much smaller network, which lead to less time running the iteration program (it could take up to and hour and a half to run 2000 iterations of the french network)... The english network is where the project culminates, and SANDBOX.ipynb is the file of interest, as it has the finalised program in it and plots a rough heat map of the various lines of the worst case scenario.

And thats about all..
