class Student:

    def __init__(self, name, group, marks):
        self.name = name
        self.group = group
        self.marks = marks

    def info(self):
        print('Student name: {}\nStudent group: {}\nStudent marks: {}\n\n'.format(self.name, self.group, self.marks))

    def average_mark(self):
        return (sum(self.marks)/len(self.marks))