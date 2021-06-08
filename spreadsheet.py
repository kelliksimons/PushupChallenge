import gspread



gc = gspread.service_account(filename='creds.json')
sh = gc.open_by_key('1Y49BGD-2p9t9WdHkvQwh76q4yI1kP-SYRGPc9wN_SSI')
worksheet = sh.sheet1

#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
#res = worksheet.col_values(1) 

#user = [""]
#update cell
#Change cell color
worksheet.format("D2:J2",{"backgroundColor": 
{"red": 0.0,
"green":1.0,
"blue":0.0}})
#print(res)#