# PyBox2d testBed template 

A simple example demonstrates how to implement a simulation by utilizing testBed Framework

Version: Box2D-2.0.2b2

## Operation

1) Execute program

    python physicenginesimulator.py

... will demonstrate 10 circles random walk in frictionless world.


## Keep in mind

2) workaround the problem of coordinate conversion b/w screen and world

	ex. Screensize = (640, 480), World will be explained into Worldwidth (-32, 32) and WorldHeight(44, -4)
	
	With the change of groundbody's postion from (0,0) -> (0, -4), the modified Worldsize becomes (-32, 32) and (48, 0)
	
3) CORRECT functions 'ConvertScreenToWorld2' and 'ConvertWorldToScreen2' when the origin of groundbody's postion changes.


##  Need to be done

1) Introduce websocket