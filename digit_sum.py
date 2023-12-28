def digit_sum(num):
    try:
        sum = 0
        while num>0:
            rem = num%10
            sum+=rem
            num//=10
        return sum
    except:
        return 0

    



