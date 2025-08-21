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
import random

r = random.randint(1, 100) #randint : random int隨機整數
count = 0
while True:
	ans = input('猜數字: ')
	ans = int(ans)
	count += 1
	if ans == r:
		print('猜對了!')
		break
	else:
		if ans > r:
			print('猜的比答案大')
		else:
			print('猜得比答案小')

	print('這是你猜的第', count,'次')