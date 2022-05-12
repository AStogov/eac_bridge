import time
print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    input("")
    starttime = time.time()
    print(starttime)
    print('开始计时')
    try:
        while True:
            print('计时: ',(time.strftime("%M:%S", time.localtime(time.time() - starttime))), end="\r")
            time.sleep(0.001)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总用时为:', round(endtime - starttime, 2),'secs')
        break