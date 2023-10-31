snacks = ['Muffins', 'Tiramisu', 'Cheese Cake', 'Sandwich']
drinks = ['Black tea', 'Coffee', 'Orange Juice']
menus = []
for snack in snacks:
    for drink in drinks:
        menu = (snack, drink)
        menus.append(menu)

    for menu in menus:
        print(menu)
