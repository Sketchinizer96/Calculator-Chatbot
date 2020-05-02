import time
print(' ========= CALCULATOR CHAT BOT ========= ')
time.sleep(1)
print('Basic operations for you while we chat')
time.sleep(1)
print('My Name is Jignesh. I and my sister Help here for people to get their work done.')
time.sleep(2)
print('Please Choose with who would you like to talk: [ Jiggna / Jignesh]')
time.sleep(2)
chat_bot_name: list = ["Jiggna", "Jignesh"]
cbi: int = input("Press 0 for Jiggna  and 1 for Jignesh : ")
if int(cbi) == 0:
    cbn = chat_bot_name[0]
else:
    cbn = chat_bot_name[1]
print('*' * 100)
exit_1: str = 'No'
print(f'{cbn} : Hello I am {cbn} a Calculator Chat bot')
print(f'{cbn} : I can do basic operations for you while we chat')
time.sleep(1)
user_name = input(f'{cbn} : Please enter your name as it will be easy for us to talk :\t')
time.sleep(1)
username_a: list = user_name.split(" ", 1)
username = username_a[0]
print(f'{cbn} : Hello {username}, lets get started !')
time.sleep(1)
print(f'{cbn} : I can perform basic arithematic operations as you instruct me. \n'
          f'{cbn} : For Example : to perform addition type "Add 4" or "add 4" or "+ 4"\n'
          f'{cbn} : Please say done to see the result')
time.sleep(3)
while 'Yes' != exit_1:
    print(f'{cbn} : Please provide me the first operation !\t')
    time.sleep(1)
    operation_1 = input(f'{username} : ')
    operation_2: list = operation_1.split(" ")
    result = 0
    if str(operation_2[0]).isalpha() and str(operation_2[2]).isalpha():
        print(
            f'{cbn} : Cannot add alphabets it looks like {operation_2[0]}{operation_2[2]}. Its not an arithematic operation.\n'
            f'{cbn} : Please provide numbers !')

    result = int(operation_2[0]) + int(operation_2[2])
    print(f'{cbn} : if you want to do more you can keep giving me inputs or else say "done" to see the result.')
    operation_3 = 'not done'
    while str(operation_3) != 'done':
        operation_3 = input(f'{username} : ')
        operation_4: list = operation_3.split(" ")
        if str(operation_4[0]) in ['Add', 'ADD', 'add', '+']:
            result = result + int(operation_4[1])

        if str(operation_4[0]) in ['Sub', 'SUB', 'sub', '-']:
            result = result - int(operation_4[1])

        if str(operation_4[0]) in ['Mul', 'MUL', 'mul', '*']:
            result = result * int(operation_4[1])

        if str(operation_4[0]) in ['Div', 'DIV', 'div', '/']:
            if int(operation_4[1]) < result:
                result = result / int(operation_4[1])

            else:
                print('Please enter a smaller value : Arithematic Error')

    print(f'{cbn} : This is the Result : ' + str(float(result)))
    time.sleep(2)
    exit_1 = input('Do you want  to End this Chat (Yes/No):  ')
print(f'Thank you {username} was Nice Talking to you, Hope to Meet You Soon ')
