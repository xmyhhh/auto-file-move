import os, shutil, sys
import threading
import configparser
import datetime


# 复制文件
def remote_copy(src_path, dst_path):
    start_time = datetime.datetime.now()
    print(start_time, " 开始复制……")

    try:
        # 获取源文件夹中的所有文件及文件夹
        files = os.listdir(src_path)
        for file in files:
            # 生成绝对路径
            src_file = os.path.join(src_path, file)
            # 判断是否为文件
            if os.path.isfile(src_file) :
                dst_file = os.path.join(dst_path, file)
                shutil.move(src_file, dst_file)
                print(src_file, ' => ', dst_file, 'move done!')

    except Exception as e:
        print("复制失败！")
        os.system('pause')
        sys.exit()


    end_time = datetime.datetime.now()
    print(end_time, " 本次执行完毕，等待", span, "秒……")


# 定时复制
def timer_copy(src_path, dst_path):
    remote_copy(src_path, dst_path)


    global timer
    timer = threading.Timer(span, timer_copy, [src_path, dst_path])
    timer.start()

# 程序入口
if __name__ == "__main__":

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    src_path = config.get('path', 'srcPath')
    dst_path = config.get('path', 'dstPath')
    global span
    span = config.getint('run', 'timeSpan')


    # 目的路径不存在则建立路径
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)

    print("配置文件为 ：config.ini")
    print("执行间隔为 ：", span)
    print("输入文件夹为：", src_path)
    print("输出文件夹为：", dst_path)

    timer = threading.Timer(1, timer_copy, [src_path, dst_path])
    timer.start()

