from lib import login, one, two, three, four, five, six, seven

input_account = input("請輸入帳號: ")
input_password = input("請輸入密碼: ")
if login(input_account, input_password) == 1:
    exit()

while (True):
    # 輸入帳號和密碼
    print("---------- 選單 ----------")
    print("0 / Enter 離開")
    print("1 建立資料庫與資料表")
    print("2 匯入資料")
    print("3 顯示所有紀錄")
    print("4 新增記錄")
    print("5 修改記錄")
    print("6 查詢指定手機")
    print("7 刪除所有記錄")
    print("--------------------------")
    choise = input("請輸入您的選擇 [0-7]: ")
    if choise == "0":
        print("")
        exit()
    if choise == "":
        print("")
        exit()
    if choise == "1":
        one()
    if choise == "2":
        two()
    if choise == "3":
        three()
    if choise == "4":
        four()
    if choise == "5":
        five()
    if choise == "6":
        six()
    if choise == "7":
        seven()
    print("")
