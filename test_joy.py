import pygame
import time

# Pygameの初期化
pygame.init()
pygame.joystick.init()

# コントローラーのチェック
if pygame.joystick.get_count() == 0:
    print("コントローラーが見つかりません！接続を確認してください。")
    exit()

# 最初のコントローラーを使用
joy = pygame.joystick.Joystick(0)
joy.init()

print(f"--- {joy.get_name()} の入力を監視中 (Ctrl+Cで終了) ---")

try:
    while True:
        # イベントを処理（これがないと数値が更新されません）
        pygame.event.pump()

        # 左スティックの上下（通常は軸1）
        # ※コントローラーによって番号が違うので、動かして確認してください
        axis_0 = joy.get_axis(0) # 左右
        axis_1 = joy.get_axis(1) # 上下
        
        # ボタン0（XboxならAボタン、PSなら×ボタンなど）
        btn_0 = joy.get_button(0)

        # 画面に表示 (\r で同じ行に上書き表示)
        print(f"Stick L(X, Y): {axis_0:>6.2f}, {axis_1:>6.2f} | Button 0: {btn_0}", end="\r")
        
        time.sleep(0.05) # 少し待機（20Hz）

except KeyboardInterrupt:
    print("\n終了しました。")
finally:
    pygame.quit()