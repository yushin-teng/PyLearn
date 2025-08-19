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
age = input('請輸入年齡: ')
age = int(age)
if age >= 20 :
	print('去工作')
elif age <= 10 and age >= 5:
	print('小屁孩')
else:
	print('小小屁孩')