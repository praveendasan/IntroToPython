#function should define starting of program
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_Name = input('Enter the first name')
print(f'your initials are {get_initial(first_Name)}')
 