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
        6. 종료하기
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
        acc_delete = input('삭제하실 계좌번호를 입력해주세요: ')

        if acc_delete not in account_dict:
            print('존재하지 않는 계좌번호입니다.')
            continue

        del account_dict[acc_delete]
        print('계좌가 삭제되었습니다.')

    elif select == '6':
        break
    
    else :
        print("1~6범위 내의 숫자를 선택하세요")
        continue


