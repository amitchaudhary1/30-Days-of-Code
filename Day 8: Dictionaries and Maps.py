n = int(input())
amit = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in amit}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
