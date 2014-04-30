'''
@author: Eric
'''

import random

from org.ggp.base.util.statemachine import MachineState
from org.ggp.base.util.statemachine.implementation.prover import ProverStateMachine
from org.ggp.base.player.gamer.statemachine import StateMachineGamer

class EricDummyBot(StateMachineGamer):

    def getName(self):
        return "EricDummyBot"
        
    def stateMachineMetaGame(self, timeout):
        pass

    def stateMachineSelectMove(self, timeout):
        moves = self.getStateMachine().getLegalMoves(self.getCurrentState(), self.getRole())

        print moves

        selection = random.choice(moves)

        return selection
        
    def stateMachineStop(self):
        pass
        
    def stateMachineAbort(self):
        pass        
        
    def getInitialStateMachine(self):
        return ProverStateMachine()