
def num_ways(data, result="", n=0):
    ## BASE CASE
    if n == len(data):
        print(result)
        return
    try:
        if int(data[n])<1:
            raise Exception("No Letter Maps to Null")
        ## TWO POSSIBLE NODE -- either one or two digits to letter
        num_ways(data, result+chr(int(data[n])+0x40), n+1) ##0x40 maps 64 -> 1 + 64 = A
        if int(data[n:n+2])<=0x1a: ##26 -> alphabet -- checks if current two digits are in range of 26
            num_ways(data, result+chr(int(data[n:n+2])+0x40), n+2)
    except Exception as e:
        return

#------------------------------------------------------#

num_ways(input("Enter Various Digits Except Null: "))
