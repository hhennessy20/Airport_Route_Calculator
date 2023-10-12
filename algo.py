from heapq import heappush, heappop


class Airport:
    def __init__(self, port, parent, cost, heuristic):
        self.port = port
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


class PriorityQueue:
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
    explored = {initial: 0.0}

    while not frontier.empty:
        current_port = frontier.pop()
        port_id = current_port.port

        if goal_test(port_id):
            return port_id

        for child in successors(port_id):
            new_cost = current_port.cost + cost(port_id, child)

            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Airport(child, current_port, new_cost,
                                      heuristic(child)))
    return None


# Unused atm
def airport_to_path(port):
    path = [port.routes]
    while port.parent is not None:
        port = port.parent
        path.append(port.routes)
    path.reverse()
    return path
