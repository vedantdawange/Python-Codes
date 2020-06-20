team = {'p1': 181, 'p2': 187, 'p3': 179, 'p4': 185, 'p5': 186,
        'p6': 175, 'p7': 192, 'p8': 189, 'p9': 196, 'p10': 180, 'p11': 193}
largest=0

for k,v in team.items():
    if int(v)>largest:
        largest=v
        captain=k

print("Captain:",captain)