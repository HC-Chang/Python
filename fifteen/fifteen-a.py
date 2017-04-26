# fifteen
# 移磚塊

import sys
import os     

# 最大維度與最小維度
dim_min = 3
dim_max = 9
board = []

# 維度
dimensions = 0

# 清除畫面
def clear():
	os.system("cls")
	return 
	
# 初始化
def init():	
	for i in range(0,dimensions*dimensions,1):
		board.append(dimensions*dimensions-i-1)
	
	if(dimensions %2 == 0):
		temp = board[dimensions*dimensions-2]
		board[dimensions*dimensions-2] = board[dimensions*dimensions-3]
		board[dimensions*dimensions-3] = temp
	
	return
	
# 繪圖
def draw():
	for i in range(dimensions):
		for j in range(dimensions):
			if(not board[i*dimensions+j] == 0):
				print(board[i*dimensions+j],end="\t")
			else:
				print("-",end = "\t")
		print("\n")

# 是否可以移動
def move(tile):
	
	# 設定行列
	row = 0
	col = 0
	for i in range(0,dimensions*dimensions,1):
		if(board[i] == 0):
			row = int(i/dimensions)
			col = i%dimensions

	# 判斷行的範圍
	if(row-1 < 0):
		if(board[(row+1)*dimensions+(col)] == tile):
			board[(row+1)*dimensions+(col)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1

	elif(row+1 == dimensions):
		if(board[(row-1)*dimensions+(col)] == tile):
			board[(row-1)*dimensions+(col)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1

	# 上下自由移動
	else:
		if(board[(row+1)*dimensions+(col)] == tile):
			board[(row+1)*dimensions+(col)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
		elif(board[(row-1)*dimensions+(col)] == tile):
			board[(row-1)*dimensions+(col)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
	
	# 判斷列的範圍
	if(col-1 < 0):
		if(board[(row)*dimensions+(col+1)] == tile):
			board[(row)*dimensions+(col+1)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
	
	elif(col+1 == dimensions):		
		if(board[(row)*dimensions+(col-1)] == tile):
			board[(row)*dimensions+(col-1)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
	
	# 左右自由移動
	else:
		if(board[(row)*dimensions+(col+1)] == tile):
			board[(row)*dimensions+(col+1)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
		elif(board[(row)*dimensions+(col-1)] == tile):
			board[(row)*dimensions+(col-1)] = 0
			board[(row)*dimensions+(col)] = tile
			return 1
		
			
	return 0

# 判斷是否贏得遊戲
def won():
	checked = 1
	for i in range(1,dimensions*dimensions-1,1):
		if ( not board[i] == i+1 ):
			checked = 0		
	if(not board[dimensions*dimensions-1] == 0):
		checked = 0
	
	return checked

# 主程式
def main(argv):
	global dimensions
	global board
	
	# 確認輸入參數
	if (len(argv) != 2):
		print("Usage: fifteen dimensions\n")
		return 1
		
	# 確認輸入為數字
	dimensions = argv[1]
	if( not dimensions.isnumeric() ):
		print("維度請輸入整數！！！")
		return 2
		
	dimensions = int(dimensions)
	
	# 確認輸入為整數
	if(not isinstance(dimensions, int)):
		print("維度請輸入整數！！！")
		return 3
		
	# 確認輸入維度大小	
	if ( dimensions < dim_min or dimensions > dim_max ):
		print("維度大小需介於整數 3 ~ 9 \n\n")
		return 4
		
	init();
	while (1):
		clear()
		draw()
		if (won()):
			print("恭喜破關！！！")
			break
		tile = input("請輸入想要移動的方塊號碼\n")
		while(not tile.isnumeric()):
			tile = input("請輸入想要移動的方塊號碼\n")
		tile = int(tile)
		while(not isinstance(tile, int)):
			tile = input("請輸入想要移動的方塊號碼\n")
		if (tile == 0):
			break
		if ( not move(tile)):
			print("移動方塊號碼錯誤，請重新輸入\n")
	return
	
main(sys.argv)