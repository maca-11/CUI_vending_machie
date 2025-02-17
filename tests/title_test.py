import pytest
from unittest import mock
import sys

# 実際の show_title 関数がどのように実装されているか仮定
# 例: ユーザーがキーを押した場合に処理を行う関数
def show_title():
    import keyboard
    key = keyboard.read_event(suppress=True).name
    if key == "enter":
        pass  # 画面をクリアして処理が進む
    elif key == "esc":
        return "admin"  # 管理画面に遷移
    elif key == "q":
        sys.exit()  # シミュレータ終了

# テストケース
@mock.patch("keyboard.read_event")
def test_enter_key(mock_keyboard_read_event):
    # "enter" キーの入力を模擬
    mock_event = mock.Mock()
    mock_event.name = "enter"
    mock_keyboard_read_event.side_effect = [mock_event]  # キーイベントを返す
    result = show_title()
    assert result is None  # Enterで処理が進み、終了しない場合

@mock.patch("keyboard.read_event")
def test_esc_key(mock_keyboard_read_event):
    # "esc" キーの入力を模擬
    mock_event = mock.Mock()
    mock_event.name = "esc"
    mock_keyboard_read_event.side_effect = [mock_event]  # Escキーが押された場合
    result = show_title()
    assert result == "admin"  # Escで管理画面に進む

@mock.patch("keyboard.read_event")
def test_q_key(mock_keyboard_read_event):
    # "q" キーの入力を模擬
    mock_event = mock.Mock()
    mock_event.name = "q"
    mock_keyboard_read_event.side_effect = [mock_event]  # qキーでシミュレータ終了
    
    with pytest.raises(SystemExit):  # qでsys.exit()が呼ばれることを確認
        show_title()
