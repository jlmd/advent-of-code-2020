def dfs(bag, bags, quantity):
    count = 1
    for containing_bag in bag.containing_bags:
        count += dfs(bags[containing_bag.color], bags, containing_bag.quantity)
    return count * quantity


class Bag:
    containing_bags = []

    def __init__(self, color, quantity):
        self.color = color
        self.quantity = quantity


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
                    quantity = line_split[i]
                    containing_bags.append(Bag(containing_bag_color, int(quantity)))
            bag = Bag(bag_color, 1)
            bag.containing_bags = containing_bags
            bags[bag_color] = bag
            line = f.readline()

    print(dfs(bags["shiny gold"], bags, 1) - 1)
