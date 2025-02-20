




try:
    user_num = int(input())
    div_num = int(input())
    
    result = user_num // div_num
    print(result)
    
except ZeroDivisionError:
    print(f"Zero Division Exception: integer division or modulo by zero")
    
except ValueError as e:  
    print(f"Input Exception: invalid literal for int() with base 10: '{e}'")