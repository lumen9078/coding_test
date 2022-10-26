x_coordinates = {}
y_coordinates = {}

for _ in range (3):
    c = input().split()
    
    if c[0] in x_coordinates:
        x_coordinates[c[0]] += 1
    else:
        x_coordinates[c[0]] = 1
    if c[1] in y_coordinates:
        y_coordinates[c[1]] += 1
    else:
        y_coordinates[c[1]] = 1

print([k for k, v in x_coordinates.items() if v == 1][0], end=' ')
print([k for k, v in y_coordinates.items() if v == 1][0], end='')