# 4-7-8 呼吸法

一個簡單的 Python GUI 應用程式，實現著名的 4-7-8 呼吸法冥想技巧。

## 功能

- **視覺化呼吸指導**：使用顏色變化提示呼吸階段
  - 🔵 吸氣 (4 秒) - 藍色
  - 🟣 憋氣 (7 秒) - 紫色
  - 🟢 呼氣 (8 秒) - 綠色

- **簡潔操作介面**：一鍵開始和暫停

## 安裝

### 系統要求
- Python 3.7+
- macOS 或 Linux（tkinter 通常預裝）

### 依賴安裝

```bash
pip install -r requirements.txt
```

## 使用

執行應用程式：

```bash
python main.py
```

1. 點擊「開始」按鈕啟動呼吸練習
2. 依照螢幕上的指示和顏色進行呼吸
3. 點擊「停止」按鈕結束練習

## 技術棧

- **tkinter** - GUI 圖形介面（Python 內建）
- **PyInstaller** - 打包成獨立執行檔（可選）

## 打包成執行檔（選項）

使用 PyInstaller 將應用程式打包成獨立執行檔：

```bash
pyinstaller --onefile --windowed main.py
```

生成的執行檔位於 `dist/` 資料夾中。

## 許可

MIT License
