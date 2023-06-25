class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, value):
        add_item = LinkedListItem(value)
        if self.__head is None:
            self.__head = add_item
            self.__tail = add_item
        else:
            self.__tail.next = add_item
            self.__tail = add_item

    def remove(self, value):
        current_item = self.__head
        past_item = None
        while current_item is not None:
            if current_item.value == value:
                if past_item is None:
                    self.__head = current_item.next
                if current_item.next is None:
                    self.__tail = past_item
                if past_item is not None:
                    past_item.next = current_item.next
                return True
            past_item = current_item
            current_item = current_item.next
        return False

    def show_all_list(self):
        current_item = self.__head
        while current_item is not None:
            print(current_item.value)
            current_item = current_item.next

    def search_item(self, value):
        current_item = self.__head
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False


def binary_search(list, item):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            right = mid - 1
        elif list[mid] < item:
            left = mid + 1
    return None


def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for _ in range(len(list)):
        if list[_] < smallest:
            smallest = list[_]
            smallest_index = _
    return smallest_index


def selection_sort(list):
    new_list = []
    for _ in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list


