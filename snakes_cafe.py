def welcome():
    print(
        """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Beverages
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
        """
    )


def goodbye():
    print(
        """
***************************************
** Thanks for coming to Snakes Cafe! **
**           See you soon!           **
***************************************
        """
    )


def order_manager():
    # dictionary with the menu items as keys
    menu_items = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0,
    }

    while True:
        user_input = input("> ").title()
        if user_input == "Quit":
            print("\n You ordered:")
            for i in menu_items:
                if menu_items[i] != 0:
                    print(f" - {menu_items[i]} of {i}")
            break
        elif user_input in menu_items:
            menu_items[f"{user_input}"] += 1
            print(
                f"** {menu_items[f'{user_input}']} order of {user_input} have been added to your meal **"
            )
        else:
            print(f"** we don't serve {user_input} **")


if __name__ == "__main__":
    welcome()
    order_manager()
    goodbye()
