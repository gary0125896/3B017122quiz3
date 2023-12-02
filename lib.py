import json, sqlite3, os


def login(input_account: tuple, input_password: tuple) -> tuple:
    # 讀取 JSON 檔案
    with open("pass.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 檢查輸入是否正確
    login_successful = False
    for user_info in data:
        if user_info.get("帳號") == input_account and user_info.get("密碼") == input_password:
            login_successful = True
            break

    # 印出結果
    if login_successful:
        print("登入成功")
        return 0
    else:
        print("帳密錯誤，程式結束")
        return 1


def one():
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect("wanghong.db")

    # 創建一個游標
    cursor = conn.cursor()

    # 創建一個資料表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            "iid" INTEGER PRIMARY KEY AUTOINCREMENT,
            "mname" TEXT NOT NULL,
            "msex" TEXT NOT NULL,
            "mphone" TEXT NOT NULL
        )
    """)

    # 關閉連接
    conn.close()

    print("=>資料庫已建立")


def two():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        conn = sqlite3.connect("wanghong.db")
        cursor = conn.cursor()
        # 讀取 txt 檔案
        with open("members.txt", "r", encoding="utf-8") as file:
            # 逐行讀取並插入資料庫
            i = 0
            for line in file:
                data = line.strip().split(',')
                cursor.execute("INSERT INTO members (mname, msex, mphone) VALUES (?, ?, ?)", (data[0], data[1], data[2]))
                i = i + 1

        # 提交變更並關閉連接
        conn.commit()
        conn.close()
        print("=>異動{:^3}筆記錄".format(i))
    else:
        print("=>尚未建立資料庫")


def three():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        conn = sqlite3.connect("wanghong.db")
        cursor = conn.cursor()
    try:
        # 查詢 members 表的所有資料
        cursor.execute('SELECT * FROM members')
        result = cursor.fetchall()

        if not result:
            print("=>查無資料")
        else:
            # 列印標題行
            print("{:<10} {:<3} {:<15}".format("姓名", "性別", "電話號碼"))
            print("-" * 29)

            # 列印每一行資料
            for row in result:
                print("{:<10} {:<3} {:<15}".format(row[1], row[2], row[3]))
        conn.close()
    except Exception:
        print("=>查無資料")


def four():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        conn = sqlite3.connect("wanghong.db")
        cursor = conn.cursor()
        a = input("請輸入姓名: ")
        b = input("請輸入性別: ")
        c = input("請輸入手機: ")
        try:
            cursor.execute("INSERT INTO members (mname, msex, mphone) VALUES (?, ?, ?)", (a, b, c))
            # 提交變更並關閉連接
            conn.commit()
            conn.close()
        except Exception:
            print("=>請先建立資料表")
    else:
        print("=>請先建立資料庫")


def five():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        # 建立資料庫連接
        conn = sqlite3.connect("wanghong.db")
        cursor = conn.cursor()

        # 接收使用者輸入
        name_to_update = input("請輸入想修改記錄的姓名: ")
        # 查詢原資料
        cursor.execute("SELECT * FROM members WHERE mname=?", (name_to_update,))
        old_record = cursor.fetchone()

        if old_record:
            # 列印原資料
            print("\n原資料：")
            print_record(old_record)
            new_gender = input("請輸入要改變的性別: ")
            new_phone = input("請輸入要改變的手機: ")
            # 修改資料
            cursor.execute("UPDATE members SET msex=?, mphone=? WHERE mname=?",
                        (new_gender, new_phone, name_to_update))
            conn.commit()

            # 再次查詢修改後的資料
            cursor.execute("SELECT * FROM members WHERE mname=?",
                        (name_to_update,))
            new_record = cursor.fetchone()

            # 列印修改後的資料
            print("=>異動 1 筆記錄")
            print("\n修改後資料：")
            print_record(new_record)

        else:
            print("=>必須指定姓名才可修改記錄")

        # 關閉連接
        conn.close()
    else:
        print("=>請先建立資料庫")


def print_record(record):
    print(f"姓名：{record[1]}，性別：{record[2]}，手機：{record[3]}")


def six():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        # 建立資料庫連接
        conn = sqlite3.connect("wanghong.db")
        cursor = conn.cursor()

        # 接收使用者輸入
        phone_to_search = input("請輸入想查詢記錄的手機: ")

        # 查詢資料
        cursor.execute("SELECT * FROM members WHERE mphone=?", (phone_to_search,))
        result = cursor.fetchall()
        if not result:
            print("=>沒有這支手機")
        else:
            # 列印標題行
            print("{:<10} {:<3} {:<15}".format("姓名", "性別", "手機"))
            print("-" * 30)

            # 列印查詢結果
            for row in result:
                print("{:<10} {:<3} {:<15}".format(row[1], row[2], row[3]))

        # 關閉連接
        conn.close()
    else:
        print("=>請先建立資料庫")


def seven():
    db_file = "wanghong.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        print("=>已刪除所有資料。")
    else:
        print("=>找不到資料庫")
