import sys 
import getopt

opts,args = getopt.getopt(sys.argv[1:],'f:m:',['filename','message'])


print(opts)
print(args)


# python writer2.py -f test.txt -m Hello\ World
# [('-f', 'test.txt'), ('-m', 'Hello\\')]
# ['World']



# python writer2.py  -m Hello -f this.txt  
# [('-m', 'Hello'), ('-f', 'this.txt')]
# []
