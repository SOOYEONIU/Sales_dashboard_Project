"""
TodaySales = {
	"2023년 08월 10일" : {
		**for문으로 반복 돌리기
		"hour": 1 ~ 24,
		"productData" : {
			"상품명 (브랜드)": { "가격": 0, "판매량": random값 },
			"상품명 (브랜드)": { "가격": 0, "판매량": random값 },
			"상품명 (브랜드)": { "가격": 0, "판매량": random값 },
			...
			"상품명 (브랜드)": { "가격": 0, "판매량": random값 },
			"상품명 (브랜드)": { "가격": 0, "판매량": random값 },
	}
}
"""

import datetime
import random
import json

now = datetime.datetime.now()
today_sales = {
	"date": "{}년 {}월 {}일".format( now.year, now.month, now.day ), 
	"productData" : {
		"상품명 (브랜드)": {"가격": 0, "판매량": random.randrange(0,501)}
	}
}

for i in range(24):
	today_sales["hours"] = i+1


with open ("todaySales2.json", "w") as data_file:
	json.dump(today_sales, data_file, ensure_ascii=False, indent=4)

"""for i in range(24) :
	"hour": i+1,
		"productData" : {
			"상품명(브랜드)" : {"가격" : 0, "판매량": random.randrange(0, 501)}
		}"""

