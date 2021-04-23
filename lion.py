from Account import *

# Key : 계좌번호, Value : account 객체
account_dict = dict()

while True :
    print(
        """
        ========Bank Menu=========
        1. 계좌개설
        2. 입금하기
        3. 출금하기
        4. 전체조회
        5. 계좌삭제
        6. 계좌이체
        7. 종료하기
        """
    )
    select = input()
    if select == '1':
        print("=======계좌개설========")
        acc = input("계좌번호 : ")
        name = input("이름 : ")
        money = input("예금 : ")

        #계좌번호 및 금액 입력 시 예외처리
        try :
            int(acc)
            float(money)
        except :
            print("계좌번호와 금액은 반드시 숫자형으로 입력해주세요.")
            continue

        if acc in account_dict:
            print("이미 해당 계좌가 존재합니다.")
            continue
        
        #Account class 객체 생성
        account = Account(acc, name, float(money))
        account.create_account()
        #dict에 계좌번호와 객체 매칭해서 담기
        account_dict[acc] = account

    elif select == '2':
        acc_for_input = input("입금하실 계좌번호를 입력해주세요 : ")

        if acc_for_input not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue
        
        #입금 전 계좌 상태 출력
        account_dict[acc_for_input].Account_inquiry()

        account_for_input = account_dict[acc_for_input]
        money_for_input = input("입금하실 금액을 입력해주세요 : ")

        #입금 금액 예외처리(only 숫자형만 가능)
        try :
            float(money_for_input)
        except :
            print("입금 금액은 반드시 숫자형으로 입력해주세요.")
            continue

        #입금
        account_for_input.input_money(float(money_for_input))

        #입금 후 계좌 상태 출력
        account_dict[acc_for_input].Account_inquiry()
    
    elif select == '3':
        acc_for_output = input("출금하실 계좌번호를 입력해주세요 : ")
        if acc_for_output not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue

        #출금 전 계좌 상태 출력
        account_dict[acc_for_output].Account_inquiry()

        account_for_output = account_dict[acc_for_output]
        money_for_output = input("출금하실 금액을 입력해주세요 : ")

        #입금 금액 예외처리(only 숫자형만 가능)
        try :
            float(money_for_output)
        except :
            print("출금 금액은 반드시 숫자형으로 입력해주세요.")
            continue

        account_for_output.output_money(float(money_for_output))

        #출금 후 계좌 상태 출력
        account_dict[acc_for_output].Account_inquiry()

    elif select == '4':
        for i in account_dict:
            account_dict[i].Account_inquiry()

    elif select == '5':
        acc_for_delete = input("삭제하실 계좌번호를 입력해주세요.")

        if acc_for_delete not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue

        del account_dict[acc_for_delete]

    elif select == '6':
        my_acc = input("본인 계좌를 입력해주세요.")
        opponent_acc = input("이체할 계좌를 입력해주세요.")
        money_for_transfer = input("이체할 금액을 입력해주세요.")

        if my_acc not in account_dict or opponent_acc not in account_dict:
            print("존재하지 않는 계좌입니다.")
            continue
        
        #이체 금액 예외처리(only 숫자형만 가능)
        try :
            float(money_for_transfer)
        except :
            print("이체 금액은 반드시 숫자형으로 입력해주세요.")
            continue

        account_for_output = account_dict[my_acc]
        account_for_input = account_dict[opponent_acc]


        #이체 전 본인 계좌 출력
        account_dict[my_acc].Account_inquiry()

        #이체금액이 잔액보다 크거나 같다면 이체 금액만큼 상대 계좌에다 입금
        if(account_for_output.money>=float(money_for_transfer)) :
            account_for_input.input_money(float(money_for_transfer))
            print("이체가 완료되었습니다.")

        #이체 금액만큼 본인 계좌에서 출금
        account_for_output.output_money(float(money_for_transfer))

        #이체 후 본인 계좌 출력
        
        account_dict[my_acc].Account_inquiry()


    elif select == '7':
        break

    else :
        print("1~7범위 내의 숫자를 선택하세요")
        continue


