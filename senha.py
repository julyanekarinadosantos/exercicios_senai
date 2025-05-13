from colorama import init,Fore
init(autoreset=True)


senha = 'julyxs@2022'
s=input('qual é a senha? ')
if s == senha:
    print(Fore.GREEN+'senha correta!')
else:
    print(Fore.RED+'senha incorreta')

