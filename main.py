# TODO-5: Create app main loop with the following key options:
#       o: Create new order
#       l: Show list of un paid bills
#       p: Pay one bill by (your preferred) key
#       r: Reset current loop, for example if is inside create order
#            should reset and start loop again
#       e: Exist from current loop, for example step out from create_order
#            to the main menu
#       esc: Close program
# Note: Be careful of user inputs, you should accept L instead of l, E instead
# of e or ...
from utils import create_time, show_unpaid_bill, pay_bill, get_order

switches = {'o': 'create new order',
            'c': 'create item',
            'l': 'show list of unpaid bills',
            'p': 'pay one bill',
            'e': 'exit',
            }


def run():
    for k, v in switches.items():
        print(f"Enter '{k}' for {v} ")

    inp = input(':  ').lower()

    if inp == 'o':
        get_order()
        run()
    elif inp == 'c':
        create_time()
        run()
    elif inp == 'l':
        show_unpaid_bill()
        run()
    elif inp == 'p':
        pay_bill()
        run()
    elif inp == 'e':
        print('program closed !')
        return None
    else:
        print('Invalid input')
        run()


if __name__ == "__main__":
    run()
