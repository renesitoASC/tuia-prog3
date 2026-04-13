from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root,root.cost)
        
        if frontier.is_empty():
            return NoSolution()
        
        while not frontier.is_empty():
            nodo = frontier.pop()
            
            if grid.objective_test(nodo.state):
                return Solution(nodo,reached)
            
            for acciones in grid.actions(nodo.state):
                nuevoEstado = grid.result(nodo.state,acciones)
                nuevoCosto = nodo.cost + grid.individual_cost(nodo.state,acciones)
                
                if nuevoEstado not in reached or nuevoCosto < reached[nuevoEstado]:
                    nodo2 = Node('',nuevoEstado,nuevoCosto,nodo,acciones)
                    reached[nuevoEstado] = nuevoCosto
                    frontier.add(nodo2,nuevoCosto)

        return NoSolution(reached)
