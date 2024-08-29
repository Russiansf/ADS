# n = ''
# # with open("z_privatkey11-50.txt", "r") as f:
# # 	keys = [row.strip() for row in f]



# # for key in keys:
# # 	xkey = int(key,16)
# # 	zkey = xkey-n

# # 	f = open('zkeyprivat.py', 'a') #zkeyprivat.txt
# # 	f.write(f'{zkey}\n')
# # 	f.close()


    
# n = (input('Введи ключ: '))
# with open("zkeyprivat.txt", "r") as f:
# 	privat_keys = [row.strip() for row in f]

# for i, z_privat_key in enumerate(privat_keys):
# 	zkey = int(z_privat_key) + int(n)
# 	# zkey = z_privat_key + n
# 	privat_key = hex(int(zkey))            
# 	if z_privat_key[0] == '0':      
# 		privat_key = privat_key[:2] + '0' + privat_key[2:]
# 	else:
# 		privat_key

# 	# print(privat_key)

# print(type(privat_keys))
# print(privat_keys[0])