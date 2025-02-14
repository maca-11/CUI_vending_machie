import os

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
