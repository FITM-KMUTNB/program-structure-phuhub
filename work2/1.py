def line ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    keep=0
    for i in read1:
        if i == "\n":
            keep=keep+1
        else:
            pass
    print(keep)

def sentense ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    read2=read1.split(".")
    print (len(read2)-1)
def word ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    read2=read1.split()
    print (len(read2)-1)
def letter ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    keep=0
    for i in read1:
        if i.isalpha()==True:
            keep=keep+1
        else:
            pass
    print(keep)
def upper ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    keep=0
    for i in read1:
        if i.isupper()==True:
            keep=keep+1
        else:
            pass
    print(keep)
def lower ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    keep=0
    for i in read1:
        if i.islower()==True:
            keep=keep+1
        else:
            pass
    print(keep)
def brabra ():
    infile=open('essay.txt',"r")
    read1=infile.read()
    infile.close()
    keep=0
    for i in read1:
        if i=="." or i=="," or i=="/" or i == "(" or i==")" or i== ";":
            keep=keep+1
        else:
            pass
    print(keep)
def main ():
    line()
    sentense()
    word()
    letter()
    upper()
    lower()
    brabra()
main()
