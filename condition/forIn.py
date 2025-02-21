[(xx, yy) for xx in x for yy in y if xx != yy]

# another way to solve the problem

l = []
for xx in x:
    for yy in y:
        if xx != yy:
            l.append((xx, yy))
