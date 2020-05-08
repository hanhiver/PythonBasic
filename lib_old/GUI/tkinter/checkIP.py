import tkinter as tk
from tkinter import ttk 
import pygeoip
from pprint import pprint

class FindLocation(object):
	def __init__(self):
		self.gi = pygeoip.GeoIP('./GeoLiteCity.dat')

		style = ttk.Style()
		style.configure("BW.TLabel", foreground="black", background="white")

		# 创建主要窗口，容纳其他所有控件。
		self.root = tk.Tk()
		# 设置主窗口标题。
		self.root.title('全球定位IP位置（离线版）')
		# 创建一个输入框，并且设置尺寸。
		self.ip_input = ttk.Entry(self.root, width = 30)
		# 创建一个回显列表
		self.display_info = tk.Listbox(self.root, width = 50)
		# 创建一个查询结果的按钮。 
		self.result_button = ttk.Button(self.root, 
									   command = self.find_position, 
									   text = '查询')

	# 完成布局
	def gui_arange(self):
		self.ip_input.pack()
		self.display_info.pack()
		self.result_button.pack()

	# 根据IP查找地理位置。 
	def find_position(self):
		# 获取输入信息
		self.ip_addr = self.ip_input.get()
		aim = self.gi.record_by_name(self.ip_addr)
		pprint(aim)

		try:
			# 获取目标城市
			city = aim['city']
			# 获取目标国家
			country = aim['country_name']
			# 获取目标地区
			region_code = aim['region_code']
			# 获取目标经度
			longitude = aim['longitude']
			# 获取目标纬度
			latitude = aim['latitude']
			print('All info got. ')
		except:
			raise 

		# 创建临时列表。
		#ip_info = '所在纬度：{}\n 所在经度：{}\n 地域代码：{}\n 所在城市：{}\n 所在国家或地区：{}\n 需要查询的IP：{}'.format(
		#			latitude, longitude, region_code, city, country, self.ip_addr)
		ip_info = ['所在纬度：' + str(latitude),  
				   '所在经度：' + str(longitude), 
				   '地域代码：' + str(region_code), 
				   '所在城市：' + str(city),
				   '所在国家或地区：' + str(country), 
				   '需要查询的IP：' + str(self.ip_addr)]


		# 清空回显列表的可见部分。
		for item in range(10):
			self.display_info.insert(0, '')

		# 为回显列表赋值。
		for item in ip_info:
			self.display_info.insert(0, item)

def main():
	# 初始化对象
	FL = FindLocation()

	# 布局窗口
	FL.gui_arange()

	# 执行主程序
	tk.mainloop()
	pass

if __name__ == '__main__':
	main()


