class Building:
    city = None
    money = None
    nachalo = None
    konez = None

    def __init__(self, city='England', money='amount', nachalo='some time', konez='some time'):
        self.data(city,money,nachalo,konez)
        self.getdata()

    def data(self, city, money, nachalo, konez):
        self.city = city
        self.money = money
        self.nachalo = nachalo
        self.konez = konez

    def getdata(self):
        print('Building ans store are construction in', self.city, 'and was allocated', self.money, 'pounds.')
        print('Construction started at', self.nachalo, 'and is scheduled to end in', self.konez)

Building()
print()

class Store(Building):
    departments = None
    workers = None

    def __init__(self, city, money, nachalo, konez, departments, workers):
        super(Store, self).__init__(city, money, nachalo, konez)
        self.departments = departments
        self.workers = workers

    def data_store(self):
        print(f'City: {self.city}', f'Money: {self.money}', f'Start: {self.nachalo}', f'Estimated end: {self.konez}', f'Departments: {self.departments}', f'Workers: {self.workers}', sep='\n')

a = Store('London', 1000000, '01.04.2022', '04.09.2024', '12', '50')
print()
a.data_store()