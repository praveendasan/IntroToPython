def get_initial(name):
    k = name[len(name)-1:len(name)].upper()
    return k

firstName = input('enter your first name: ')
lastName = input('enter your last name: ')

print(f'Initial are: {get_initial(firstName)+ get_initial(lastName)}')