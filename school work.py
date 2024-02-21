from tqdm.rich import trange
from pyfiglet import Figlet
import pygetwindow as gw
import pyperclip
import pyautogui
import random
import time
#pingyu=["你的字太美了，批你的作业犹如在欣赏一件作品，谢谢你。",
#        "孩子，优异的成绩需要坚持，只要坚持每天都认真踏实的完成作业，老师相信最后的胜利者一定是你！",
#        "字如其人，你这样好看，相信你的字也会写得很帅的。",
#        "认真是你的朋友，马虎是你的敌人。快！把你的敌人赶走，把你的朋友请回来。",
#        "你的进步让老师看到了希望，你的努力给老师增加了信心，记住：一份耕耘一份收获，努力了就是最棒的！",
#        "看了你今天的作业，老师很高兴，知道你上课能认真学习了，希望你明天的表现更好！",
#        "你很聪明，如果把字再写得好一点，那就更好了！",
#        "你的作业给人的感觉赏心悦目，好孩子，继续努力，希望看到更加出色的你。",
#        "你养成了良好的学习习惯，特别是作业本很干净，书写也很端正，老师很高兴。",
#        "今天，我终于看到了低估工整的书写，我心里很高兴，原来只要用心去写，你是能写出一手好字的，对吗？",
#        "老师相信你，今后能按时完成作业的、能干的你会把字写得工工整整。",
#        "这次作业，你给我留下了深刻的印象，因为你写得好啊！",
#        "你最近几次作业，都有很大进步，只要努力一定能成功。“作业好”标兵非你莫属。",
#        "你想飞可以，但字不能飞出横格去，坚守规距，才能有出息。"]

fenshulowlb=[]
fenshuhightlb=[]
f = Figlet(font='slant')
print(f.renderText('school work'))
print("欢迎使用基于python的看作业辅助器---- school work")
print("作者:shuaqiyy")
if 1==1:
    window = gw.getWindowsWithTitle('凡高假期作业老师端')[0]
    print("已成功获取窗口")
    print("窗口名称：",window)
    window.moveTo(130, 100)
    shuliang=int(input("请输入份数："))
    tishu=int(input("题数："))
    #调取每个题的得分区间
    for c in range(tishu) :
        print("第",c,"题:")
        fenlow=int(input("最低分："))
        fenhight=int(input("最高分："))
        fenshulowlb.append(fenlow)
        fenshuhightlb.append(fenhight)
    #设置间隔时间
    shijianlow=int(input("间隔时间初始值："))
    shijianhight=int(input("间隔时间结束值："))
    print("份数：",shuliang)
    print("题数：",tishu)
    print("分值区间：",fenlow,"~",fenhight)
    print("间隔时间：",shijianlow,"~",shijianhight)
    for a in trange(shuliang) :
        shijian=random.uniform(shijianlow,shijianhight)
        print("同学",a)
        pingyubianliang=int(random.uniform(0,13))
        #shuchupingyu=pingyu[pingyubianliang]
        #输入部分
        #激活窗口
        window.activate()
        #点击第一个题
        pyautogui.click(192,534, clicks=1)
        time.sleep(shijian)
        for b in range(tishu) :
            fenlowshuchu=fenshulowlb[b]
            fenhightshuchu=fenshuhightlb[b]
            defen=int(random.uniform(fenlowshuchu, fenhightshuchu))
            print(b,"题")
            print("得分：",defen) 
            #点击输入分数
            pyautogui.click(584,849, clicks=1)
            time.sleep(shijian)
            #输入分数
            pyperclip.copy(defen)
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('v')
            time.sleep(shijian)
            #下一个题
            pyautogui.click(746,869, clicks=1)
            time.sleep(shijian)
        #提交
        pyautogui.click(614,978, clicks=1)
        time.sleep(shijian)
        #输入评语
        #pyautogui.scroll(500)
        #pyautogui.click(205,872, clicks=1)
        #time.sleep(shijian)
        #print("评语：",shuchupingyu)
        #pyperclip.copy(shuchupingyu)
        #pyautogui.keyDown('ctrl')
        #pyautogui.keyDown('v')
        #time.sleep(shijian)
        #下位同学
        pyautogui.click(677,1000, clicks=1)
        time.sleep(shijian)
else:
    print("未获取窗口")
    print("请重新开始")