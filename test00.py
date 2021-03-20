cases_num = int(input())
result = []

for cases in range(1,cases_num + 1):
  nn = int(input())
  total = {}
  end = []
  num_iteration = 0
  total[nn] = num_iteration


  def two(a, num_iteration):
    del total[a]
    each_i = [int(s) for s in str(a)]
    nn = int(each_i[0] * each_i[1])
    num_iteration += 1
    total[nn] = num_iteration
    if nn == 0:
      end.append(num_iteration)
      total[0] = 0

  def three(a, num_iteration):
    del total[a]
    each_i = [int(s) for s in str(a)]
    nn1 = int(each_i[0] * (10*each_i[1] + each_i[2]))
    nn2 = int((10*each_i[0] + each_i[1]) * each_i[2])
    nn3 = int(each_i[0] * each_i[1] * each_i[2])
    num_iteration += 1
    total[nn1] = num_iteration
    total[nn2] = num_iteration
    total[nn3] = num_iteration
    if nn1 == 0 and nn2 == 0 and nn3 == 0:
      end.append(num_iteration)
      total[0] = 0

  def four(a, num_iteration):
    del total[a]
    each_i = [int(s) for s in str(a)]
    nn1 = each_i[0] * each_i[1] * each_i[2] * each_i[3]
    nn2 = each_i[0] * (100*each_i[1] + 10*each_i[2] + each_i[3])
    nn3 = (10*each_i[0] + each_i[1]) * (10*each_i[2] + each_i[3])
    nn4 = (100*each_i[0] + 10*each_i[1] + each_i[2]) * each_i[3]
    nn5 = each_i[0] * each_i[1] * (10*each_i[2] + each_i[3])
    nn6 = each_i[0] * (10*each_i[1] + each_i[2]) * each_i[3]
    nn7 = (10*each_i[0] + each_i[1]) *each_i[2] * each_i[3]
    num_iteration += 1
    total[nn1] = num_iteration
    total[nn2] = num_iteration
    total[nn3] = num_iteration
    total[nn4] = num_iteration
    total[nn5] = num_iteration
    total[nn6] = num_iteration
    total[nn7] = num_iteration
    if nn1 == 0 and nn2 == 0 and nn3 == 0 and nn4 == 0 and nn5 == 0 and nn6 == 0 and nn7 == 0:
      end.append(num_iteration)
      total[0] = 0

  def five(a, num_iteration):
    del total[a]
    each_i = [int(s) for s in str(a)]
    nn1 = each_i[0] * each_i[1] * each_i[2] * each_i[3] * each_i[4]
    nn2 = each_i[0] * (1000*each_i[1] + 100*each_i[2] + 10*each_i[3] + each_i[4])
    nn3 = (10*each_i[0] + each_i[1]) * (100*each_i[2] + 10*each_i[3] + each_i[4])
    nn4 = (100*each_i[0] + 10*each_i[1] + each_i[2]) * (10*each_i[3] + each_i[4])
    nn5 = (1000*each_i[0] + 100*each_i[1] + 10*each_i[2] + each_i[3]) * each_i[4]
    nn6 = each_i[0] * each_i[1] * (100*each_i[2] + 10*each_i[3] + each_i[4])
    nn7 = each_i[0] * (10*each_i[1] + each_i[2]) * (10*each_i[3] + each_i[4])
    nn8 = each_i[0] * (100*each_i[1] + 10*each_i[2] + each_i[3]) * each_i[4]
    nn9 = (10*each_i[0] + each_i[1]) * each_i[2] * (10*each_i[3] + each_i[4])
    nn10 = (10*each_i[0] + each_i[1]) * (10*each_i[2] + each_i[3]) * each_i[4]
    nn11 = (100*each_i[0] + 10*each_i[1] + each_i[2]) * each_i[3] * each_i[4]
    nn12 = each_i[0] * each_i[1] * each_i[2] * (10*each_i[3] + each_i[4])
    nn13 = each_i[0] * each_i[1] * (10*each_i[2] + each_i[3]) * each_i[4]
    nn14 = each_i[0] * (10*each_i[1] + each_i[2]) * each_i[3] * each_i[4]
    nn15 = (10*each_i[0] + each_i[1]) * each_i[2] * each_i[3] * each_i[4]
    num_iteration += 1
    total[nn1] = num_iteration
    total[nn2] = num_iteration
    total[nn3] = num_iteration
    total[nn4] = num_iteration
    total[nn5] = num_iteration
    total[nn6] = num_iteration
    total[nn7] = num_iteration
    total[nn8] = num_iteration
    total[nn9] = num_iteration
    total[nn10] = num_iteration
    total[nn11] = num_iteration
    total[nn12] = num_iteration
    total[nn13] = num_iteration
    total[nn14] = num_iteration
    total[nn15] = num_iteration
    if nn1 == 0 and nn2 == 0 and nn3 == 0 and nn4 == 0 and nn5 == 0 and nn6 == 0 and nn7 == 0 and nn8 == 0 and nn9 == 0 and nn10 == 0 and nn11 == 0 and nn12 == 0 and nn13 == 0 and nn14 == 0 and nn15 == 0:
      end.append(num_iteration)
      total[0] = 0

  while not str(total.keys()) == "dict_keys([0])":

    for i in list(total.keys()):
      num_digits = len(str(i))
      loop_count = total[i]

      if num_digits == 1:
        end.append(loop_count)
        del total[i]
        total[0] = 0

      elif num_digits == 2:
        two(i, loop_count)

      elif num_digits == 3:
        three(i, loop_count)

      elif num_digits == 4:
        four(i, loop_count)

      elif num_digits == 5:
        five(i, loop_count)

  result.append(max(end))

for j in range (0,cases_num):
  print('#',j+1,' ',  result[j], sep = '')