rating = [1, 5, 8, 6, 4, 4, 7, 9, 8, 9, 2, 1, 4]
a = int(input('Enter new place: '))

rating.sort()
if a in rating:
    rating.insert(rating.index(a), a)
else:
    rating.append(a)
rating.sort()
rating.reverse()
print(rating)