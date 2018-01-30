import walkSearch


def writeList(mylist, myfile):
    f = open(myfile, 'w', encoding='utf-8')
    for i in mylist:
        for j in i:
            j = str(j)
            f.write(j + "\n")
    f.close()


if __name__ == '__main__':
    f = open("C:/核心资料/肖伟祥/会计杂项参数2018-1-19.txt", "r")
    # f = open("E:/aaa.txt", "r", encoding='utf-8')
    lines = f.readlines()  # 读取全部内容
    b = []
    i = 0
    myfile = "E:/ccc.txt"
    for line in lines:
        print(line)
        i += 1
        line = str(line).strip()
        a = walkSearch.detect_walk(line, myfile, "C:/core-local/frw_user_apps/apps/onl/modules")
        # print(a)
        if len(a)>0:
            b.append(a)
    print("len(b)="+str(len(b)))
    print("i="+str(i))
    myfile1 = "E:/bbb.txt"
    writeList(b, myfile1)
    # print(len(b))
    f.close()
