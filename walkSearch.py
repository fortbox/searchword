import os

import codecs


def writeList(mylist, myfile):
    f = open(myfile, 'w', encoding='utf-8')
    # print(mylist)
    f.write(str(mylist))
    f.close()


def detect_walk(str, myfile, dir_path):
    mylist = []
    myNote = -1
    for root, dirs, files in os.walk(dir_path):
        # print(len(dirs))
        # print(root)
        # print(dirs)
        # print(files)
        # print(str)

        # print(type(files))
        for filename in files:
            # print(len(mylist))
            # print(filename)
            if str != "":
                f = open(os.path.join(root, filename), "rb")
                a = f.read()
                # print(a)
                writeList(a, myfile)
                f.close()
                f1 = open(myfile, 'r', encoding='utf-8')
                aa = f1.read()
                # print(type(aa))
                # print(c.find(str))
                if (aa.find(str) != -1):
                    str1 = str + "在文件" + os.path.join(root, filename)
                    # mylist.append(str1)
                    myNote = 1
                f1.close()
                # if str in filename:
                #     # print("%s 在文件 %s " % (str, os.path.join(root, filename)))
                #     str1 = str + "在文件" + os.path.join(root, filename)
                #     mylist.append(str1)
                # else:
                #     # print("%s 没有在文件 %s" % (str, os.path.join(root, filename)))
                #     str1 = str + "没有在文件" + os.path.join(root, filename)
                #     # mylist.append(str1)
    if (myNote == -1):
        mylist.append(str)
    return mylist


if __name__ == "__main__":
    myfile = "E:/ccc.txt"
    b = detect_walk("DATA", myfile,
                    "C:/core-local/frw_user_apps/apps/onl/modules/busi/ac/src/main/resources/report/genl")
    # print(b)
