from colorama import init, Fore
def print_name(name, force_uppercass=True):
    if force_uppercass:
        temp = name[0:len(name)].upper()
        print(Fore.GREEN + 'go green')
    else:
        temp = name[0:len(name)].lower()
        print(Fore.RED +'go red')
    print(temp)
