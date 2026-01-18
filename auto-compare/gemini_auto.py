import pyperclip
import pyautogui
import time

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
    # 切換到瀏覽器（假設你已經開著 Gemini 的分頁）
    # 使用 Alt + Tab 或是根據你的視窗排序切換，這裡建議手動點到瀏覽器後啟動程式
    # 或者你可以使用快捷鍵直接貼上
    
    pyperclip.copy(text) # 將組合好的字串放入剪貼簿
    
    # 模擬自動操作
    time.sleep(0.5) 
    pyautogui.hotkey('alt', 'tab') # 切換視窗到瀏覽器 (視情況調整次數)
    input()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')  # 貼上內容
    time.sleep(0.2)
    pyautogui.press('enter')       # 送出 Prompt

if __name__ == "__main__":
    try:
        start_automation()
    except KeyboardInterrupt:
        print("\n程式已停止。")