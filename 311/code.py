#12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz
#c=""
#for i in range(1,16):
#    if i%15==0 :
#        c=c+"FizzBuzz"
#    elif i%5 == 0:
#        c=c+"zz"
#    elif i%3 == 0:
#        c=c+"zz"
#    print(i,c.count("z"))
#
N=int(input())        
magick=[0,0,2,2,4,6,6,6,8,10,10,12,12,12,16]
print(N//15 * 16 + magick[(N-1)%15])
