from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution | NoSolution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        if grid.objective_test(root.state):
            return Solution(root)
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)
        
        if frontier.is_empty():
            return NoSolution()
        
        while not frontier.is_empty():
            nodo1 = frontier.remove() 
        
            for acciones in grid.actions(nodo1.state):
                NuevoEstado = grid.result(nodo1.state,acciones)
                if NuevoEstado not in reached:
                    nodo2 = Node("",state=NuevoEstado,cost=nodo1.cost + grid.individual_cost(nodo1.state,acciones),parent=nodo1,action=acciones)
                    if grid.objective_test(NuevoEstado):
                        return Solution(nodo2,reached)
                    reached[nodo2.state] = True
                    frontier.add(nodo2)

        return NoSolution(reached)
