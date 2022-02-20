from colorama import Fore

logo = '''
██╗░░██╗██╗░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██║░░██║██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
███████║██║██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██╔══██║██║██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░░██║██║╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
'''
print(Fore.GREEN + logo)

print(Fore.GREEN +'''
                             
- - - - -Welcome to HiCalculator! - - - -
1) Addition                                                      
2) Subtraction 
3) Muliplication 
4) Division 
5) Calculate the nth term of an arithmetic sequence 
6) Generate Time Table of a number
7) Credits ''')




choice = input(Fore.GREEN + 'Please choose a option: ')


def credits():
 print(Fore.GREEN + 'Made by: HiPapi! January 2022')



if choice == "1":
    num1 = int(input(Fore.GREEN + 'What is your first number?:'))
    num2 = int(input(Fore.GREEN + 'What is your second number?:'))
    result = num1+num2 #adds the numbers together
    print(Fore.GREEN + 'Your answer is:',result)
    


elif choice == "2":
    num1 = int(input(Fore.GREEN + 'What is your first number?:'))
    num2 = int(input(Fore.GREEN + 'What is your second number?:'))
    result = num1-num2
    print(Fore.GREEN + 'Your answer is:',result)
    


elif choice == "3":
    num1 = int(input(Fore.GREEN + 'What is your first number?:'))
    num2 = int(input(Fore.GREEN + 'What is your second number?:'))
    result = num1*num2
    print(Fore.GREEN + 'Your answer is:',result)
    

elif choice == "4":
    num1 = int(input(Fore.GREEN + 'What is your first number?:'))
    num2 = int(input(Fore.GREEN + 'What is your second number?:'))
    result = num1/num2
    print(Fore.GREEN + 'Your answer is:',result)    

elif choice == "5":
    termtotermrule = int(input(Fore.GREEN + 'What is your term to term rule on your arithmetic sequence?:'))
    termrule = input(Fore.GREEN + 'Is your number + or - USE THESE SIGNS!:')
    multiple = int(input(Fore.GREEN + 'Write the number next to n for example 3?:'))
    nth = int(input(Fore.GREEN + 'Write the term you wanna find:'))
    result = multiple*nth,termrule,termtotermrule
    print(Fore.GREEN + 'Your answer is:',result)
    

elif choice == "6":
    num1 = int(input(Fore.GREEN + 'Choose the number you wanna find the time table of:'))
    for loop in range(12):
       answer = num1*loop
       print(Fore.GREEN + num1, 'X', loop, '=', answer,)
       

elif choice == "7":
   credits()
   

   #to do
   #add options for more math stuff
   #add gradient