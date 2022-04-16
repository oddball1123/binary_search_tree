class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if not current_node.left_child:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if not current_node.right_child:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            print(f"{value} already in Tree, not inserting")

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)
        else:
            print("Tree has no nodes")

    def _print_tree(self, current_node):
        if current_node:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

    def height(self):
        if not self.root:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, current_node, curr_height):
        if not current_node:
            return curr_height

        left_height = self._height(current_node.left_child, curr_height + 1)
        right_height = self._height(current_node.right_child, curr_height + 1)
        # print(f"left height: {left_height}")
        # print(f"right height: {right_height}")
        return max(left_height, right_height)

    def search(self, value):
        if self.root:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, current_node, value):
        if current_node and current_node.value == value:
            return True
        elif current_node.value < value and current_node.right_child:
            return self._search(current_node.right_child, value)
        elif current_node.value > value and current_node.left_child:
            return self._search(current_node.left_child, value)
        return False


# helper method to fill the tree
def fill_tree(tree, num_elems=15, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


# helper method to pretty print the binary tree
def pretty_print_tree(root, val="value", left="left_child", right="right_child"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


# =======================================================
# Randomly fill the tree
# =======================================================
def random_tree():
    tree = BinarySearchTree()
    tree = fill_tree(tree)
    tree.print_tree()
    pretty_print_tree(tree.root)
    print(f"Height of tree is {tree.height()}")


# =======================================================
# Fill the tree with specific values to implement search
# =======================================================
def search_tree():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(79)
    tree.insert(1)
    tree.insert(15)
    tree.insert(23)
    tree.insert(-6)
    tree.insert(93)
    tree.insert(16)
    pretty_print_tree(tree.root)

    for i in [16,69]:
        if tree.search(i):
            print(f"{i} found in tree")
        else:
            print(f"{i} not in tree")


# =======================================================
# Call random or search methods
# =======================================================
# search_tree()
random_tree()
