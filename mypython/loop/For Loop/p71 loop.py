from colorama import Back, Style,Fore

limits = int(input("Enter limits ="))

for i in range(1, limits+1):
    print(Fore.GREEN , i, end ="*" + Style.RESET_ALL)
