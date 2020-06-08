def is_armstrong_number(number):
    digits = list(str(number))
    TotalDig = len(digits)
    sumaT, i = 0, 0
    
    for i in range (TotalDig):
        sumaT += int(digits[i]) ** TotalDig
        
    if sumaT == number:
        return True
    else:
        return False