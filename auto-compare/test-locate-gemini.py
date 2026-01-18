from pywinauto import Application
import time

def test_locate_gemini():
    try:
        # 連接到 Edge
        app = Application(backend="uia").connect(title_re=".*Gemini.*", timeout=5)
        dlg = app.top_window()
        
        # 根據你找出的 aria-label 定位
        # 這裡不指定 control_type，讓它用 Name 直接找，增加成功率
        input_box = dlg.child_window(title="Enter a prompt here")
        
        if input_box.exists():
            print("🎯 找到對話框了！")
            # 在螢幕上把該元素框起來（你會看到紅框閃爍）
            input_box.draw_outline(colour='red', thickness=2)
            
            # 測試獲取焦點並輸入測試文字
            input_box.set_focus()
            time.sleep(0.5)
            # 因為是 contenteditable div，有時需要點擊一下
            input_box.click_input() 
            input_box.type_keys("Hello Gemini!", with_spaces=True)
        else:
            print("❌ 雖然標籤對，但 UIA 抓不到這個元素。")
            
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    test_locate_gemini()