# YouTube Donate Calculator

A tool that helps you calculate Super Chat earnings on the YouTube platform and allows you to display the calculated values in your live stream.

# Requirements

Python 3.9 and above

# Setup Instructions

### 1. Clone or download this repository.

Place the files in a suitable environment.

### 2. Open PowerShell in the folder where the files are located. If you are not familiar, refer to the image below.
![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/08d9453b-2447-4661-9e3e-4ba193f5771f)

### 3. Enter the following command
```script
pip install -r requirements.txt
```

### 4. Check if files are blank.
Initially, "AddAmountManual.txt," "CurrentDonateAmount.txt," and "DonateHistory.txt" should be completely blank. If you need to reset values in the future, simply make these three files blank.

### 5. Enter ``` python DonateCalculator.py ```

You should see a screen similar to the one below:
![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/8b700baa-3ea0-48f9-a282-be7bc1f3b670)

Enter your live stream ID, which can be found in the live stream URL (as shown below):
![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/f8913835-1bd1-481f-a2b1-67a85a6f92cf)

### 6. That's it! The tool is now running.

# Usage

### 1. Displaying values during a live stream
You can use OBS's text source and select "Read from file," specifying the path to "CurrentDonateAmount.txt."

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/5e741952-34cd-4ea9-a4a3-ac3c8d59fc4e)

### 2. Manual value adjustments

If you need to manually adjust values, open "AddAmountManual.txt" and enter the desired positive or negative value. Don't forget to save by pressing ```ctrl + s``` after making changes!


### 3. How to Use the Health Bar
Start by adding background.png to OBS:

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/123f2855-d868-4377-a09e-519a02e69c3a)

Insert the bar_example.png for positioning, ensuring that the green bar completely covers the health bar.

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/ac942100-f0d9-4a9d-98a0-5fae6b4cff38)

Replace bar_example.png with bar.png.

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/9eb3e388-3578-4b3a-995c-9f25e067b62d)

Finally, place heart.png on the heart in background.png, and you're all set!

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/000d8133-6e57-40c8-a709-856ff2921c9a)

The health bar will automatically rise with the increase in CurrentDonateAmount.
You can modify your donation goal in line 11 of DonateCalculator.py:

```python
TARGET = 500000
```
In the example above, the goal is set to five hundred thousand units.

Feel free to ask if you have any questions or need further clarification.

# ----------------------------------------------------------------

# Youtube 抖內計算機

一個可以幫你計算 YT 平台上 SC 收益的工具，也可以透過它來將數值顯示在你的直播上。

# Requirement

Python 3.9 and above

# How To Setup

### 1. 你可以直接 clone，或是下載這份 repo。
總之將檔案安置在一個環境宜人的地方。

### 2. 到檔案的資料夾，開啟你的 powershell，如果你不會開的話，請參照下圖。
![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/08d9453b-2447-4661-9e3e-4ba193f5771f)

### 3. 輸入下面的指令
```script
pip install -r requirements.txt
```

### 4. 檢查數值是否歸零
初始狀態下，"AddAmountManual.txt"、"CurrentDonateAmount.txt"、"DonateHistory.txt" 應該都要是完全空白的。
如果未來你要歸零數值的話，也是直接把這三個檔案都弄成空白即可。

### 5. 輸入
```script
python DonateCalculator.py
```

你應該會看到類似下圖的畫面：
![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/8b700baa-3ea0-48f9-a282-be7bc1f3b670)

請輸入你的 直播　ID，你可以在直播的網址中找到（如下圖）

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/f8913835-1bd1-481f-a2b1-67a85a6f92cf)


### 6. 這樣就開始執行啦！

# Usage

### 1. 在直播中顯示數值
你可以直接使用 OBS 中的文字截取

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/5e741952-34cd-4ea9-a4a3-ac3c8d59fc4e)

選擇從檔案讀取，並將路徑指定到 "CurrentDonateAmount.txt"

### 2. 手動修正數值

如果你發現今天有手動修改數字的需求，你可以打開 "AddAmountManual.txt"，輸入你想要增減的數值，增加就輸入數字即可，減去的話請輸入負值。

！！！修改後請按 ```ctrl + s ```存檔！！！

！！！修改後請按 ```ctrl + s ```存檔！！！

！！！修改後請按 ```ctrl + s ```存檔！！！

### 3. 血條如何使用

先把 background.png 放進 OBS：

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/123f2855-d868-4377-a09e-519a02e69c3a)

將定位用的 bar_example.png 放進去，使綠色條完全蓋住血條。

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/ac942100-f0d9-4a9d-98a0-5fae6b4cff38)

將 bar_example.png 取代成 bar.png

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/9eb3e388-3578-4b3a-995c-9f25e067b62d)

最後將 heart.png 蓋到 background.png 的愛心上，就大功告成啦！

![image](https://github.com/catagain/YT_Donate_Calculator/assets/35026988/000d8133-6e57-40c8-a709-856ff2921c9a)

血條會自動隨著 CurrentDonateAmount 上升。
你可以在 DonateCalculator.py 中的第 11 行
```python
TARGET = 500000
```
中修改你的 Donate 目標，上面的例子就是五十萬元。
