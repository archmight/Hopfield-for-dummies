from work_with_matrix import mul_v, sum_m, fill_diagonal, mul_m

two = [1,1,1,1,     #1111
       -1,-1,-1,1,  #0001
       -1,1,1,-1,   #0110
       1,-1,-1,-1,  #1000
       1,1,1,1]     #1111

four = [-1,1,-1,1,  #0101
        1,-1,-1,1,  #1001
        1,1,1,1,    #1111
        -1,-1,-1,1, #0001
        -1,-1,-1,1] #0001

eight = [1,1,1,1,   #1111
         1,-1,-1,1, #1001
         1,1,1,1,   #1111
         1,-1,-1,1, #1001
         1,1,1,1]   #1111

spoiled_two = [1,1,-1,1,    #1101
               -1,-1,-1,1,  #0001
               -1,1,1,-1,   #0110
               1,-1,-1,-1,  #1000
               1,1,1,1]     #1111

spoiled_four = [-1,1,-1,1,  #0101
                1,-1,-1,1,  #1001
                1,1,1,1,    #1111
                -1,-1,-1,-1,#0000
                -1,-1,-1,1] #0001

spoiled_eight = [-1,-1,1,1, #0011
                 1,-1,-1,1, #1001
                 1,1,1,1,   #1111
                 1,-1,-1,1, #1001
                 1,1,1,1]   #1111

m_two = mul_v(two)
m_four = mul_v(four)
m_eight = mul_v(eight)

W = sum_m(sum_m(m_two,m_four),m_eight)
W = fill_diagonal(W)

print(W)

spoiled = spoiled_eight

while(True):
    spoiled = mul_m(W,spoiled)
    if(spoiled == two):
        print("it's two!!")
        break
    elif(spoiled == four):
        print("it's four!!")
        break
    elif(spoiled == eight):
        print("it's eight!!")
        break