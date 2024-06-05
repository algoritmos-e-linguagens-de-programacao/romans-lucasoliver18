num = input("Digite um valor até 3000: ")
i = len(num) - 1
o = int(num)

def int_to_roman(num):
    if o > 3000:
        return "ERROR"
    
    result = ""
    i = len(num) - 1
    
    while i >= 0:
        if i == 3:
            if num[len(num)-i-1] == '1':
                result += 'M'
            elif num[len(num)-i-1] == '2': 
                result += 'MM' 
            elif num[len(num)-i-1] == '3':
                result += 'MMM' 
            elif num[len(num)-i-1] == '0':
                result += ''
            i -= 1
        elif i == 2:    
            if num[len(num)-i-1] == '1':
                result += 'C'
            elif num[len(num)-i-1] == '2': 
                result += 'CC' 
            elif num[len(num)-i-1] == '3':
                result += 'CCC'
            elif num[len(num)-i-1] == '4':
                result += 'CD'
            elif num[len(num)-i-1] == '5':
                result += 'D'
            elif num[len(num)-i-1] == '6':
                result += 'DC'
            elif num[len(num)-i-1] == '7':
                result += 'DCC'
            elif num[len(num)-i-1] == '8':
                result += 'DCCC'
            elif num[len(num)-i-1] == '9':
                result += 'CM'
            elif num[len(num)-i-1] == '0':
                result += ''
            i -= 1
        elif i == 1:
            if num[len(num)-i-1] == '1':
                result += 'X'
            elif num[len(num)-i-1] == '2': 
                result += 'XX' 
            elif num[len(num)-i-1] == '3':
                result += 'XXX'
            elif num[len(num)-i-1] == '4':
                result += 'XL'
            elif num[len(num)-i-1] == '5':
                result += 'L'
            elif num[len(num)-i-1] == '6':
                result += 'LX'
            elif num[len(num)-i-1] == '7':
                result += 'LXX'
            elif num[len(num)-i-1] == '8':
                result += 'LXXX'
            elif num[len(num)-i-1] == '9':
                result += 'XC'
            elif num[len(num)-i-1] == '0':
                result += ''
            i -= 1
        elif i == 0:
            if num[len(num)-i-1] == '1':
                result += 'I'
            elif num[len(num)-i-1] == '2': 
                result += 'II'
            elif num[len(num)-i-1] == '3':
                result += 'III'
            elif num[len(num)-i-1] == '4':
                result += 'IV'
            elif num[len(num)-i-1] == '5':
                result += 'V'
            elif num[len(num)-i-1] == '6':
                result += 'VI'
            elif num[len(num)-i-1] == '7':
                result += 'VII'
            elif num[len(num)-i-1] == '8':
                result += 'VIII'
            elif num[len(num)-i-1] == '9':
                result += 'IX'
            elif num[len(num)-i-1] == '0':
                result += ''
            i -= 1
    
    return result

print(f"O numero em romano é {int_to_roman(num)}")

def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = roman_values[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

print("Agora: ")
roman_number = input("Digite um número romano: ")
inteiro_numero = roman_to_int(roman_number)
print(f"O numero {roman_number} em inteiro fica {inteiro_numero}")
