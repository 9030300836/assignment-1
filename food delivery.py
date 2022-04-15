class Restaurant:
    def __init__(self, name, add):
        self.name = name
        self.add = add
        self.menu = dict()
        self.orders = []

    def __repr__(self):
        return f'name: {self.name}, Add:{self.add}'

    def add_menu(self, name, price):
        self.menu.update({name: price})

    def print_menu(self):
        for key, value in self.menu.items():
            print(f'{key} -------> {str(value)}')

    def order_recieved(self, new_order):
        self.orders.append(new_order)  

    def print_orders(self):
        for order in self.orders:
            print(order)

    def deliver_order(self):
        for order in self.orders:
            if order.status == 'Pending':
                order.change_status()
                print(order)

    def calculate_income(self):
        income = 0
        Users = set()
        for order in self.orders:
            if order.status == 'Delivered':
                if order.username.name in Users:
                    discount = 0
                else:
                    discount = 5
                    Users.add(order.username.name)
                    print(f'{discount}% discount is given to {order.username.name}')

                item = order.item
                qty = order.qty
                price = self.menu.get(item)
                income += ((price * qty) * ((100 - discount) / 100))
        print(income)


class User:
    def __init__(self, name, add, phone):
        self.name = name
        self.add = add
        self.phone = phone
        self.orders = [] 

    def __repr__(self):
        return f'name : {self.name},add : {self.add}, phone : {self.phone}'

    def print_menu(self, res_name):
        res_name.print_menu()

    def order_food(self, res_name, item, qty):
        new_order = Order(self, res_name, item, qty)  
        self.orders.append(new_order) 
        res_name.order_recieved(new_order)  

    def cancel_order(self):
        last_order = self.orders[-1]
        last_order.cancel_order()


class Order:
    def __init__(self, username, rest_name, item, qty):
        self.username = username
        self.rest_name = rest_name
        self.item = item
        self.qty = qty
        self.status = 'Pending'

    def change_status(self):
        self.status = 'Delivered'

    def cancel_order(self):
        if self.status != 'Delivered':
            self.status = 'Cancel'

    def __repr__(self):
        return f'user:{self.username.name}, item : {self.item}, qty : {self.qty}, status: {self.status}'
KFC = Restaurant('KFC','HYD')
Pista_House = Restaurant('Pista_House','HYD')
Pista_House.add_menu('Tandoori Chicken (4 pieces)',240)
KFC.add_menu('Vegan Burger (1 Piece)',320)
KFC.add_menu('Truffle Cake (500gm)',900)
pritom = User('Pritom','HYD','1213131331')
pritom.print_menu(Pista_House)
pritom.order_food(Pista_House,'Tandoori Chicken (4 pieces)',4)
Pista_House.print_orders()
Pista_House.deliver_order()
abhi = User('Anji','HYD','1213131331')
abhi.print_menu(KFC)
abhi.order_food(KFC,'Vegan Burger (1 Piece)',1)
KFC.print_orders()
pritom.order_food(KFC,'Vegan Burger (1 Piece)',5)
abhi.order_food(KFC,'Vegan Burger (1 Piece)',4)
pritom.order_food(KFC,'Truffle Cake (500gm)',2)
pritom.cancel_order()
KFC.deliver_order()
KFC.calculate_income()
dict1 = {'name':'Pritom','age':25}
dict1.get('name','Key is Not present')
100 *((100-5)/100)
def add(a,b):
    return (a+b)
add(1,2)
add,1,2,3