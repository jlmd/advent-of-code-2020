class Compass:
    position = [0] * 2
    orientations_degrees = {"N": 0, "E": 90, "S": 180, "W": 270, }
    degrees_orientations = {v: k for k, v in orientations_degrees.items()}

    def __init__(self, initial_direction):
        self.orientation = self.orientations_degrees[initial_direction]

    def move(self, direction, value):
        if direction == "N":
            self.position[1] += value
        elif direction == "E":
            self.position[0] += value
        elif direction == "S":
            self.position[1] -= value
        elif direction == "W":
            self.position[0] -= value
        elif direction == "L":
            new_orientation = self.orientation - value
            self.orientation = new_orientation if self.orientation - value >= 0 else 360 + self.orientation - value
        elif direction == "R":
            self.orientation = (self.orientation + value) % 360
        elif direction == "F":
            self.move(self.degrees_orientations[self.orientation], value)

    def get_manhattan_distance(self):
        return abs(self.position[0]) + abs(self.position[1])


if __name__ == '__main__':
    compass = Compass("E")
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            compass.move(line[:1], int(line[1:]))
            line = f.readline()

    print(compass.get_manhattan_distance())
