from heapq import heapify, heappop, heappush

from .node import Node


class HuffmanTree(object):
    def __init__(self):
        self.queue = None
        self.code_table = {}

    def _make_queue(self, freq_table):
        node_list = [Node(item, frequency) for item, frequency in freq_table.items()]
        heapify(node_list)
        return node_list

    def _make_table(self, start, node):
        if node.item:
            if not start:
                self.code_table[node.item] = '0'
            else:
                self.code_table[node.item] = start
        else:
            self._make_table(start+'0', node.left)
            self._make_table(start+'1', node.right)

    def make(self, freq_table):
        priority_queue = self._make_queue(freq_table)
        while len(priority_queue) > 1:
            left = heappop(priority_queue)
            right = heappop(priority_queue)
            new_node = Node(None, right.weight+1)
            new_node.add_children(left, right)
            heappush(priority_queue, new_node)
        self.queue = priority_queue
        return self.queue

    def encode(self):
        self._make_table('', self.queue[0])
        return self.code_table

    def get_compressed_string(self, input_):
        return ''.join([self.code_table[c] for c in input_])
