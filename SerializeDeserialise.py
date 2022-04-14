class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class SerDesr:
     def serialize(self, root):
         serialised_data = []

         def preorder(node):
             if not node:
                 serialised_data.append('N')
                 return
             serialised_data.append(str(node.data))
             preorder(node.left)
             preorder(node.right)

         preorder(root)

         ','.join(serialised_data)
         return serialised_data


     def deserialize(self, serialized):
         data = serialized.split(',')
         self.i = 0

         def preorder_inverted():
             if data[self.i] == 'N':
                 self.i += 1
                 return None
             node = Tree(int(data[self.i]))
             node.left = preorder_inverted()
             node.right = preorder_inverted()

             return node

         return preorder_inverted()



