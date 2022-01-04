from collections import deque


class Lee:

    def __init__(self, board, starting_circles, directions, predicate):
        self.board = board
        self.starting_circles = starting_circles
        self.directions = directions
        self.predicate = predicate
        self.visited = dict()

    def __is_valid_position(self, position):
        return position in self.board.keys()

    def run(self):
        circles_queue = deque()
        for starting_circle in self.starting_circles:
            circles_queue.append(starting_circle)
            self.visited[starting_circle.position] = starting_circle

        while len(circles_queue):
            extracted_circle = circles_queue.popleft()
            for direction in self.directions:
                determined_position = extracted_circle.position[0] \
                                      + direction[0], \
                                      extracted_circle.position[1] \
                                      + direction[1]
                neighbour_position = determined_position
                if self.__is_valid_position(neighbour_position):
                    neighbour = self.board[neighbour_position]
                    if self.predicate(neighbour, self.visited, extracted_circle):
                        self.visited[neighbour_position] = neighbour
                        circles_queue.append(neighbour)
