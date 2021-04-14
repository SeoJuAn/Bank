from Account import *

account_dict = dict()

while True :
    print(
        """
        ========Bank Menu=========
        1. 계좌개설
        2. 입금하기
        3. 출금하기
        4. 전체조회
        5. 종료하기
        """
    )
    select = input()
    if select == '1':
        print("=======계좌개설========")
        acc = input("계좌번호 : ")
        name = input("이름 : ")
        money = input("예금 : ")

        if acc in account_dict:
            print("이미 해당 계좌가 존재합니다.")
            continue

        account = Account(acc, name, float(money))
        account.create_account()
        account_dict[acc] = account

    elif select == '2':
        acc_for_input = input("입금하실 계좌번호를 입력해주세요 : ")
        if acc_for_input not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue

        account_for_input = account_dict[acc_for_input]
        money_for_input = input("입금하실 금액을 입력해주세요 : ")
        account_for_input.input_money(float(money_for_input))
    
    elif select == '3':
        acc_for_output = input("출금하실 계좌번호를 입력해주세요 : ")
        if acc_for_output not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue

        account_for_output = account_dict[acc_for_output]
        money_for_output = input("입금하실 금액을 입력해주세요 : ")
        account_for_output.output_money(float(money_for_output))


    elif select == '4':
        for i in account_dict:
            account_dict[i].Account_inquiry()

    elif select == '5':
        break
    else :
        "1~5범위 내의 숫자를 선택하세요"
        continue


