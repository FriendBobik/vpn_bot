import paramiko
import pyotp

# Установка параметров для подключения SSH
host = '95.214.11.40'
port = 22
username = 'root'
password = 'your_password'  # или используйте ключи для аутентификации

# Создание объекта SSH клиента
client = paramiko.SSHClient()

# Игнорирование проверки ключа хоста (для простоты, в реальном использовании это должно быть безопасно)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Генерация OTP
    totp = pyotp.TOTP('your_secret_key')  # Замените 'your_secret_key' на ваш секретный ключ
    otp = totp.now()

    # Подключение к серверу SSH с использованием OTP в качестве пароля
    client.connect(hostname=host, port=port, username=username, password=otp)

    # Выполнение команды на удаленном сервере
    stdin, stdout, stderr = client.exec_command('command_to_execute')
    
    # Получение вывода команды
    output = stdout.read().decode()
    print(output)

finally:
    # Закрытие соединения SSH
    client.close()
