class Account:
    def __init__(self,account,name,money):
        self.account = account
        self.name = name
        self.money = money
    
    def create_account(self):
        print("계좌개설을 완료했습니다.")
        #print('계좌 : '+self.account)
        #print('이름 : '+self.name)
        #print('잔액 : '+str(self.money))

    def input_money(self, input_money):
        #self.input_money = input_money
        self.money += input_money
        print(self.money)

    def output_money(self, output_money):
        #self.input_money = input_money
        self.money -= output_money
        print(self.money)

    def Account_inquiry(self):
        print('계좌정보 : '+ self.account+' / 이름 : '+self.name+' / 잔액 : '+str(self.money))