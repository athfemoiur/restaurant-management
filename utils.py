# TODO-4: Add create_time() function which get proper data from user,
#       create Item instance and return
# TODO-4: Add get_order() function which will:
#       get item data from user, create Order intance and return
#       Call show_menu() method of Item class on the top of each order,
#       User can select any item, anytime
#       It's up to you (developer) how to store items(by id, uuid, instance)
# TODO-4: Add show_unpaid_bill() function which will render a list to console
# TODO-4: Add pay_bill() function which just get a bill identifier
#       (id, uuid or ...) and set all related payment flags to True
# TODO-4: Add get_finance_report() method which will show last 10 paid
#       Payments and aggregation of all paid payments as integer (Hint: use
#       paid_list() method of Payment class)


from finance import Bill, Payment
from menu import Item
from order import Order


def create_time():
    while True:
        name = input('Enter the name of the item:  ')
        item_type = input('Enter the type of item (f,s,b):  ').lower()
        if item_type not in ('f', 's', 'b'):
            print('Invalid item type! choose (f,s,b)')
            create_time()
        price = input('Enter the price of the item:  ')
        Item(name, item_type, price)
        is_continue = input('Do you want to continue? (y/n): ').lower()
        if is_continue == 'n':
            return None


def get_item_dict():
    orders = {}
    while True:
        item = input('Enter item name: ').lower()
        for itm in Item.item_list:
            if itm.name == item:
                item = itm.item_id
        count = int(input('Please Enter the count: '))
        orders[item] = count
        is_continue = input('Do you want to add items? (y/n): ').lower()
        if is_continue == 'n':
            return orders


def in_out_handler():
    in_out = input("Enter 'i' for in or 'o' for out : ").lower()
    return in_out


def get_order():
    Item.show_menu()
    item_dict = get_item_dict()
    in_out = in_out_handler()
    Order(item_dict, in_out)


def show_unpaid_bill():
    print(Bill.show_unpaid())


def pay_bill():
    uuid = input('Enter the uuid of the bill which you want to pay: ')
    for bill in Bill.bill_list:
        if bill.uuid == uuid:
            return bill.payment.pay()
    print('There is no bill with this uuid')


def get_finance_report():
    paid_payments = Payment.paid_list()
    if len(paid_payments) == 0:
        return 0
    elif 10 > len(paid_payments) > 0:
        return sum(pym.prcie for pym in paid_payments)
    else:
        return sum(pym.prcie for pym in paid_payments[-10:])
