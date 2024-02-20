class Fish:
    def __init__(self):
        self.members = ['Pike', 'Tuna', 'Salmon']

    def printMembers(self):
        print("Printing members of Fish class:")
        for member in self.members:
            print('\t%s' % member)

