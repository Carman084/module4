def check_palindrom(word):
    a = word[::-1]
    if word.lower() == a.lower():
        return True
    else:
        return False 
print(check_palindrom('лепсспел'))
print(check_palindrom('Ок'))
