import pygetwindow as gw

# 获取当前打开的所有窗口
all_windows = gw.getWindowsWithTitle('')
for window in all_windows:
    print(window)