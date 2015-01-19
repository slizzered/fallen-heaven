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
    def __init__(self, settings, model, agentName, layer, world, uniqInMap=True):
        fife.InstanceActionListener.__init__(self)
        self.settings = settings
        self.model = model
        self.agentName = agentName
        self.layer = layer
        self.world = world
        if uniqInMap:
            self.agent = layer.getInstance(agentName)
            if not self.agent:
                # We have to create a new this instance.
                object = model.getObject("boy", "http://www.fifengine.net/xml/rio_de_hola")
                point = fife.Point3D(0,0,0)
                self.agent = layer.createInstance(object, point)

            self.agent.addActionListener(self)

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


def create_anonymous_agents(settings, model, objectName, layer, world, agentClass):
    agents = []
    instances = [a for a in layer.getInstances() if a.getObject().getId() == objectName]
    i = 0
    for a in instances:
        agentName = '%s:i:%d' % (objectName, i)
        i += 1
        agent = agentClass(settings, model, agentName, layer, world, False)
        agent.agent = a
        a.addActionListener(agent)
        agents.append(agent)
    return agents