class Parent():

    def __init__(self, name):
        self.name = name
        self.children = []

    class Inner(object):
        pass

    def Child(self, name):
        parent = self
        class Child(Parent.Inner):
            def __init__(self, name):
                self.name = name
                self.parent = parent
                parent.children.append(self)
        return Child(name)

parent = Parent('Bar')

child1 = parent.Child('Foo')
child2 = parent.Child('World')

print(
    # Getting its first childs name
    child1.name, # From itself
    parent.children[0].name, # From its parent
    # Also works with the second child
    child2.name,
    parent.children[1].name,
    # Go nuts if you want
    child2.parent.children[0].name,
    child1.parent.children[1].name
)

print(
    # Getting the parents name
    parent.name, # From itself
    child1.parent.name, # From its children
    child2.parent.name,
    # Go nuts again if you want
    parent.children[0].parent.name,
    parent.children[1].parent.name,
    # Or insane
    child2.parent.children[0].parent.children[1].parent.name,
    child1.parent.children[1].parent.children[0].parent.name
)


# Second parent? No problem
parent2 = Parent('John')
child3 = parent2.Child('Doe')
child4 = parent2.Child('Appleseed')

print(
    child3.name, parent2.children[0].name,
    child4.name, parent2.children[1].name,
    parent2.name # ....
)