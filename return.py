s_username="VBF"
s_pwrd=2004

uaname= input("Enter the User Name: ")
passpword= int(input("Enter the Password: "))

def validate():
    if(s_username==uaname) and (s_pwrd==passpword):
        return "True"
    else:
        return "False"
    
print(validate())