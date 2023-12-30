import random
def password(n):
    letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*_+=|<>1234567890:"
    key="".join(random.choice(letters)for i in range(n))
    return key
n=int(input("enter the no of elements in password:"))
print("password:",password(n))
