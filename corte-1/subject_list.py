from subject_node import SubjectNode

class SubjectList:
    def __init__(self):
        self.head = None

    def add_subject(self, subject):
        new_node = SubjectNode(subject)
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
            yield current.subject
            current = current.next
