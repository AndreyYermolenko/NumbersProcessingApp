import time

from utils.number_utils import NumberTracking

nt = NumberTracking()

f = open('data/10m.txt', 'r')
count_of_numbers = 10_000_000

i = 0
start_time = time.time()
print("File processing...")
for number in f:
    nt.add(number)

    if i % (count_of_numbers / 10) == 0:
        print(str(i * 100 / count_of_numbers) + "%")
    i += 1

print("Getting result...")
print("List length: " + str(nt.get_count()))
print("Min number: " + str(nt.get_min()))
print("Max number: " + str(nt.get_max()))
print("Median: " + str(nt.get_median()))
print("Average number: " + str(nt.get_average()))
print("Ascending sequence:\n"
      "    index_start: %s, \n"
      "    index_end: %s \n"
      "    list of elements: %s" %
      nt.get_inc_sequence())
print("Descending sequence:\n"
      "    index_start: %s, \n"
      "    index_end: %s \n"
      "    list of elements: %s" %
      nt.get_des_sequence())
print("--- %s seconds ---" % (time.time() - start_time))
