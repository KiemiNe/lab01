while True:
    try:
        a = float(input())
        b = float(input())
        c = float(input())
    except: 
        print('пожалуйста, введите числа')
    else:
        D = b**2 - 4*a*c
        r = 0
        k = 0
        if a == 0: print('нет решений')
        else:
            if D < 0: print('нет решений')
            elif D == 0:
                r = (-b)/(2*a)
                print(r)
            else:
                k = (-b+(D**0.5))/(2*a)
                r = (-b-(D**0.5))/(2*a)
                print(r,k)

