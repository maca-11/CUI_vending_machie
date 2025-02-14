def select_products(products):
    cart = {}
    while True:
        print("\n商品一覧:")
        for num, item in products.items():
            print(f"{num}. {item['name']} {item['price']}円")
        print("c. 購入確定")
        choice = input("購入する商品番号を入力してください: ")
        if choice == 'c':
            break
        if choice.lower() == 'esc':
            return 'admin'
        if not choice.isdigit() or int(choice) not in products:
            print("無効な入力です。再入力してください。")
            continue
        choice = int(choice)
        cart[choice] = cart.get(choice, 0) + 1
    return cart

def select_products(products):
    cart = {}
    while True:
        print("\n商品一覧:")
        for num, item in products.items():
            print(f"{num}. {item['name']} {item['price']}円")
        print("c. 購入確定")
        choice = input("購入する商品番号を入力してください: ")
        if choice == 'c':
            break
        if choice.lower() == 'esc':
            return 'admin'
        if not choice.isdigit() or int(choice) not in products:
            print("無効な入力です。再入力してください。")
            continue
        choice = int(choice)
        cart[choice] = cart.get(choice, 0) + 1
    return cart