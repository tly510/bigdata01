number = int(input())
count = 0

if number >= 2:
    for i in range(2, number):
        if number % i == 0:
            count += 1
            print(i, end=" ")

    if count == 0:
        print(f"{number}은(는) 소수입니다.")
    else:
        print(f"{number}은(는) 소수가 아닙니다!")