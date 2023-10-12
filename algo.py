from heapq import heappush, heappop
from typing import Generic, TypeVar

from initialize_data import initialize_data

T = TypeVar('T')

airports, routes = initialize_data()

class Airport:
    def __init__(self, port, parent, cost, heuristic):
        self.port = port
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


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
    frontier = PriorityQueue()
    frontier.push(Airport(initial, None, 0.0, heuristic(initial)))
    explored = set(initial)

    while not frontier.empty:
        current_port = frontier.pop()
        port_id = current_port.port

        if goal_test(port_id):
            return current_port

        for child in successors(port_id):
            if not (airports['IATA'] == child).any():
                continue
            new_cost = current_port.cost + cost(port_id, child)
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Airport(child, current_port, new_cost, heuristic(child)))

    return None


def airport_to_path(port):
    path = [port.port]
    while port.parent is not None:
        port = port.parent
        path.append(port.port)
    path.reverse()
    return path
