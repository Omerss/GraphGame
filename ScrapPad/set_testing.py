set_1 = set()

set_1.add(1)
set_1.add(1)
set_1.add(2)
set_1.add(2)

assert(len(set_1) == 2)

list_check = [0.003861003861003861, 0.1987179487179487, 0.6891891891891891, 0.31746031746031744, 0.04404145077720207, 17.125, 0.22072072072072071, 0.0038610038610038776, 0.19871794871794862, 0.6891891891891891, 0.31746031746031744, 0.0440414507772021, 17.12499999999993, 3.303030303030302, 0.22072072072072074]


set_2 = set()

for item in list_check:
    set_2.add(item)
set_2.add(17.125)

assert(len(set_2) == 5)