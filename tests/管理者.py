import unittest
from unittest.mock import patch, call
import CUI
# 'CUI' 関数をインポートしてください
# from your_module import CUI

class TestShowAdminPanel(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'enter', '2', '1', 'enter', 'a'])
    @patch('builtins.print')
    @patch('keyboard.read_event')
    def test_sales_reset(self, mock_read_event, mock_print, mock_input):
        products = {
            1: {"name": "特製ラーメン", "price": 1000, "sales": 50},
            2: {"name": "醤油ラーメン", "price": 780, "sales": 10},
            3: {"name": "しおラーメン", "price": 880, "sales": 25},
            4: {"name": "ごはん", "price": 150, "sales": 6}
        }
        
        # キーボードイベントのモック
        mock_read_event.side_effect = [
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'a'})
        ]

        CUI(products)

        # 売上がリセットされていることを確認
        for item in products.values():
            self.assertEqual(item['sales'], 0)

        # プリント文が正しく呼び出されていることを確認
        mock_print.assert_any_call("売上をリセットしました。")

    @patch('builtins.input', side_effect=['2', 'enter', '2', '1', '1000', 'enter', 'a'])
    @patch('builtins.print')
    @patch('keyboard.read_event')
    def test_change_price_with_sales_reset(self, mock_read_event, mock_print, mock_input):
        products = {
            1: {"name": "特製ラーメン", "price": 1000, "sales": 0},
            2: {"name": "醤油ラーメン", "price": 780, "sales": 0},
            3: {"name": "しおラーメン", "price": 880, "sales": 0},
            4: {"name": "ごはん", "price": 150, "sales": 0}
        }
        
        # キーボードイベントのモック
        mock_read_event.side_effect = [
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'a'})
        ]

        CUI(products)

        # 価格が変更されていることを確認
        self.assertEqual(products[1]['price'], 1000)
        mock_print.assert_any_call("特製ラーメンの価格が1000円に変更されました。")

    @patch('builtins.input', side_effect=['2', 'enter', '2', '1', '1000', 'enter', 'a'])
    @patch('builtins.print')
    @patch('keyboard.read_event')
    def test_change_price_without_sales_reset(self, mock_read_event, mock_print, mock_input):
        products = {
            1: {"name": "特製ラーメン", "price": 1000, "sales": 50},
            2: {"name": "醤油ラーメン", "price": 780, "sales": 10},
            3: {"name": "しおラーメン", "price": 880, "sales": 25},
            4: {"name": "ごはん", "price": 150, "sales": 6}
        }

        # キーボードイベントのモック
        mock_read_event.side_effect = [
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'enter'}),
            type('Event', (object,), {'name': 'a'})
        ]

        CUI(products)

        # 価格が変更されていないことを確認
        self.assertNotEqual(products[1]['price'], 1000)
        mock_print.assert_any_call("価格を変更する前に売上をリセットしてください。")

if __name__ == '__main__':
    unittest.main()
