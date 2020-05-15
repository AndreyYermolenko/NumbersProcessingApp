class _Sequence:
    __index_begin = 0
    __index_end = 0
    __count_start = 0
    __max_queue = 0
    __active = False

    def is_active(self):
        return self.__active

    def activate(self, count_start):
        if not self.__active:
            self.__active = True
            self.__count_start = count_start

    def deactivate(self, count_finish):
        if self.__active:
            self.__active = False
            diff = count_finish - self.__count_start
            if diff > self.__max_queue:
                self.__max_queue = diff
                self.__index_begin = self.__count_start
                self.__index_end = count_finish

    def get_index_begin(self):
        return self.__index_begin

    def get_index_end(self):
        return self.__index_end


class NumberTracking:
    __numbers_list = []
    __inc_seq = _Sequence()
    __des_seq = _Sequence()

    __max = None
    __min = None
    __sum = 0

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
            if self.__inc_seq.is_active():
                self.__inc_seq.deactivate(self.get_count() - 1)
            if self.__des_seq.is_active():
                self.__des_seq.deactivate(self.get_count() - 1)

    def get_max(self):
        return self.__max

    def get_min(self):
        return self.__min

    def get_average(self):
        return self.__sum / self.get_count()

    def get_count(self):
        return len(self.__numbers_list)

    def get_inc_sequence(self):
        index_begin = self.__inc_seq.get_index_begin()
        index_end = self.__inc_seq.get_index_end()
        selection = self.__numbers_list[index_begin:index_end + 1]
        return index_begin, index_end, selection

    def get_des_sequence(self):
        index_begin = self.__des_seq.get_index_begin()
        index_end = self.__des_seq.get_index_end()
        selection = self.__numbers_list[index_begin:index_end + 1]
        return index_begin, index_end, selection

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

    def __get_last_number(self):
        if self.get_count() > 0:
            return self.__numbers_list[self.get_count() - 1]
