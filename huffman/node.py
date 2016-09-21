class Node(object):
    def __init__(self, item, weight=0):
        self.left = None
        self.right = None
        self.item = item
        self.weight = weight

    def add_children(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Item: {0}, Weight: {1}>'.format(self.item, self.weight)

    def __lt__(self, cmp_):
        return self.weight < cmp_.weight

    def __le__(self, cmp_):
        return self.weight <= cmp_.weight

    def __eq__(self, cmp_):
        return self.weight == self.cmp_.weight

    def __ne__(self, cmp_):
        return self.weight != self.cmp_.weight

    def __gt__(self, cmp_):
        return self.weight > self.cmp_.weight

    def __ge__(self, cmp_):
        return self.weight >= self.cmp_.weight
