from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

import plotly.graph_objs as go

import sys
import os

# 全域變數
Fields = []
Datas = []
dx = [[]]
dy = [[]]

# 匯入檔案
def r_data(argv):
	
	global Fields
	global Datas
	
	# 讀取檔案
	sr = open('%s.csv' %argv[1], 'r')
	
	# 欄位名稱
	Fields = sr.readline().split('\n')[0].split(',')
	
	
	# 資料讀取
	while 1:
		row = sr.readline().split('\n')[0]
		if(not row):
			break
		row = "".join(row).split(',')
		Datas.append(row)
	
	# 關閉檔案
	sr.close()	

# 座標軸資料設定
def set_axis():
	
	global x_index
	global y_index
	
	print()
	for i in range(0,len(Fields),1) :
		print( i, "\t",Fields[i])
	
	print("\n請輸入X軸代表欄位(代碼)")
	x_index = upbound_int(len(Fields))
	
	print("\n請輸入Y軸代表欄位(代碼)")
	
	while 1:
		y_index = upbound_int(len(Fields))
		if(int(y_index) == x_index):
			print("\nY軸欄位與X軸相同\n請重新輸入")
			continue
		
		break

####################################		
# 增加資料
def add_datas():
	print("\n資料增加：\n")
	add_datas_type = ["全部匯入","分組匯入"]
	for i in range(0,len(add_datas_type),1):
		print(i,"\t",add_datas_type[i])
	
	select_add_type = upbound_int(len(add_datas_type))
	print(add_datas_type[select_add_type])
	
	if(select_add_type == 0):
		# 設定 X 軸, Y 軸 資料
		for i in range(0,len(Datas),1):
			dx[0].append(Datas[i][x_index])
			dy[0].append(Datas[i][y_index])
			
	elif(select_add_type == 1):
		add_count = 0
		while 1:			
			split_line = []
			a = 0
			b = 0
			while 1:
				line = input("\n請選擇資料行數： (n1-n2)\n\n")			
				split_line = line.split('-')			
				if( not(split_line[0].isnumeric() and split_line[1].isnumeric()) ):
					print("請重新輸入\n\n")
					continue
					
				a = int(split_line[0])-1
				b = int(split_line[1])
				
				if(a<0 or b <0):
					print("請重新輸入\n\n")
					continue
					
				break
			
			for i in range(a,b,1):
				dx[add_count].append(Datas[i][x_index])
				dy[add_count].append(Datas[i][y_index])
			
			add_count = add_count+1
			dx.append([])
			dy.append([])
			if(input("\n是否增加資料？ (0-否)") == '0'):
				break
	
# 匯出檔案
# filename	匯出檔案名稱
# data		寫入資料
'''
def data_export(filename,data):
	sw = open("{0}.csv".format(filename),"w")
	w = csv.writer(sw)
	w.writerows(data)
	sw.close()
'''

# 畫圖
def charts():
	chart_type = ["Basic Charts","Statistical and Seaborn-style Charts","Scientific Charts","Financial Charts","Maps","3D Charts","Multiple Axes, Subplots, and Insets","Financial Analysis"]
	print("\n畫圖類型：\n")
	
	# 畫圖類型
	for i in range(0,len(chart_type),1):
		print(i,"\t",chart_type[i])
	
	select_type = upbound_int(len(chart_type))
	
	print(chart_type[select_type])

	s_line()
	
	fig_data = []
	if( select_type == 0 ):
		fig_data = basic_line_plot()
	
	layout = go.Layout(
		title='Line Figure',
		xaxis=dict(title=Fields[x_index]),
		yaxis=dict(title=Fields[y_index])	
	)
	
	fig = go.Figure(data=fig_data, layout=layout)
	
	plot(fig)
	
# 折線圖
def basic_line_plot():
	
	#import pandas as pd
	import numpy as np
	
	#df = pd.DataFrame({'x': dx, 'y': dy})
	#df.head()
	
	line_modes = ["markers","lines","lines+markers"]
	
	print("\n顯示類型：\n")
	for i in range(0,len(line_modes),1):
		print(i,"\t",line_modes[i])
	
	select_line_modes = upbound_int(len(line_modes))
	print(line_modes[select_line_modes])
	
	data = []
	
	for i in range(0,len(dx),1):
		data.append(
			go.Scatter(
				# x=df['x'], # assign x as the dataframe column 'x'
				# y=df['y'],
				x = dx[i],
				y = dy[i],
				mode = line_modes[select_line_modes]
			))
	
	return data

	

# function	
# 分割線	
def s_line():
	print("\n**********************************************************************")

#	判斷整數
def upbound_int(upbound):
	
	# value 	待判斷之值
	# upbound	value之上限
	print()
	while 1:
		value = input()
		if(value.isnumeric() and isinstance(int(value),int) and int(value) > -1 and int(value)<upbound):
			value = int(value)
			return value
		print("請重新輸入")

		
		
# 主程式
def main(argv):
	
	# 確認輸入參數
	if (len(argv) != 2):
		print("\nUsage: table InputFileName(.csv)\n")
		return 1
	
	if (os.path.isfile('test.txt')):
		print("檔案開啟錯誤，請重新選擇檔案！！！")
		return 2
	
	global Fields
	global Datas	
	# 匯入檔案
	r_data(argv)
	
	global x_index
	global y_index
	global dx
	global dy
	# 座標軸資料設定
	set_axis()
	
	# 分隔線
	s_line()
	print("\nX軸欄位\t",Fields[x_index],"\nY軸欄位\t",Fields[y_index])
	
	# 分隔線
	s_line()
	
	# 增加資料
	add_datas()
	
	# 分隔線
	s_line()
	
	# 畫圖
	charts()
	
	# 分隔線
	s_line()
	
	print ("\n******************\n*   Finish !!!   *\n******************")

main(sys.argv)