with open('disco_no_id.txt', 'r') as file:
    # Чтение строк из файла и удаление символов новой строки
    disco_no_id = file.read().splitlines()

pref = ' - no id'

for login in disco_no_id:
    login = login.replace(pref,'')
    with open('disco_log.txt', 'a') as file:
        file.write(f'{login}\n')