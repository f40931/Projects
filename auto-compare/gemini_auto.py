import pyperclip
import pyautogui
import time
from pywinauto import Desktop

def start_automation():
    print("自動化程式已啟動... 請依序複製「你的翻譯」與「正確解答」")
    
    last_clipboard = pyperclip.paste() # 記錄初始剪貼簿內容
    first_text = ""
    
    while True:
        # 獲取當前剪貼簿內容
        current_clipboard = pyperclip.paste()
        
        # 如果剪貼簿內容改變了
        if current_clipboard != last_clipboard:
            if not first_text:
                # 這是第一次複製（你的翻譯）
                first_text = current_clipboard
                last_clipboard = current_clipboard
                print(f"✅ 已偵測到翻譯：{first_text[:20]}...")
                print("請繼續複製「正確解答」...")
            else:
                # 這是第二次複製（正確解答）
                second_text = current_clipboard
                print(f"✅ 已偵測到解答：{second_text[:20]}...")
                
                # 組合字串
                final_prompt = f"{first_text} vs. {second_text}"
                
                # 執行自動化操作
                print("🪄 正在傳送到 Gemini...")
                send_to_gemini(final_prompt)
                
                # 重置狀態，準備下一組
                first_text = ""
                last_clipboard = pyperclip.paste() 
                print("\n--- 等待下一組練習 (請先複製翻譯) ---")
        
        time.sleep(0.5) # 每 0.5 秒檢查一次，避免占用過多 CPU

def send_to_gemini(text):

    # 1. 將組合好的 Prompt 放入剪貼簿
    pyperclip.copy(text) 
    
    try:
        # 2. 尋找 Edge 視窗
        # 我們尋找標題包含 "Edge" 的視窗
        windows = Desktop(backend="win32").windows()
        edge_win = None
        
        for w in windows:
            if "Edge" in w.window_text():
                edge_win = w
                break
        
        if edge_win:
            # 強制設定焦點
            edge_win.set_focus()
            print("🚀 已成功切換至 Edge")
        else:
            print("❌ 找不到 Edge 視窗，請確認 Edge 是否已開啟")
            return

    except Exception as e:
        print(f"切換視窗時發生小意外 (但不影響): {e}")
        # 如果失敗，保險起見用最原始的 Alt+Tab 頂替一下
        pyautogui.hotkey('alt', 'tab')
    
""" 
## 現在沒辦法解決找到gemini 對話框的方法

    time.sleep(0.8) # 給視窗一點反應時間
    # 3. 執行貼上與送出
    # 注意：請確保你的 Edge 焦點是在 Gemini 的輸入框內
    pyautogui.hotkey('ctrl', 'v')  # 貼上內容
    time.sleep(0.2)
    pyautogui.press('enter')       # 送出 Prompt
 """

if __name__ == "__main__":
    try:
        start_automation()
    except KeyboardInterrupt:
        print("\n程式已停止。")