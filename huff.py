from huffman import FreqTable, HuffmanTree


if __name__ == '__main__':
    ft = FreqTable()
    table = ft.get_table_for_file('text.txt')
    huffman_tree = HuffmanTree()
    priority_queue = huffman_tree.make(table)
    code_table = huffman_tree.encode()
    compressed_string = huffman_tree.get_compressed_string(ft.data)
