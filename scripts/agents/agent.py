# -*- coding: utf-8 -*-

# ####################################################################
#  Copyright (C) 2005-2013 by the FIFE team
#  http://www.fifengine.net
#  This file is part of FIFE.
#
#  FIFE is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
# ####################################################################

from fife import fife
from scripts.common.common import ProgrammingError

class Agent(fife.InstanceActionListener):
    def __init__(self, unitName, nameSpace, world):
        fife.InstanceActionListener.__init__(self)
        # self.settings = settings
        # self.model = model
        self.agentName = None
        self.unitName = unitName
        self.nameSpace = nameSpace
        # self.layer = layer
        self.world = world
        self.agent = None


        # if uniqInMap:
        #     self.agent = layer.getInstance(agentName)
        #     if not self.agent:
        #         # We have to create a new this instance.
        #         object = model.getObject("boy", "http://www.fifengine.net/xml/rio_de_hola")
        #         point = fife.Point3D(0,0,0)
        #         self.agent = layer.createInstance(object, point)


    def createInstance(self, location):
        '''
        Creates the instance of the object on the map.
        :param location: Location where the instance will be.
        :return:
        '''
        #FIXME: Fix this namespace.
        self.nameSpace = "http://www.fifengine.net/xml/rio_de_hola"
        object = self.world.model.getObject(self.unitName, self.nameSpace)
        if not object:
            print "Error! No ", self.unitName ,"found in the object library"
        point = location.getLayerCoordinates()
        self.agent = self.world.scene.agentLayer.createInstance(object, point)
        self.agent.setCellStackPosition(0)

        if self.unitName:
            fifeID = self.agent.getFifeId()
            self.agentName = self.unitName + ":" + str(fifeID)

            self.agent.setId(self.agentName)
            print self.agent.getId()

        self.agent.addActionListener(self)



    def selectInstance(self, instanceName):
        '''
        Looks for an instance with the same name in the map and associates it with this agent.
        :param instanceName: Name of the instance in the loaded map on the "activeLayer"
        :return: bool, true if it could be loaded.
        '''
        layer = self.world.scene.agentLayer
        self.agent = layer.getInstance(instanceName)
        object = self.agent.getObject()

        if self.agent:
            self.agentName = instanceName
            self.agent.addActionListener(self)
            return True
        else:
            return False



    def onInstanceActionFinished(self, instance, action):
        raise ProgrammingError('No OnActionFinished defined for Agent')

    def onInstanceActionCancelled(self, instance, action):
        raise ProgrammingError('No OnActionFinished defined for Agent')

    def onInstanceActionFrame(self, instance, action, frame):
        raise ProgrammingError('No OnActionFrame defined for Agent')

    def start(self):
        raise ProgrammingError('No start defined for Agent')

    # def resetAP(self):
    #     pass
