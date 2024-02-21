# 基于python的自动评判作业脚本
### 一.安装教程
#### 1.python环境就不需要我多说了吧
#### 2.所需库的安装
(1)安装tqdm库
``` pip install tqdm ```

(2)安装rich库
``` pip install rich ```

>（此为进度条的库，不想要的可以不安装哦）

(3)安装pyfiglet库
``` pip install pyfiglet ```

>（此为艺术字库，不想要的可以不安装哦）

(4)安装pygetwindow库
``` pip install pygetwindow ```

(5)安装pyperclip库
``` pip install pyperclip ```

(6)安装pyautogui库
``` pip install pyautogui ```

> （这个是读取程序和模拟键鼠输入的，需要安装）

---

### 二.自定义
因为此程序为面对性开发，所以很多功能只能在固定系统上起作用，程序仅供参考

在此我将给大家提供自定义思路，开发属于自己的脚本

### 1.识别窗口

通过使用tools文件夹下的``` 窗口.py ```进行读取窗口标题

``` window = gw.getWindowsWithTitle('你的窗口标题')[0] ```

让程序可以找到窗口，固定每个按键的坐标

``` window.moveTo(130, 100) ```

将窗口移动到合适的位置

---

### 2.批改作业
（1）通过使用tools文件夹下的``` 坐标.py ```进行读取关键位置的坐标

在python的写法:

``` pyautogui.click(100,100, clicks=1) ```

上面的意思为在``` 100,100 ```坐标，点击``` 1 ```次

（2）然后是输入，这里通过调用剪贴板的方式进行输入

``` pyperclip.copy() ```

将``` () ```内容移动到剪贴板

``` pyautogui.keyDown('ctrl') ```

``` pyautogui.keyDown('v') ```

使用快捷键粘贴

最后经过排列组合即可完成！！！

---

### 3.使用方法
如果需要评语请将注释部分打开即可
