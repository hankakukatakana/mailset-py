import pyautogui

# 処理を実行するたびに1秒待機
pyautogui.PAUSE = 1.0

# 画面のサイズを取得
width, height = pyautogui.size()

# スタートボタン付近にカーソルを移動しクリック
pyautogui.moveTo(5, height-5, duration=1)
pyautogui.click()

# メモ帳のアプリを検索し、エンターで起動
pyautogui.write("memo")
pyautogui.press("enter")

# 文字を入力
pyautogui.write("It was created using the Python module pyautogui.")

# Ctrl+S で保存
pyautogui.hotkey("ctrl", "s")

# ファイル名を入力し、エンターキーで保存
pyautogui.write("Python.txt", interval=0.25)
pyautogui.press("enter")
