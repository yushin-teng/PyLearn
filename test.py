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


#讀取檔案 split
# import os	#operating system
# # 檢查檔案在不在系統
# products = []
# if os.path.isfile('products.txt'): #只給檔名是相對路徑的給定方式，也可以給絕對路徑去查找
# 	print('yeah!找到該檔案了!')
# 	with open('products.txt', 'r', encoding = 'utf-8') as f:
# 		for line in f:
# 			if '商品,價格' in line:
# 				continue	#繼續，跳至下一回繼續處理
# 			name, price = line.strip().split(',')
# 			products.append([name, price])
# 	print(products)
# else:
# 	print('shit!找不到該檔案')


# 記帳程式
# while True:
# 	name = input('請輸入商品名稱:')
# 	if name == 'q':
# 		break
# 	price = int(input('請輸入商品價格:'))
# 	# p = []	#小清單
# 	# p.append(name)
# 	# p.append(price)
# 	p = [name, price]
# 	products.append(p)
# # print(len(products))
# # print(products)
# print(products[0][1])
# for product in products:
# 	print(product[0], '的價格是', product[1])

# # 字串可以做運算合併: 'abc' + 'edf' = 'abcdef' ； 'abc' * 3 = 'abcabcabc'
# with open('products.txt', 'w', encoding = 'utf-8') as f:	#只有打開檔案而已
# 	f.write('商品,價格\n')	#加入開頭欄位名稱，encoding需確認是否正確(於打開檔案就要寫入想要的編法方式)
# 	for p in products:
# 		f.write(p[0] + ', ' + str(p[1]) + '\n')	#逐筆寫入資料

# Function函式

# def wash():	#功能實作 define
# 	print('加水')
# 	print('加洗衣精')
# 	print('旋轉')

# # wash()	#執行功能
# wash()	

# def say_hi():
# 	print('Hi!')

# say_hi()

#parameter
# def wash(dry = False, water_level = 8):	#功能實作 define
# 	print('加水', water_level,'分滿')
# 	print('加洗衣精')
# 	print('旋轉')
# 	if dry:
# 		print('烘衣')
# 	else:
# 		print('自己曬衣服')

# wash(True)	#dry = True
# wash(water_level = 10)	#dry = False

# def add(x = 0, y = 0):
# 	print(x + y)

# add(1, 2)
# add(5, 4)
# add()	#若參數有預設值，則可不需要輸入參數即可使用該函式
# add(5)	# x = 5, y = 預設值
# add(y = 5)	# x = 0, y = 5

# #function return
# def add(x=1, y=1):
# 	return x + y
# result = add(3, 4)
# print(result)

# def average(numbers):
# 	return sum(numbers) / len(numbers)

# print(average([1, 2, 3]))

# Refactor(程式重構)
# #              運算子          變數       清單        篩選條件
# # output = [(number - 1) for number in reference if num % 2 == 0]

# import os

# # 讀取檔案
# def read_file(filename):
# 		products = []
# 		with open(filename, 'r', encoding = 'utf-8') as f:
# 			for line in f:
# 				if '商品,價格' in line:
# 					continue
# 				name, price = line.strip().split(',')
# 				products.append([name, price])
# 			print(products)
# 		return products	

# # 使用者輸入
# def user_input(products):
# 	while True:
# 		name = input('輸入購買商品名稱: ')
# 		if name == 'q':
# 			break
# 		else:
# 			price = input('輸入購買商品價格:')
# 			price = int(price)
# 			products.append([name, price])
# 	print(products)
# 	return products

# # 印出所有購買紀錄
# def print_products(products):
# 	for p in products:
# 		print(p[0], '的價格是', p[1])

# # 寫入檔案
# def write_file(filename, products):
# 	with open(filename, 'w', encoding = 'utf-8') as f:
# 		f.write('商品,價格\n')
# 		for p in products:
# 			f.write(p[0] + ',' + str(p[1]) + '\n')

# def main():
# 	# 檢查檔案是否存在 (只使用一次，不會重複使用，所以不需要包成函式
# 	filename = 'products.txt'
# 	if os.path.isfile(filename):	#檢查檔案是否存在再執行
# 		print('購物清單存在')
# 		products = read_file('products.txt')
# 	else:
# 		print('該檔案不存在')

# 	products = user_input(products)
# 	print_products(products)
# 	write_file('products.txt', products)

# main()

# 對話紀錄-程式改寫
# import os

# def read_file(filename):
# 	lines = []
# 	with open(filename, 'r', encoding = 'utf-8-sig') as f:
# 		for line in f:
# 			lines.append(line.strip())
# 	return lines

# def convert(lines):
# 	new = []
# 	person = None
# 	for line in lines:
# 		if line == 'Allen':
# 			person = 'Allen'
# 			continue
# 		elif line == 'Tom':
# 			person = 'Tom'
# 			continue

# 		if person:	#person有值才執行
# 			new.append(person + ': ' + line)
# 	return new

# def write_file(datafile, lines):
# 	with open(datafile, 'w', encoding = 'utf-8-sig') as f:
# 		for line in lines:
# 			f.write(line + '\n')

# def main():
# 	filename = 'input.txt'
# 	if os.path.isfile(filename):
# 		print('Input檔案存在!')	
# 		lines = read_file(filename)
# 		# print(lines)	#\ufeff 這些是記事本偷存的有關於編碼的資料
# 		lines = convert(lines)
# 		print(lines)
# 		write_file('dataTest.txt', lines)

# main()

# 對話紀錄- Line對話格式改寫

# def read_fiel(filename):
# 	conv_rec = []
# 	with open(filename, 'r', encoding = 'utf-8-sig') as f:
# 		for line in f:
# 			conv_rec.append(line.strip())
# 	return conv_rec

# def convert(conv_rec):
# 	allen_word_cnt = 0
# 	allen_stick_count = 0
# 	allen_image_count = 0
# 	viki_word_cnt = 0
# 	viki_stick_count = 0
# 	viki_image_count = 0
# 	for rec in conv_rec:
# 		s = rec.split(' ')
# 		time = s[0]
# 		name = s[1]
# 		if name == 'Allen':
# 			# 清單分割功能n[開始值:結束值] (開始有包含，結束不包含)
# 			# n[:3] 可以拿到前三個
# 			# n[2:4] 可以拿到n[2], n[3]
# 			# n[-2:] 可以拿到最後兩個
# 			if s[2] == '貼圖':
# 				allen_stick_count += 1
# 			elif s[2] == '圖片':
# 				allen_image_count += 1
# 			else:
# 				for msg in s[2:]:	#2開始後的所有對話紀錄
# 					allen_word_cnt += len(msg)
# 		elif name == 'Viki':
# 			if s[2] == '貼圖':
# 				viki_stick_count += 1
# 			elif s[2] == '圖片':
# 				viki_image_count += 1
# 			else:
# 				for msg in s[2:]:
# 					viki_word_cnt += len(msg)

# 	print('allen說了', allen_word_cnt, '個字')
# 	print('allen傳了', allen_stick_count, '個貼圖')
# 	print('allen傳了', allen_image_count, '個圖片')

# 	print('viki說了', viki_word_cnt, '個字')	
# 	print('viki傳了', viki_stick_count, '個貼圖')
# 	print('viki傳了', viki_image_count, '個圖片')


# def main():
# 	line_rec = read_fiel('LINE-Viki.txt')

# 	convert(line_rec)

# main()

# 對話紀錄-3 清單分割法
# lines = []
# with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
# 	for line in f:
# 		lines.append(line.strip())

# for line in lines:
# 	s = line.split(' ')
# 	time = s[0][:5]
# 	name = s[0][5:]
# 	print('時間: ', time)
# 	print('名字: ', name)


# Dictionary字典
# a = []	#清單
# d = {}	#字典

# words = {
# 	# key      value值 : 字典的核心概念就是key-value pair key跟值的配對
# 	'ramen': '拉麵',
# 	'pasta': '義大利麵'
# }

# words['tea'] = '茶'	#增加新的key的寫法

# print(words['ramen'])
# print(words['tea'])
# print(words)

# 字典可以儲存屬性名稱
# p0 = {
# 	'name' : '麥香奶茶',
# 	'price': 15
# }

# p1 = {	
# 	'name' : '珍珠奶茶',
# 	'price': 60
# }

# drinks = [p0, p1]	#list, 清單裝字典
# print(drinks[0])
# print(drinks[0]['name'])
# print(drinks[0]['price'])

# 留言程式: 最常出現的字數

# import標準函式庫套件
# import time
# import progressbar	#進度條套件, 可以去pypi的網站抓取別人已寫好的套件，皆有說明使用套件方式，也可以在github上查找原始程式碼

# data = []
# count = 0
# # 在python裡所有的東西都是物件(object)
# # x = 5  x是一個物件，只是型別不同 (type, 此為int)，型別可以當物件使用
# #                  object 物件(ProgressBar)，物件第一個字一定是大寫，function第一個字一定是小寫!!!
# bar = progressbar.ProgressBar(max_value = 1000000)
# with open('reviews.txt', 'r', encoding = 'utf-8-sig') as f:
# 	for d in f:
# 		data.append(d)
# 		count += 1
# 		# bar的專屬功能update，update是ProgressBar這個類別裡的function
# 		bar.update(count)
# print('檔案讀取完了，有', len(data), '筆資料')
# # 計時開始
# start_time = time.time()
# word_cnt = {}
# for d in data:
# 	# words = d.split(' ')	
# 	words = d.split()	#split預設值就是空白鍵
# 	for word in words:	# 建立字典
# 		if word in word_cnt:
# 			word_cnt[word] += 1
# 		else:
# 			word_cnt[word] = 1	# 新增新的key(第一次遇到的word)

# for word in word_cnt:
# 	if word_cnt[word] > 1000000:
# 		print(word, word_cnt[word])

# print(len(word_cnt))
# print(word_cnt['Allen'])
# end_time = time.time()
# # 計時結束
# print('花了', end_time - start_time, 'sec')

# while True:
# 	word = input('請問你想查什麼字: ')
# 	if word == 'q':
# 		print('感謝使用查詢功能')
# 	break
# 	if word in word_cnt:
# 		print(word, '出現過',word_cnt[word], '次')
# 	else:
# 		print('此單字未出現在留言中')

#處理Excel套件:openpyxl
# from openpyxl import Workbook
# wb = Workbook()	#物件object，開頭大寫, type : Workbook

# # grab the active worksheet
# ws = wb.active

# # Data can be assigned directly to cells
# ws['A1'] = 42

# # Rows can also be appended
# ws.append([1, 2, 3])

# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()

# # Save the file
# wb.save("sample.xlsx")

#處理Word套件:python-docx
# from docx import Document
# from docx.shared import Inches

# document = Document()

# document.add_heading('Document Title', 0)

# p = document.add_paragraph('A plain paragraph having some ')
# p.add_run('bold').bold = True
# p.add_run(' and some ')
# p.add_run('italic.').italic = True

# document.add_heading('Heading, level 1', level=1)
# document.add_paragraph('Intense quote', style='Intense Quote')

# document.add_paragraph(
#     'first item in unordered list', style='List Bullet'
# )
# document.add_paragraph(
#     'first item in ordered list', style='List Number'
# )

# document.add_picture('Remove_impurities.png', width=Inches(1.25))

# records = (
#     (3, '101', 'Spam'),
#     (7, '422', 'Eggs'),
#     (4, '631', 'Spam, spam, eggs, and spam')
# )

# table = document.add_table(rows=1, cols=3)
# hdr_cells = table.rows[0].cells
# hdr_cells[0].text = 'Qty'
# hdr_cells[1].text = 'Id'
# hdr_cells[2].text = 'Desc'
# for qty, id, desc in records:
#     row_cells = table.add_row().cells
#     row_cells[0].text = str(qty)
#     row_cells[1].text = id
#     row_cells[2].text = desc

# document.add_page_break()

# document.save('demo.docx')

# 製作圖表: matplotlib
# import matplotlib.pyplot as plt 	#as 簡稱 plt，如果沒用簡稱 則都需要打全名才可以使用
# import numpy as np

# plt.style.use('_mpl-gallery')

# # make data
# x = np.linspace(0, 10, 100)
# y = 4 + 1 * np.sin(2 * x)
# x2 = np.linspace(0, 10, 25)
# y2 = 4 + 1 * np.sin(2 * x2)

# # plot
# fig, ax = plt.subplots()

# ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)
# ax.plot(x, y, linewidth=2.0)
# ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.ylabel('efficiency')
# plt.xlabel('times')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# species = ('Adelie', 'Chinstrap', 'Gentoo')
# sex_counts = {
#     'Male': np.array([73, 34, 61]),
#     'Female': np.array([73, 34, 58]),
# }
# width = 0.6  # the width of the bars: can also be len(x) sequence


# fig, ax = plt.subplots()
# bottom = np.zeros(3)

# for sex, sex_count in sex_counts.items():
#     p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
#     bottom += sex_count

#     ax.bar_label(p, label_type='center')

# ax.set_title('Number of penguins by sex')
# ax.legend()

# # plt.show()
# plt.savefig('test123.png')

# 寄送簡訊程式 : twilio註冊使用(下載其套件)

# 圖片處理 : pillow
from PIL import Image
import os

# image_file = Image.open("Remove_impurities.png")
# print(type(image_file))	#檢查使用的物件名稱
# image_file = image_file.convert('L')	#convert image to black and white, 可以用1或L
# image_file.save('testImg.png')


# for file in os.listdir('.'):	#list dir顯示此資料夾的清單， .是同階層
# 	if file.endswith('.png'):
# 		print(file)


# for file in os.listdir('origin_image'):	
# 	if file.endswith('.png'):
# 		# image_file = Image.open('origin_image/' + file)	# 需處理路徑問題，OS模組有路徑合併的模組，此寫法是手動寫
# 		image_file = Image.open(os.path.join('origin_image', file))	# OS路徑模組合併
# 		image_file = image_file.convert('L')	#convert image to black and white, 可以用1或L
# 		image_file.save(os.path.join('new_image', file[:-4]) + '_gray.png')	#可以不用包含.png ([:-4]倒數四個字串)；需處理路徑問題

# class類別
# 物件包含屬性(可用dir(物件)查詢
# self ? self-reference 

# class Student:	#class命名需大寫開頭
# 	def __init__(self, name, score):	# initialize初始化
# 		self.sleep_time = 8
# 		self.name = name
# 		self.score = score
# 		print('初始化程式')

# 	def do_hw(self, subject):
# 		print('快做作業' + subject)

# 	def study(self):
# 		print(self.name, '規劃讀書計畫')
# 		self.score += 5

# 	def sleep(self):
# 		print('I need to sleep', self.sleep_time, '小時')
# 		self.study()	# 如果要執行此class的function, 需使用self去call

# s1 = Student('YuShin', 100)	# 產生出一個物件
# s2 = Student('Jilin', 100)
# s1.do_hw('English')
# print(s1.score, s2.score)
# s1.study()
# s1.sleep()
# # print(dir(s1))
# print(s1.name, s2.name)
# print(s1.score, s2.score)

# students = [s1, s2]
# for s in students:
# 	print(s.name, '的分數是',s.score, '分')


# class Desk:
# 	def __init__(self, color, height):
# 		print('客製化桌子')
# 		self.color = color
# 		self.height = height
# 	def re_color(self, new_color):
# 		self.color = new_color

# d = Desk('brown','50')	# instantiation 實體化
# print(d.color)
# d.re_color('red')
# print(d.color)

# class YoutubeDownLoader:	# c3套組內的一個模組
# 	def __init__(self):
# 		print('我誕生了')

# 	def download_single_vedio(self, url):	# URL, Uniform Resource Locator 統一資源定位符號 (即網址)
# 		print('downloading...', url)

# 	def download_multiple_vedios(self, urls):
# 		for url in urls:
# 			self.download_single_vedio(url)

# from c3 import YoutubeDownLoader	#可以從套組中使用其中一個模組

# ytd = YoutubeDownLoader()
# ytd.download_single_vedio('http://youtube.com/XXXXXXX')

# class Player:
# 	def __init__(self, name):
# 		self.name = name	
# 		self.hp = 100
# 		self.ap = 2
# 		self.level = 1
# 		self.defence = 1

# 	def attack(self, target):	# method
# 		print(self.name, '死纏爛打', target.name)	# 此寫法target需有name成員才可以作為參數使用，若亂引入則程式會當掉
# 		target.hp = target.hp - (self.ap - target.defence)
# 		print(target.hp, '血量')

# p1 = Player('YuShin')
# p2 = Player('JiLin')
# players = [p1, p2]

# for p in players:
# 	print('玩家名稱:',p.name, '等級:',p.level, '血量: ',p.hp, '攻擊力: ',p.ap)

# p1.attack(p2)
# print(p2.hp)


# import lesson
# class Db:	#物件
# 	def __init__(self):
# 		self.connect()

# 	def connect(self):
# 		print('實際建立連線')

# 	def insert_data(self):
# 		print('上傳資料')

# def addrs:	#function
# 	pass

# x = 5

# # 若Db再不同的檔案程式碼db，則採以下import
# from db import Db, addrs, x		# 同目錄載入方式
# from 檔案名稱.db import Db		#不同目錄載入方式，母資料夾要引用子資料夾中的檔案
# from ..db import Db		#子資料夾要引用母資料夾的檔案 不建議這樣使用， python不允許這樣使用(有特定方式可以處理，但此設計不好)

# class Tool:	#在tool.py
# 	def __init__(self):
# 		print('test first')
# 		self.db = Db()

# 	def upload(self):
# 		self.db.insert_data()

# line聊天機器人 : line-bot-sdk
# flask, django 架設伺服器或寫網站的套件，下列程式碼為網頁程式碼
from flask import Flask, request, abort

from linebot.v3 import (	# webhook Webhook = Web + Hook（鉤子）它是一種 由伺服器主動推送資料給你的機制，通常透過 HTTP POST 請求 將即時事件傳送到你指定的網址（endpoint）。 所以需要致能使用
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

configuration = Configuration(access_token='YOUR_CHANNEL_ACCESS_TOKEN')		# 提供必須金鑰 (此為line聊天機器人官網提供予使用者的金鑰)，證明你為此帳戶的擁有者
handler = WebhookHandler('YOUR_CHANNEL_SECRET')		# 提供密碼


@app.route("/callback", methods=['POST'])	# 將訊息轉載到'指定的網址' + /callback 則執行此段程式
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )


# 在 Python 中，每個模組（.py 檔案）都有一個內建變數 __name__。
# 如果這個檔案是 被直接執行（例如 python myfile.py），那麼 __name__ 的值會是 "__main__"。
# 如果這個檔案是 被其他程式匯入（例如 import myfile），那麼 __name__ 的值會是這個檔案的檔名（不含 .py）。
if __name__ == "__main__":		# 如果app.py是直接被執行而不是被載入的話，才執行此內容 (不希望import就執行) 「只有當這個檔案是直接執行時，才會執行下面的程式碼。」
    app.run()



# line聊天機器人 : 架設雲端平台(程式在雲端執行) HEROKU PaaS（Platform as a Service，平台即服務）
# git push origin master
# git push heroku master		# heroku目前要收費，所以只寫範例code

# remote / local #遠端
# heroku git:remote -a line-bot-0402	# "line-bot-0402此為heroku的專案名稱，須讓git知道對應在heroku的專案名稱"

# 需要建立一個procfile.py，讓heroku知道要怎麼運行，內容只有: web gunicorn app:app
# 須建立requirements.txt, 讓營運者知道此專案用到那些套件: line-bot-sdk==1.2.3(version), gunicorn==2.4.1, flask
# 上面的requirements內的套件可以透過pip更新版本pip install --upgrade <套件名稱> 或 pip install -U <套件名稱>
# 可透過pip freeze > "requirements.txt"儲存目前使用套件的資訊
# git add . 將資料夾內的檔案都staged
# NLP natural language processing 自然語言程序 (True AI)
