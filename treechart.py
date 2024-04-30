class EmployeeNode:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class OrganizationChart:
    def __init__(self):
        self.root = None

    def insert(self, id, name):
        if self.root is None:
            self.root = EmployeeNode(id, name)
        else:
            self._insert(self.root, id, name)

    def _insert(self, node, id, name):
        if id < node.id:
            if node.left:
                self._insert(node.left, id, name)
            else:
                node.left = EmployeeNode(id, name)
        else:
            if node.right:
                self._insert(node.right, id, name)
            else:
                node.right = EmployeeNode(id, name)

    def search(self, id):
        return self._search(self.root, id)

    def _search(self, node, id):
        if node is None:
            return None
        elif node.id == id:
            return node
        elif id < node.id:
            return self._search(node.left, id)
        else:
            return self._search(node.right, id)

    def delete(self, id):
        self.root = self._delete(self.root, id)

    def _delete(self, node, id):
        if node is None:
            return node
        if id < node.id:
            node.left = self._delete(node.left, id)
        elif id > node.id:
            node.right = self._delete(node.right, id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._min_value_node(node.right)
                node.id = successor.id
                node.name = successor.name
                node.right = self._delete(node.right, successor.id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_chart(self):
        self._print_chart(self.root, 0)

    def _print_chart(self, node, depth):
        if node:
            self._print_chart(node.right, depth + 1)
            print(' ' * depth + '|-- ', node.id, node.name)
            self._print_chart(node.left, depth + 1)



org_chart = OrganizationChart()

# Insert employees
org_chart.insert(1, 'John')
org_chart.insert(2, 'Alice')
#org_chart.insert(3, 'Bob')
org_chart.insert(4, 'Charlie')
org_chart.insert(5, 'Eva')

# Print the organization chart
org_chart.print_chart()

# Search for an employee
employee = org_chart.search(3)
if employee:
    print(f"Found employee: {employee.id}, {employee.name}")
else:
    print("Employee not found")

# Delete an employee
org_chart.delete(2)

# Print the updated organization chart
org_chart.print_chart()        