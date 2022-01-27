l, p = map(int, input().split())
guests_count = list(map(int, input().split()))

for guest in guests_count:
    print(guest - l * p, end=' ')
