from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)
        
        if frontier.is_empty():
            return NoSolution()
        
        while not frontier.is_empty():
            nodo = frontier.remove()
            
            if nodo.state in expanded:
                continue
            expanded[nodo.state] = True
            
            for acciones in grid.actions(nodo.state):
                NuevoEstado = grid.result(nodo.state,acciones)
                
                if NuevoEstado not in expanded:
                    nodo2 = Node('',NuevoEstado,nodo.cost + grid.individual_cost(nodo.state,acciones),nodo,acciones)
                    if grid.objective_test(nodo2.state):
                        return Solution(nodo2,expanded)
                    frontier.add(nodo2)
            

        return NoSolution(expanded)
