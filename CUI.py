import os
import sys
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    print("""
    ******************************
        券売機シミュレーター
    ******************************
    Please Enter (Enterキー押下で画面がクリアされて処理が進む)
    (escキー押下で管理画面に処理が進む)
    (qキー押下でシミュレータ終了)
    """)

    while True:
        key = keyboard.read_event(suppress=True).name
        if key == 'enter':
            clear_screen()
            break
        elif key == 'esc':
            return 'admin'
        elif key == 'q':
            print("シミュレーターを終了します...")
            sys.exit()

def show_menu():
    products = {
        1: {"name": "特製ラーメン", "price": 1000, "sales": 50},
        2: {"name": "醤油ラーメン", "price": 780, "sales": 10},
        3: {"name": "しおラーメン", "price": 880, "sales": 25},
        4: {"name": "ごはん", "price": 150, "sales": 6}
    }
    return products

def show_admin_panel(products):
    clear_screen()
    print("""
    ******************************
        管理画面
    ******************************
    """)
    print("======== 商品一覧 ========")
    print("商品       単価    販売数    売上金額")
    print("=================================")
    total_sales = 0
    sales_reset = True  # 売上がリセットされているかどうかを示すフラグ
    for num, item in products.items():
        sales_amount = item["sales"] * item["price"]
        total_sales += sales_amount
        if item["sales"] != 0:
            sales_reset = False  # 販売数がリセットされていない場合フラグをFalseに設定
        print(f"{num}. {item['name']}  {item['price']}円   {item['sales']}   {sales_amount}円")
    print("=================================")
    print(f"総売上金額  {total_sales}円")
    print("\n----- 管理メニュー -----")
    print("1. 売上をリセットする")
    print("2. 商品の価格を変更する")
    print("3. 管理画面を終了する")

    choice = input("\n管理コード入力: ")
    if choice == '1':
        for item in products.values():
            item["sales"] = 0
        print("売上をリセットしました。")
    elif choice == '2':
        if sales_reset:
            try:
                print("\n商品番号と新しい価格を入力してください。")
                product_number = int(input("商品番号: "))
                new_price = int(input("新しい価格: "))
                if product_number in products:
                    products[product_number]["price"] = new_price
                    print(f"{products[product_number]['name']}の価格が{new_price}円に変更されました。")
                else:
                    print("無効な商品番号です。")
            except ValueError:
                print("無効な入力です。")
        else:
            print("価格を変更する前に売上をリセットしてください。")
            print("Enterキーを押して続行...")
            while True:
                key = keyboard.read_event(suppress=True).name
                if key == 'enter':
                    clear_screen()
                    break
    elif choice == '3':
        print("\n管理画面を終了します。")
    
    print("\n管理画面に戻ります...")
    print("aキーを押してください...")
    while True:
        key = keyboard.read_event(suppress=True).name
        if key == 'a':
            clear_screen()
            break

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

def calculate_total(cart, products):
    print("\n購入商品一覧:")
    total = 0
    for num, qty in cart.items():
        name = products[num]["name"]
        price = products[num]["price"]
        print(f"{name} × {qty}個  {price * qty}円")
        total += price * qty
    print(f"合計{total}円です。")
    return total

def process_payment(total):
    while True:
        try:
            print(f"\n合計{total}円です。現金を投入してください: ")
            
            while True:
                key = keyboard.read_event(suppress=True).name
                if key == 'enter':
                    money = int(input(f"\n合計{total}円です。現金を投入してください: "))
                    break

            if money < total:
                print("金額が不足しています。タイトル画面に戻ります。")
                print("aキーを押して続行...")
                while True:
                    key = keyboard.read_event(suppress=True).name
                    if key == 'a':
                        clear_screen()
                        return None

            change = money - total
            print(f"ご購入ありがとうございます。おつり{change}円です。")
            print("お釣りを受け取った後、wキーを押してタイトル画面に戻ります...")

            while True:
                key = keyboard.read_event(suppress=True).name
                if key == 'w':
                    clear_screen()
                    return change
        except ValueError:
            print("無効な金額です。タイトル画面に戻ります。")
            print("aキーを押して続行...")
            while True:
                key = keyboard.read_event(suppress=True).name
                if key == 'a':
                    clear_screen()
                    return None

def update_sales(cart, products):
    """ 購入が完了したら、販売数を更新 """
    for num, qty in cart.items():
        products[num]["sales"] += qty  # 販売数を加算

def main():
    products = show_menu()
    while True:
        result = show_title()
        if result == 'admin':
            show_admin_panel(products)
            continue

        cart = select_products(products)
        if cart == 'admin':
            show_admin_panel(products)
            continue
        if not cart:
            print("購入がキャンセルされました。タイトル画面に戻ります。")
            continue
        
        total = calculate_total(cart, products)
        if process_payment(total) is None:
            continue
        
        # 販売数を更新
        update_sales(cart, products)


if __name__ == "__main__":
    main()