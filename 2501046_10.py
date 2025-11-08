# 25
# keys = input().split()
# values = input().split()
# d = dict(zip(keys, values))
# print(d)

# 26
# park = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# print(park['english'])
# print(park['science'])

# 27
# kim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# kim.update(korean=100, english=100, mathematics=100, science=100)
# print(kim)

# 28
# lee = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# if 'english' in lee:
#     lee.pop('english')
# print(lee)

# 29
# lim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# for i, j in lim.items():
#     print(i, j)

# 30
# choi = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# a = {key: value for key, value in choi.items() if value >= 90}
# for i in a.keys():
#     print(i, end=' ')

# 31
# yoo = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
# a = sum(yoo.values()) / len(yoo)
# print(a)