
fileObject = open("myfile.txt" )
myFile = fileObject.read()#注意读取出来的是字符串
print(myFile)


fileObject2 = open("test.txt" , "a")
#r，读取，默认，可不写；w，写入，目前只试验了txt，重新写入，不管以前有什么直接清空重写；+，可读可写，没试验出来区别待更新；b,二进制方式，可与读写连用；a,追加写入，不改变原有内容，新增写入。
fileObject2.write(myFile)
fileObject2.write("\n")
fileObject2.write("\f这个是我按照第一个文件\v重新定义的一个\t新文件")
fileObject2.writable()
fileObject2.close()#不要忘记关闭

fileObject.close()




