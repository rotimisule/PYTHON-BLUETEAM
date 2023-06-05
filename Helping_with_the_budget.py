spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]
x = 0 
for low_months in spendings:
        if (low_months<1000 ):
           x = x+1
y = 0
for normal_months in spendings:
    if ( normal_months <2500):
        y = y+1
z= 0
for high_months in spendings :
    if (high_months <= 2500):
        z =z+1

print("Numbers of months with low spendings:" ,x, ", normal spendings: " ,y,", high spendings:" , z , ".")