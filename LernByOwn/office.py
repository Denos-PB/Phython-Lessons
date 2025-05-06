class Office:
    def __init__(self, location, size, employees_count, monthly_rent, company):
        self.location = location
        self.size = size
        self.employees_count = employees_count
        self.monthly_rent = monthly_rent
        self.company = company

class Node:
    def __init__(self, office):
        self.office = office
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, office):
        new_node = Node(office)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                raise IndexError("Position out of bounds")
            current = current.next
        current.next = current.next.next

    def destroy_list(self):
        self.head = None

    def display_offices_by_company(self, company_name):
        current = self.head
        while current:
            if current.office.company == company_name:
                print(vars(current.office))
            current = current.next

    def count_offices_with_employees_greater_than(self, n):
        count = 0
        current = self.head
        while current:
            if current.office.employees_count > n:
                count += 1
            current = current.next
        return count

    def display_offices_with_company_starting_with_t(self):
        current = self.head
        while current:
            if current.office.company.startswith("T"):
                print(vars(current.office))
            current = current.next

offices = SinglyLinkedList()


offices.insert_at_position(0, Office("New York", 500, 50, 10000, "TechCorp"))
offices.insert_at_position(1, Office("San Francisco", 300, 30, 8000, "TradeInc"))
offices.insert_at_position(2, Office("Los Angeles", 400, 20, 9000, "TechCorp"))
offices.insert_at_position(3, Office("Chicago", 200, 10, 5000, "TravelCo"))

print("Offices of TechCorp:")
offices.display_offices_by_company("TechCorp")

print("\nNumber of offices with employees > 25:")
print(offices.count_offices_with_employees_greater_than(25))

print("\nOffices with company name starting with 'T':")
offices.display_offices_with_company_starting_with_t()

offices.delete_at_position(1)

offices.destroy_list()