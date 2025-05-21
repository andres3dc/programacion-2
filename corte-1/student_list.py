from student_node import StudentNode

class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student):
        new_node = StudentNode(student)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def iterate(self):
        current = self.head
        while current:
            yield current.student
            current = current.next

    def count_by_stratum(self, stratum):
        count = 0
        for student in self.iterate():
            if student["stratum"] == stratum:
                count += 1
        return count
