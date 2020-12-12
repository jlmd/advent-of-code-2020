class Compass:
    waypoint_position = [10, 1]
    position = [0, 0]

    def move(self, direction, value):
        if direction == "N":
            self.waypoint_position[1] += value
        elif direction == "E":
            self.waypoint_position[0] += value
        elif direction == "S":
            self.waypoint_position[1] -= value
        elif direction == "W":
            self.waypoint_position[0] -= value
        elif direction == "L":
            for i in range(0, int(value / 90)):
                temp = self.waypoint_position[0]
                self.waypoint_position[0] = -(self.waypoint_position[1])
                self.waypoint_position[1] = temp
        elif direction == "R":
            for i in range(0, int(value / 90)):
                temp = self.waypoint_position[0]
                self.waypoint_position[0] = self.waypoint_position[1]
                self.waypoint_position[1] = -temp
        elif direction == "F":
            self.position[0] += value * self.waypoint_position[0]
            self.position[1] += value * self.waypoint_position[1]

    def get_manhattan_distance(self):
        return abs(self.position[0]) + abs(self.position[1])


if __name__ == '__main__':
    compass = Compass()
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            compass.move(line[:1], int(line[1:]))
            line = f.readline()

    print(compass.get_manhattan_distance())
