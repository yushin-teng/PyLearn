#if函數  python是用空格或tab當括弧，且不能混用
# rain = input('今天有沒有下雨: ')
# if rain == '有':
# 	print('撐傘出門')
# 	print('想淋雨就出門')

#casting 型別轉換
# age = input('請輸入年齡: ')
# age = int(age)
# if age >= 20 :
# 	print('擁有投票資格')


#溫度轉換攻勢
# Cdeg = input('請輸入攝氏溫度: ')
# Cdeg = float(Cdeg)
# Fdeg = Cdeg * 9 / 5 + 32
# print('現在華氏溫度為', Fdeg, 'F')

#python else語句
# age = input('請輸入年齡: ')
# age = int(age)
# if age >= 20 :
# 	print('擁有投票資格')
# else:
# 	print('回家')


#python else if(elif)語句
# age = input('請輸入年齡: ')
# age = int(age)
# if age >= 20 :
# 	print('去工作')
# elif age <= 10 and age >= 5:
# 	print('小屁孩')
# else:
# 	print('小小屁孩')

#loop迴圈 while迴圈
# x = input('請輸入任意數字: ')
# x = int(x)
# while x < 10:
# 	print('x小於10!')
# 	print('沒有跳出邏輯')
# 	x = x + 1
# print('跳出loop')

#while true迴圈
# while True:
# 	print('True一定要寫break')
# 	break #離開迴圈
# print('跳脫迴圈')

# while True:
# 	mode = input('請輸入遊戲模式: ')
# 	if mode == 'q':
# 		print('遊戲模式一')
# 		break
# 	elif mode == '1':
# 		print('遊戲模式一')
# 		break
# 	elif mode == '2':
# 		print('遊戲模式二')
# 		break
# 	else:
# 		print('只能輸入1/2/q')

#密碼重試程式
# Max_of_Login = 2  #初版
# password = input('請輸入您的密碼: ')
# user_password = 'a123456'
# Max_of_Login = 3  #密碼輸入上限

# while True:
# 	if password == user_password:
# 		print(登入成功)	#跳出迴圈
# 		break
# 	else:
		# if Max_of_Login <= 0 :
		# 	print('登入次數超過3次，帳戶鎖定')
		# 	break
		# elif Max_of_Login == 2 :			
		# 	print('密碼錯誤，剩餘',Max_of_Login,'次機會')
		# 	Max_of_Login = Max_of_Login - 1
		# elif Max_of_Login == 1 :			
		# 	print('密碼錯誤，剩餘',Max_of_Login,'次機會')
		# 	Max_of_Login = Max_of_Login - 1 

		#modify1
		# Max_of_Login = Max_of_Login - 1 
		# if Max_of_Login == 0:
		# 	print('登入次數超過3次，帳戶鎖定')
		# 	break
		# else:
		# 	print('密碼錯誤，剩餘',Max_of_Login,'次機會')
		
		#modify2
		# Max_of_Login = Max_of_Login - 1 
		# print('密碼錯誤，剩餘',Max_of_Login,'次機會')				
		# if Max_of_Login == 0:
		# 	print('登入次數超過3次，帳戶鎖定')
		# 	break

#不可寫while true的寫法

# while Max_of_Login > 0:
# 	Max_of_Login = Max_of_Login - 1	
# 	password = input('請輸入您的密碼: ')	
# 	if password == user_password:
# 		print('登入成功')
# 		break
# 	else:	
# 		if Max_of_Login == 0:
# 			print('輸入錯誤3次，帳戶鎖定')
# 		else:
# 			print('密碼錯誤，剩餘',Max_of_Login,'次機會')	

#import 載入已實作程式
# import random

# start_num = input('請決定隨機數字起始值: ')
# start_num = int(start_num)
# end_num = input('請決定隨機數字結束值: ')
# end_num = int(end_num)

# r = random.randint(1, 100) #randint : random int隨機整數
# count = 0
# while True:
# 	ans = input('猜數字: ')
# 	ans = int(ans)
# 	count += 1
# 	if ans == r:
# 		print('猜對了!')
# 		print('這是你猜的第', count,'次')
# 		break
# 	else:
# 		if ans > r:
# 			print('猜的比答案大')
# 		else:
# 			print('猜得比答案小')

# 	print('這是你猜的第', count,'次')

# List清單 data type: int、float、bool、str、list(data structure)

# a = ['Toyota', 'Honda'] #空清單
# print(a)
# print(a[0]) #index 0 , Toyota
# print(a[1]) #index 1

# a.append('Audi') #append 新增清單項目
# print(a)
# print(len(a)) #清單長度

# print('Audi' in a) #是非題 True or False
# print('Benz' in a)

#for loop

# cars = ['Toyota', 'Honda']

# for car in cars:	#car暫時變數僅給for迴圈使用
# 	print(car)

# names = ['Allen', 'Tom', 'Jack']
# for name in names:
# 	print(name)

#字串當清單
# car = 'Audi'
# # ['A', 'u', 'd', 'i']
# for member in car:
# 	print(member)
# print(len(car))
# print('A' in car)
# print('Ai' in car)

#讀取檔案
# r = read , w = write, as f 當作f(自行取變數)
# open是打開檔案
# with python獨有功能，會自動close開啟過的檔案，必須要寫，否則開啟檔案未關閉的話
# 會造成檔案損毀
# data = []
# with open('food.txt', 'r') as f:	
# 	for line in f:
# 		print(line)
# 		# data.append(line)
# 		data.append(line.strip())	#strip 清除換行\n，只能對字串操作

# print(data)
# print(data[0])

# 留言分析程式
# data = []
# # count = 0
# with open('reviews.txt', 'r') as f:
# 	for line in f:
# 		data.append(line)
# 		if len(data) % 1000 == 0:
# 			print(len(data))
# print('檔案讀取完成, 總共有:', len(data), '筆資料')
# # print(data[0])	#印出第一筆資料
# # print('--------------------------')
# # print(data[1])
# Sum_len = 0
# for d in data:
# 	Sum_len += len(d)
# print('留言平均長度為', Sum_len/len(data))

# #清單篩選
# new = []
# length_max = 100
# for d in data:
# 	if len(d) < length_max:
# 		new.append(d)
# print('一共有', len(new), '長度小於100')
# print(new[0])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('包含good字眼的留言有', len(good), '筆資料')
# print(good[0])

# good_best = []
# good_best = [d for d in data if 'good' in d]

# print('包含good字眼的留言有', len(good_best), '筆資料')

# #              運算子          變數       清單        篩選條件
# # output = [(number - 1) for number in reference if num % 2 == 0]

# bad = ['bad' in d for d in data]
# print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)
# print(bad)	

# Range範圍
# python內建功能 : 清單產生器

# import random
# range(5)  # [0, 1, 2, 3, 4]
# range(3)  # [0, 1, 2]

# for i in range(6):
# 	r = random.randint(1, 49)
# 	print('這是第',i + 1 ,'次產生隨機數:', r)

# range(2, 5) # [2, 3, 4]
# range(8, 10) # [8, 9]
# range(2, 10, 3) # [2, 5, 8]
# range(3, 8, 2) # [3, 5, 7]
# range(10, 3, -2) # [10, 8, 6, 4]

# 記帳程式
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = int(input('請輸入商品價格:'))
	# p = []	#小清單
	# p.append(name)
	# p.append(price)
	p = [name, price]
	products.append(p)
# print(len(products))
# print(products)
print(products[0][1])
for product in products:
	print(product[0], '的價格是', product[1])

# 字串可以做運算合併: 'abc' + 'edf' = 'abcdef' ； 'abc' * 3 = 'abcabcabc'
with open('products.txt', 'w', encoding = 'utf-8') as f:	#只有打開檔案而已
	f.write('商品,價格\n')	#加入開頭欄位名稱，encoding需確認是否正確(於打開檔案就要寫入想要的編法方式)
	for p in products:
		f.write(p[0] + ', ' + str(p[1]) + '\n')	#逐筆寫入資料

