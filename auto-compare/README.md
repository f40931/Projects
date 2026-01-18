English Back-Translation Automation Tool
英文反譯練習自動化工具
本專案是一個基於 Python 的自動化工具，旨在優化英文學習中的「反譯練習」流程。透過監控剪貼簿動作，自動將使用者的翻譯與正確解答組合成 Prompt，並自動傳送至 Google Gemini 進行語言差異分析。

🚀 功能特點 (Key Features)
自動化串接：消除在 Word、Anki 與瀏覽器之間頻繁切換與貼上的重複動作。

智能監聽：透過 pyperclip 實現背景監控，依序捕捉「翻譯」與「解答」兩組數據。

精準視窗對焦：利用 pywinauto 直接調度 Microsoft Edge 進程，確保操作準確。

雙語 README：適合放入個人作品集，展示解決自動化問題的能力。

🛠️ 技術棧 (Tech Stack)
語言：Python 3.13+

核心庫：

pywinauto：負責處理 Windows 視窗層級的控制與焦點切換。

pyperclip：監控與操作系統剪貼簿。

pyautogui：輔助執行鍵盤宏指令（Keyboard Macros）。

📝 開發歷程與技術挑戰 (Development Journey & Troubleshooting)
作為一名目標為 AI Architect 的開發者，我記錄了在本專案中遇到的底層挑戰與對應的解決方案：

1. 視窗控制權限與 API 異常 (PyGetWindowException)
挑戰：最初使用 pygetwindow 嘗試喚醒 Edge 視窗時，頻繁觸發 PyGetWindowException: Error code 0。

原因：Windows 的安全限制（Focus Stealing Prevention）導致一般 API 無法強制奪取焦點。

對策：改用 pywinauto 的 set_focus() 方法，透過更底層的 Win32 API 調用，成功穩定地在不同視窗間切換。

2. UI Automation (UIA) 元素定位失效
挑戰：即使透過 DevTools 與 Accessibility Insights for Windows 鎖定了輸入框的 aria-label="Enter a prompt here"，UIA 仍無法直接存取該 div 元素。

原因：現代瀏覽器（Chromium）將網頁內容封裝在深層的 Accessibility Tree 中，導致作業系統層級的 UIA 無法直接穿透 Shadow DOM。

對策：採用「混合式路徑」——利用 pywinauto 鎖定視窗主體後，配合快捷鍵發送與焦點引導，確保數據能正確填入動態生成的 Web 元件。

3. 異步監控邏輯優化
挑戰：如何判斷使用者何時完成兩次複製動作？

對策：設計了一個狀態機迴圈，透過對比前後剪貼簿內容的 hash 值變化來觸發動作，並加入 time.sleep(0.5) 優化 CPU 佔用率。

⚙️ 安裝與操作說明 (Usage)
1. 環境準備
Bash

pip install pyperclip pyautogui pywinauto
2. 啟動程式
Bash

python gemini_auto.py
3. 操作流程
開啟 Edge：保持 Gemini 頁面開啟。

複製翻譯：在 Word 選取你的翻譯並按 Ctrl+C。

複製解答：在 Anki 選取答案並按 Ctrl+C。

自動運行：腳本將自動切換至 Edge，輸入 [翻譯] vs. [解答] 並送出。

📅 未來計畫 (Roadmap)
[ ] API 整合：由 GUI 模擬轉向 Google Gemini API，實現無頭化（Headless）處理。

[ ] 自動化建卡：串接 AnkiConnect，將 Gemini 分析出的生疏用法自動轉存為 Anki 卡片。

[ ] 異常處理優化：增加對瀏覽器多標籤頁的自動搜尋邏輯。

Project Author: [Your Name] Focus: Python Automation, NLP Study Flow, AI Tooling