# This is a Python framework to compliment "Peek-a-Boo, I Still See You: Why Efficient Traffic Analysis Countermeasures Fail".
# Copyright (C) 2012  Kevin P. Dyer (kpdyer.com)
# See LICENSE for more details.

import random

from Trace import Trace
from Packet import Packet

class PadRFCRand:
    @staticmethod
    def applyCountermeasure(trace):

        newTrace = Trace(trace.getId())
        for packet in trace.getPackets():
            rand = random.choice(range(8,256,8))
            length = min( packet.getLength()+rand, Packet.MTU )
            newPacket = Packet( packet.getDirection(),
                                packet.getTime(),
                                length )
            newTrace.addPacket( newPacket )

        return newTrace