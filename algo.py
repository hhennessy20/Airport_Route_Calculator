from heapq import heappush, heappop
from typing import Generic, TypeVar

from initialize_data import initialize_data

T = TypeVar('T')

airports, routes = initialize_data()

class Airport:
    def __init__(self, port, parent, cost, heuristic):
        self.port = port            # Port is IATA ID for Airport instances
        self.parent = parent        # Airport we are coming from
        self.cost = cost            # Cost to get to this airport
        self.heuristic = heuristic  # Dist from goal airport

    # Overloads the less than operator for Priority Queue comparison
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


# Priority Queue to manage airport frontier
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container = []

    @property
    def empty(self):
        return not self._container

    def push(self, port):
        heappush(self._container, port)

    def pop(self):
        return heappop(self._container)

    def __repr__(self):
        return repr(self._container)


def astar(initial, goal_test, successors, heuristic, cost):
    # Establish frontier and explored using initial airport
    frontier = PriorityQueue()
    frontier.push(Airport(initial, None, 0.0, heuristic(initial)))
    explored = set(initial)

    while not frontier.empty:
        # Gets the next airport from queue
        current_port = frontier.pop()
        port_id = current_port.port

        # If we find the goal we're done
        if goal_test(port_id):
            return current_port

        # Loop through a list of all outgoing routes from current airport
        for child in successors(port_id):
            # Check if the child airport exists in dataset
            # Needed due to mismatched data
            if not (airports['IATA'] == child).any():
                continue
            # Update cumulative cost
            new_cost = current_port.cost + cost(port_id, child)
            # If child has already been explored, don't add to frontier
            if child in explored:
                continue
            # Otherwise add child to explored and push to frontier
            explored.add(child)
            frontier.push(Airport(child, current_port, new_cost, heuristic(child)))
    # If we get here a route could not be found
    return None


# Get the total path to airport passed as arg
def airport_to_path(port):
    path = [port.port]
    while port.parent is not None:
        port = port.parent
        path.append(port.port)
    path.reverse()
    return path
