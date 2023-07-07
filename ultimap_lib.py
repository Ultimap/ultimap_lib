import random
import collections

INFINITY = float('inf')


# Элемент связанного списка
class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.next = None


# Связанный список
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    # Добавление в конец списка
    def add(self, value):
        add_item = LinkedListItem(value)
        if self.__head is None:
            self.__head = add_item
            self.__tail = add_item
        else:
            self.__tail.next = add_item
            self.__tail = add_item

    # Удаление
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

    # Вернуть весь список
    def show_all_list(self):
        current_item = self.__head
        new_list = []
        while current_item is not None:
            new_list.append(current_item.value)
            current_item = current_item.next
        return new_list

    # Имеется ли значение в списке
    def search_item(self, value):
        current_item = self.__head
        while current_item is not None:
            if current_item.value == value:
                return True
            current_item = current_item.next
        return False

    # Добавить значение в список по индеску
    def add_in(self, add_value, index_value):
        add_item = LinkedListItem(add_value)
        current_item = self.__head
        index = 0
        while current_item is not None:
            if index == index_value - 1:
                add_item.next = current_item.next
                current_item.next = add_item
                return True
            current_item = current_item.next
            index += 1
        return False


# Бинарный поиск
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


# Поиск наименьшего эллемента в массиве
def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for _ in range(len(list)):
        if list[_] < smallest:
            smallest = list[_]
            smallest_index = _
    return smallest_index


# Сортировка выбором
def selection_sort(list):
    new_list = []
    for _ in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list


# Быстрая сортировка
def fast_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = random.choice(list)
        left = [_ for _ in list if _ < pivot]
        middle = [_ for _ in list if _ == pivot]
        right = [_ for _ in list if _ > pivot]
        return fast_sort(left) + middle + fast_sort(right)


# Поиск в ширину
def search_graph(graph, first_value, search_value):
    processed = []
    search_queue = collections.deque()
    search_queue += graph[first_value]
    while search_queue:
        now_value = search_queue.popleft()
        if now_value not in processed:
            if now_value == search_value:
                return True
            else:
                processed.append(now_value)
                search_queue += graph[now_value]
    return False


# Алгоритм Дейкстры для поиска не отрицательных взвешиных графов
def Dekstra(graph, costs, parents):
    processed = []

    def find_lower_cost_node(costs):
        lower_cost = INFINITY
        lower_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lower_cost and node not in processed:
                lower_cost = cost
                lower_cost_node = node
        return lower_cost_node

    node = find_lower_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lower_cost_node(costs)
    return parents, costs
