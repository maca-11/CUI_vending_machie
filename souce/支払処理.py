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
        