# encoding=utf-8

from datetime import date

class BanK():
    def __init__(self, base, Fio, opendate, balance, percent, id):
        self.base = base[Client(Fio, opendate, balance, percent, id)]


    def print_clientList(self):
        print(self.base)


    def addClient(self):
        self.Fio = input('введите ФИО')
        self.opendate = date.today()
        self.ballance = 0
        self.persent = 0
        self.id = int(input('введите ID'))


    def showByCode(self):
        code = input("введите ID")
        if code in self.base:
            print(Client)

    def showByMoney(self):
        money = input('введите миниальный баланс')
        while self.ballance >= money:
            print()


class Client(BanK):
    def __init__(self, Fio, opendate, balance, percent, id):
        self.Fio = Fio
        self.opendate = opendate
        self.balance = balance
        self.percent = percent
        self.id = id

Bank = ()
Bank.addClient('Вася Пупкин', 123)

