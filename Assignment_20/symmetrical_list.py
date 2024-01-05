number_list = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# number_list = [1, 3, 4, 5, 4, 3, 2, 1]

end_flag = len(number_list)//2 + 1
from_start = 0
from_end = -1

for _ in range(len(number_list)):
     if number_list[from_start] == number_list[from_end]:
          end_flag -= 1
          if end_flag == 0:
               print("list is symmetrical")
               break
     else:
          print("list isn't symmetrical")
          break
     from_start += 1
     from_end -= 1
