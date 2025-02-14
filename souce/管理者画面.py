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
    for num, item in products.items():
        sales_amount = item["sales"] * item["price"]
        total_sales += sales_amount
        print(f"{num}. {item['name']}  {item['price']}円   {item['sales']}   {sales_amount}円")
    print("=================================")
    print(f"総売上金額  {total_sales}円")
    print("\n----- 管理メニュー -----")
    print("1. 売上をリセットする")
    print("2. 商品の価格を変更する")
    print("3. 管理画面を終了する")

