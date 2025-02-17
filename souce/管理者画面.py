import os
import keyboard


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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