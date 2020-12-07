def dfs(bag, bags, expected_color):
    if bag.color == expected_color:
        return 1
    else:
        for containing_bag in bag.containing_bags:
            if dfs(bags[containing_bag.color], bags, expected_color) == 1:
                return 1
    return 0


class Bag:
    containing_bags = []

    def __init__(self, color):
        self.color = color


if __name__ == '__main__':
    bags = {}
    with open('input.txt', 'r') as f:
        line = f.readline()
        while line:
            line_split = line.split()
            containing_bags = []
            bag_color = line_split[0] + " " + line_split[1]
            for i in range(4, len(line_split), 4):
                containing_bag_color = line_split[i + 1] + " " + line_split[i + 2]
                if containing_bag_color != "other bags.":
                    containing_bags.append(Bag(containing_bag_color))
            bag = Bag(bag_color)
            bag.containing_bags = containing_bags
            bags[bag_color] = bag
            line = f.readline()

    count = 0
    color_to_found = "shiny gold"
    for bag_key in bags:
        if bag_key != color_to_found:
            count += dfs(bags[bag_key], bags, "shiny gold")
    print(count)
