def road (v,t):
    s = v*t
    return(s)
car1 = road(int(input()),int(input()))
car2 = road(int(input()),int(input()))
if car1 > car2:
    itog = car1 - car2
    print('первая машина проехала на', itog, 'больше ')
elif car2 > car1:
    itog = car2 - car1
    print('вторая машина проехала на',itog, 'больше')
else:
    print('пути равны', car1)
s = lambda r:(r*r)*3.14
nyaf = s(int(input()))
print(nyaf)

