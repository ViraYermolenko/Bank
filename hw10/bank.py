class Bank:

    def __init__(self):
        self.client = 'stranger'
        self.put_some_money = 0
        self.take_some_money = 0
        self.acc_balance = 0

    def welcome(self):
        ask_name = input('\nWelcome in Python Bank! What is your name?   ')
        self.client = ask_name
        if ask_name:
            ask_open_acc = int(input('''\nHello,{}! Do you want to open an account in the Python Bank? 
                     YES push "1"; NO push "0"; -->>   '''.format(self.client)))
            if ask_open_acc == 1:
                print('\nGreat! {}, you has just opened a new account in the Python Bank'.format(self.client))
                self.first_choice()
            else:
                return quit(print("{}, we're glad to see you in the Python Bank".format(self.client)))
        else:
            return quit(print("We're glad to see you, {}, into our Bank".format(self.client)))

    def first_choice(self):
        res = int(input('''\nDo you want to put money into your new account? 
         YES push "1"; NO push "0"; -->>   '''))
        if res == 1:
            self.put_money()
            self.operation_with_money(self.put_some_money)
        elif res == 0:
            return print("\n{} decided just open new account and do nothing with it today".format(self.client))

    def put_money(self):
        put_some_money = int(input('\nHow many money do you want to put? '))
        print('\n{} put {} dollars into his account in our Bank'.format(self.client, put_some_money))
        self.acc_balance += put_some_money
        return self.acc_balance

    def operation_with_money(self, acc_balance):
        took_money = int(input('''\nDo you want to take some money or close your account?
For doing nothing push "0"
For putting more money to your account push "1"
For taking some money from your account push "2"
For closing yor account push "3" 
-->>  '''))
        if took_money == 0:
            return quit(print("\n{} decided just open new account and do nothing with it today".format(self.client)))
        elif took_money == 1:
            self.put_money()
            self.operation_with_money()
        elif took_money == 2:
            self.check_acc()
            self.operation_with_money()
        elif took_money == 3:
            self.close_account()

    def check_acc(self):
        take_some_money = int(input('\nHow many money do you want to take?   '))
        if take_some_money <= self.acc_balance:
            self.take_money(take_some_money)
            self.acc_balance -= self.take_some_money
            return self.acc_balance
        else:
            other_check = int(input(print('''You doesn't have enough money to take. 
Your balance is: {} dollars. Do you want to take less?
    YES push "1"
    NO push "0" 
    -->>  '''.format(self.put_some_money))))
            if other_check == 1:
                self.check_acc()
        return quit(print("We're glad to see you, {}, into our Bank".format(self.client)))

    def take_money(self, take_some_money):
        print('\n{} take {} dollars from his/her account in our Bank'.format(self.client, take_some_money))
        print('\nYour balance is {} dollars'.format(self.acc_balance))
        return self.operation_with_money()

    def close_account(self):
        return quit(print('''{}, you decided to close your account.
Took your {} dollars and your certificate of account closure.'''.format(self.client, self.take_some_money)))


client1 = Bank()
client1.welcome()

