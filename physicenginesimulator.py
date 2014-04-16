#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# C++ version Copyright (c) 2006-2007 Erin Catto http://www.gphysics.com
# Python version Copyright (c) 2008 kne / sirkne at gmail dot com
# 
# Implemented using the pybox2d SWIG interface for Box2D (pybox2d.googlecode.com)
# 
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

from test_main import *

import threading

class PhysicEngineSimulator (Framework):
    name="PhysicEngineSimulator"
    num_of_bodies = 10
    bodies=[]
    _pickle_vars=['bodies']

    end_lock = threading.Event()

    def __init__(self):
        super(PhysicEngineSimulator, self).__init__()

        self.world.SetGravity((0.0, 0.0))


        ### borders
        bd=box2d.b2BodyDef()
        bd.position = (0, -4)
        ground = self.world.CreateBody(bd) 

	sd=box2d.b2PolygonDef() 
        sd.density = 0.0
        sd.restitution = 1.0
	sd.friction = 0.0

	#void SetAsBox(float32 hx, float32 hy, const b2Vec2& center, float32 angle);
	sdgroups = [ self.ConvertScreenToWorld2(x,y) for x,y in  ( (self.screenSize.x*0.5, 0), 
								   (self.screenSize.x*0.5, self.screenSize.y), 
								   (0, self.screenSize.y*0.5), 
								   (self.screenSize.x, self.screenSize.y*0.5) ) ]
	print sdgroups

	print [ self.ConvertWorldToScreen2(p) for p in sdgroups ]



        sd.SetAsBox( 30,0.5, sdgroups[0], 0.0)
        ground.CreateShape(sd)

        sd.SetAsBox( 30,0.5, sdgroups[1], 0.0)
        ground.CreateShape(sd)

        sd.SetAsBox( 0.5,22, sdgroups[2], 0.0)
        ground.CreateShape(sd)

        sd.SetAsBox( 0.5,22, sdgroups[3], 0.0)
        ground.CreateShape(sd)


        ### circle (Master)
        sd = box2d.b2CircleDef()  # shape def
        sd.radius = 1.0
        sd.density = 0.2
	sd.friction = 0.0
        sd.restitution = 1.0

	"""
        bd = box2d.b2BodyDef()    # body def
        bd.position = ( self.ConvertScreenToWorld2( self.screenSize.x*0.75, self.screenSize.y*0.25) )
        cbd = self.world.CreateBody(bd)
	cbd.SetLinearVelocity( (-25,-25)  )
        cbd.CreateShape(sd)
        cbd.SetMassFromShapes()
	"""

        for i in range(self.num_of_bodies):
            x = box2d.b2Random(-32, 32)
	    y = box2d.b2Random(-4, 44)
            bd=box2d.b2BodyDef()
            bd.position = (x + 5.0,  y + 1.05 + 2.5 * i)
            cbd = self.world.CreateBody(bd)
	    cbd.SetLinearVelocity( (box2d.b2Random(-20, 20), box2d.b2Random(-20, 20))  )
            cbd.CreateShape(sd)
            cbd.SetMassFromShapes()
	    self.bodies.append(cbd)

	"""
        ### rods
        sd=box2d.b2PolygonDef() 
        sd.SetAsBox(3,0.4)
        sd.density = 2.0
        for i in range(self.num_of_bodies):
            bd = box2d.b2BodyDef()
            bd.fixedRotation = True
            p = ( box2d.b2Random(-1*self.half_space+5, self.half_space-5), 
                        box2d.b2Random(5, 2*self.half_space-5) )
            bd.position = p

            rbd = self.world.CreateBody(bd)
            rbd.CreateShape(sd)
            rbd.SetMassFromShapes()
            self.bodies.append(rbd)

        self.is_entered = False
	"""	

    def CheckKeys(self):
        super(PhysicEngineSimulator, self).CheckKeys()


    def Step(self, settings):
        super(PhysicEngineSimulator, self).Step(settings)

	bd_posdata = [ (i, self.ConvertWorldToScreen2(self.bodies[i].position) ) for i in range(self.num_of_bodies) ]




    def Keyboard(self, key):
        pass


if __name__=="__main__":
     main(PhysicEngineSimulator)
