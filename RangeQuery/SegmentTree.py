'''
For range min, max, sum
1. Build: O(N)
2. Query: O(logN) 
3. Insert/Update: O(logN)
'''

class SegmentTree:
    def __init__(self, data, fn):
        self.nodes = [None] * 4 * len(data) #node: (value, left_node_index, right_node_index)
        self.data = data
        self.fn = fn # min, max, sum
        self._build_tree(0, 0, len(data)-1)

    def _left(self, index):
        return (index + 1) * 2 - 1

    def _right(self, index):
        return (index + 1) * 2

    def _build_tree(self, node_index, left_data_index, right_data_index):
        value = None
        if left_data_index == right_data_index:
            value = self.data[left_data_index]
        else:
            left_node_index = self._left(node_index)
            right_node_index = self._right(node_index)

            mid_data_index = (left_data_index + right_data_index) // 2
            value = self.fn([
                self._build_tree(left_node_index, left_data_index, mid_data_index),
                self._build_tree(right_node_index, mid_data_index + 1, right_data_index)
            ])
        self.nodes[node_index] = value
        return value

    def _query(self, node_index, left_query_index, right_query_index, left_data_index, right_data_index):
        value = self.nodes[node_index]
        mid_data_index = (left_data_index + right_data_index) // 2

        if left_query_index == left_data_index and right_query_index == right_data_index:
            return value

        left_node_index = self._left(node_index)
        right_node_index = self._right(node_index)

        if right_query_index <= mid_data_index:
            return self._query(left_node_index, left_query_index, right_query_index, left_data_index, mid_data_index)
        elif left_query_index > mid_data_index:
            return self._query(right_node_index, left_query_index, right_query_index, mid_data_index + 1, right_data_index)
        else:
            return self.fn([
                self._query(left_node_index, left_query_index, mid_data_index, left_data_index, mid_data_index),
                self._query(right_node_index, mid_data_index + 1, right_query_index, mid_data_index + 1, right_data_index)
            ])

    def query(self, left_query_index, right_query_index):
        return self._query(0, left_query_index, right_query_index, 0, len(self.data) - 1)

    def _update(self, node_index, data_index, update_value, left_data_index, right_data_index):
        mid_data_index = (left_data_index + right_data_index) // 2
        left_node_index = self._left(node_index)
        right_node_index = self._right(node_index)

        new_value = None
        if left_data_index == right_data_index:
            new_value = update_value
        elif data_index <= mid_data_index:
            new_value = self.fn([
                self.nodes[right_node_index],
                self._update(left_node_index, data_index, update_value, left_data_index, mid_data_index)
            ])
        else:
            new_value = self.fn([
                self.nodes[left_node_index],
                self._update(right_node_index, data_index, update_value, mid_data_index + 1, right_data_index)
            ])
        self.nodes[node_index] = new_value
        return new_value

    def update(self, data_index, update_value):
        self.data[data_index] = update_value
        return self._update(0, data_index, update_value, 0, len(self.data) - 1)

    def peak(self):
        return self.nodes[0]

    def find(self, data_index):
        return self.data[data_index]

print('====== min ======')
data = [1,2,3,4,5,6,7,8,9,10]
st1 = SegmentTree(data, min)
# st1.pprint()
print(st1.query(3,7)) #4
st1.update(4,1)
print(st1.query(3,7)) #1
st1.update(6,0)
print(st1.query(3,7)) #0

print('====== sum ======')
data = [1,2,3,4,5,6,7,8,9,10]
st2 = SegmentTree(data, sum)
print(st2.query(1,3)) #9 (2+3+4)
print(st2.query(1,4)) #14 (2+3+4+5)
print(st2.query(1,5)) #20 (2+3+4+5+6)
st2.update(2,100)
print(st2.query(1,3)) #106 (2+100+4)
# st2.update(7,80)
print(st2.query(1,4)) #111 (2+100+4+5)
print(st2.query(1,5)) #117 (2+100+4+5+6)
st2.update(7,80)
print(st2.query(2,8)) #211 (100+4+5+6+7+80+9)
