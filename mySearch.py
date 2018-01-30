# coding="utf-8"
import os


def find_dir(str, path):
    """

    :param str:
    :param path:
    :return:
    """
    print("目录是： %s" % os.path.abspath(path))
    # 遍历当前文件，找出符合要求的文件，将路径添加到l中
    for filename in os.listdir(path):
        deeper_dir = os.path.join(path, filename)
        if os.path.isfile(deeper_dir) and str in filename:
            print("%s 含有 %s " % (filename, str))
        if os.path.isdir(deeper_dir):
            find_dir(str, deeper_dir)


if __name__ == '__main__':
    find_dir("fo", "E:/fortbox\经验总结")
