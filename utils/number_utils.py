class _Sequence:
    __indexes_dict = None
    __index_begin = 0
    __max_queue = 0
    __active = False

    def __init__(self):
        self.__indexes_dict = {}

    def is_active(self):
        return self.__active

    def activate(self, index_begin):
        if not self.__active:
            self.__active = True
            self.__index_begin = index_begin

    def deactivate(self, index_end):
        if self.__active:
            self.__active = False
            diff = index_end - self.__index_begin
            if diff > self.__max_queue:
                self.__max_queue = diff
                self.__indexes_dict.clear()
                self.__indexes_dict[self.__index_begin] = index_end
            elif diff == self.__max_queue:
                self.__indexes_dict[self.__index_begin] = index_end

    def get_indexes_dict(self):
        return self.__indexes_dict


class NumberTracking:
    __numbers_list = None
    __inc_seq = None
    __des_seq = None

    __max = None
    __min = None
    __sum = 0

    def __init__(self):
        self.__numbers_list = []
        self.__inc_seq = _Sequence()
        self.__des_seq = _Sequence()

    def add(self, value):
        number = int(value)

        self.__min_max_average(number)
        self.__sequence(number)
        self.__numbers_list.append(number)

    def __min_max_average(self, number):
        if self.__max is None:
            self.__max = number
        elif self.__max < number:
            self.__max = number

        if self.__min is None:
            self.__min = number
        elif self.__min > number:
            self.__min = number

        self.__sum += number

    def __sequence(self, number):
        if self.get_count() == 0:
            return
        elif number > self.__get_last_number():
            if not self.__inc_seq.is_active():
                self.__inc_seq.activate(self.get_count() - 1)
                self.__des_seq.deactivate(self.get_count() - 1)
        elif number < self.__get_last_number():
            if not self.__des_seq.is_active():
                self.__des_seq.activate(self.get_count() - 1)
                self.__inc_seq.deactivate(self.get_count() - 1)
        else:
            self.__deactivate_all_sequences()

    def __deactivate_all_sequences(self):
        if self.__inc_seq.is_active():
            self.__inc_seq.deactivate(self.get_count() - 1)
        if self.__des_seq.is_active():
            self.__des_seq.deactivate(self.get_count() - 1)

    def get_count(self):
        return len(self.__numbers_list)

    def __get_last_number(self):
        return self.__numbers_list[self.get_count() - 1]

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

    def get_median(self):
        sorted_list = sorted(self.__numbers_list)
        if self.get_count() % 2 == 0:
            index_median1 = int(self.get_count() / 2)
            index_median2 = index_median1 - 1
            median = (sorted_list[index_median1] + sorted_list[index_median2]) / 2
            return median
        else:
            index_median = int(self.get_count() / 2)
            return sorted_list[index_median]

    def get_average(self):
        return self.__sum / self.get_count()

    def print_inc_sequences(self):
        self.__deactivate_all_sequences()
        idxes_dict = self.__inc_seq.get_indexes_dict()
        list_keys = sorted(list(idxes_dict.keys()))
        for idx_begin in list_keys:
            idx_end = idxes_dict[idx_begin]
            selection = self.__numbers_list[idx_begin:idx_end + 1]
            print("Ascending sequence:\n"
                  "    index_start: {0}, \n"
                  "    index_end: {1} \n"
                  "    list of elements: {2} \n"
                  .format(idx_begin, idx_end, selection)
                  )

    def print_des_sequences(self):
        self.__deactivate_all_sequences()
        idxes_dict = self.__des_seq.get_indexes_dict()
        list_keys = sorted(list(idxes_dict.keys()))
        for idx_begin in list_keys:
            idx_end = idxes_dict[idx_begin]
            selection = self.__numbers_list[idx_begin:idx_end + 1]
            print("Descending sequence:\n"
                  "    index_start: {0}, \n"
                  "    index_end: {1} \n"
                  "    list of elements: {2} \n"
                  .format(idx_begin, idx_end, selection)
                  )
