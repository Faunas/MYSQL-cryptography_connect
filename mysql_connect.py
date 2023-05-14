from cryptography.fernet import Fernet
import MySQLdb
from create_stealth_key_in_temp import *

# Создаем объект шифрования на основе ключа
try:
    f = Fernet(key)
except Exception:
    os.remove("C:/temp/keycode.txt")
    print("Произошла ошибка. Выполняю сброс. Перезапустите программу.")
    quit()

# Выводим зашифрованную строку и ключ шифрования
print("Зашифрованная строка:",
      "gAAAAABkYNI-vxXqH1OrjDDqD916kEX1wUCmAahHzh7tCASdh1oAlALuqTd1DbtEt1KNKIslIdRDhimVbA7D4cPt_Mz7GExrK4kcN5JvNuMYi0iwG82-tv8MWLgOFbhtbrsucYzCl_VyIfL-Ukj7QzfVqT2X7BiCRk9kWC7tNj4reHEBplTj1iu1c8YduPK2lxjV_iJWdCbNj1EGHIAwg3YBrmJuoXGVbeaeI8LHUxcclRPVBnrJtGM=")
print("Ключ шифрования:", key.decode())
encrypted_string = b'gAAAAABkYNI-vxXqH1OrjDDqD916kEX1wUCmAahHzh7tCASdh1oAlALuqTd1DbtEt1KNKIslIdRDhimVbA7D4cPt_Mz7GExrK4kcN5JvNuMYi0iwG82-tv8MWLgOFbhtbrsucYzCl_VyIfL-Ukj7QzfVqT2X7BiCRk9kWC7tNj4reHEBplTj1iu1c8YduPK2lxjV_iJWdCbNj1EGHIAwg3YBrmJuoXGVbeaeI8LHUxcclRPVBnrJtGM='
# Расшифровываем строку
decrypted_string = f.decrypt(encrypted_string)

# Декодируем строку из байтов и преобразуем в словарь
MYSQLCONF = eval(decrypted_string.decode())

# Подключаемся к базе данных, используя расшифрованную строку
conn = MySQLdb.connect(
    host=MYSQLCONF['host'],
    user=MYSQLCONF['user'],
    password=MYSQLCONF['password'],
    db=MYSQLCONF['db'],
    charset=MYSQLCONF['charset'],
    autocommit=MYSQLCONF['autocommit'],
)


def test_connection():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `keys_users`')
    result = cursor.fetchall()
    cursor.close()
    return result


print(test_connection())
conn.close()
