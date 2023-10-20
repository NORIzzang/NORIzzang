l1 = [(1, 2), (3, 4), (5, 6)]
for t in l1:
    print(t)
    print(t[0] + t[1])

    # 변수 선언 :
    a, b = (1, 2)
    print(a + b)
    print("==" * 30)

    for a, b in l1:
        print(a + b)

(a, b) = (1, 2)
for (a, b) in l1:
    print(a + b)

print("==" * 30)
l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for a, b, c in l2:  # l2 의 대괄호 묶음이 3개 여서 a,b,c
    print(a + b + c)
for (a, b, c) in l2:
    print(a + b + c)
for (a, b, c) in l2:
    print(a + b + c)
