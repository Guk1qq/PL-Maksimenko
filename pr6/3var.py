d = [1, 2, 4, 6, 7, 9, 13, 4]
#первое
print(sum(s for j , s in enumerate(d) if j % 2 != 0))
#второе
print([2 * s if s < 15 else s for s in d])
