# lst = [3, 1, 2]
# a = sorted(lst)
# b = lst.sort()
# print(a, b, lst)


# def classify(n):
#     if n < 0:
#         return "neg"
#     for i in range(n):
#         if i == 2:
#             return "big"
#     return "small"
 
# print(classify(3), classify(2), classify(1))

# z = {"60637", "94305", "07974"}
# z.discard("11111")
# z.remove("94305")
# print(len(z))
# z.remove("07974")
# print(len(z))

# import json
# s = '["grape", {"bar": [3.5, false, null]}]'
# x = json.loads(s)
# print(x)
# print(type(x), type(s))

# print(1 % 2)

# lang = ["Lisp", "Java", "Python", "Swift", "Haskell"]
# lang[2:5] = 5, 1
# print(lang, len(lang))

# n = [[0] * 3] * 3
# m = [[0] * 3 for i in range(3)]
# n[2][0] = 8
# m[2][0] = 8

# print(n, m)

# contribs = [("Kang", "94305", 75), ("Kang", "94305", 55),
#             ("Kodos", "94305", 35), ("Kodos", "94305", 55)]
# rv = {}
# for cand, z, amt in contribs:
#     if cand not in rv:
#         rv[cand] = {}
#     rv[cand][z] = rv[cand].get(z, 0) + amt
# print(rv)


# with open("RIO.txt", "w")as f:
#     f.write("RIO is smart\n")
#     f.write("Rio is beautiful")
#     f.write("Rio is a genious")

# with open("out.txt", "w") as f:
#     f.write("Ken\n")
#     f.write("Ivan\n")
#     f.write("Maya\n")
 
# with open("out.txt") as f:
#     print(f.read().splitlines())


# with open("instructors.csv") as f:
#     header = f.readline()
#     for row in f:
#         fields = row.strip().split(",")
#         print(len(fields))

# lst = [1, 2, 3, 4, 5, 2, 4, 5, 1]
# a = lst.pop(lst.index(1))
# b = lst.remove(2)
# print(a)
# print(b)
# print(lst)


# m = [[3, 3, 6], [4, 4, 4], [2, 2, 2]]
# n = []

# for i in m:
#     for j in i:
#         print(i[j])
#         # if i[j] == 3:
#         #     print(i)
#         # i[j] = 6


lst = [31, 14, 40, 22, 18, 21]
print(lst[-50:11])