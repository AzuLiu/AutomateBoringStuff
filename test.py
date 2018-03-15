bandList = '''东鹏-佛山瓷砖
大自然-佛山
东鹏-佛山洁具
东鹏-淄博
奥普
贝朗
大卫
大自然-湖州
好门面
开来
科勒
乐宜嘉-成都
乐宜嘉-合肥
乐宜嘉-中山
美标
美赫
梦天
名门
欧派-木门
欧派-五金
普乐美
西顿-开关面板
西顿-浴霸
亚美利加
意利宝
优丽斯-南京
友邦
中迅
邦克
汇泰龙
尚高
大自然-上饶
优丽斯-重庆'''
bandstr = bandList.split('\n')
print(bandstr)

import openpyxl
wb = openpyxl.load_workbook('Atest2.xlsx')
sheet = wb.get_sheet_by_name('0')
print(sheet.cell(row= 1,column=1).value/0.3)


