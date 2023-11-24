'''
!sample data
{
	1: [ 
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		...
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
	],
	2: [ 
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
		...
		{"pdName": "", "pdPrice": , "pdOrdersCnt": random값, "cumulativeOrder": 누적값},
	],
	...
}
'''

import datetime
import random
import json
import time

tdDate = datetime.datetime.now()

#sample_list = []
#상품 정보 딕셔너리 생성
class ProductData:
	def __init__( self, idV, pdName, pdPrice ):
		self.idV = idV
		self.pdName = pdName
		self.pdPrice = pdPrice
		self.shopping_sales_data = {}

	def makeProductData(self):
		self.shopping_sales_data["pdName"] = self.pdName
		self.shopping_sales_data["pdPrice"] = self.pdPrice
		self.shopping_sales_data["pdOrdersCnt"] = 0
		self.shopping_sales_data["cumulativeOrder"] = 0

	def randomOrdersCnt(self):
		if self.pdPrice >= 500000:
			pdOrdersCnt = random.randrange(0, 1)
		elif  100000 <= self.pdPrice < 500000:
			pdOrdersCnt = random.randrange(0, 3)
		elif self.pdPrice < 100000:
			pdOrdersCnt = random.randrange(0, 10)
		self.shopping_sales_data["pdOrdersCnt"] = pdOrdersCnt
		self.shopping_sales_data["cumulativeOrder"] += pdOrdersCnt

	def printInfo(self):
		return {"pdName": self.shopping_sales_data["pdName"], "pdPrice": self.shopping_sales_data["pdPrice"], "pdOrdersCnt": self.shopping_sales_data["pdOrdersCnt"], "cumulativeOrder": self.shopping_sales_data["cumulativeOrder"]}

#인스턴스 선언
product_list = []

product1 = ProductData("product1", "여성 르 그랑 밤비노 도트백 - 블랙 (자크뮈스)", 559000)
product1.makeProductData()
product_list.append(product1)

product2 = ProductData("product2", "MATIN LOGO CROP TOP IN WHITE (Matin Kim)", 39000)
product2.makeProductData()
product_list.append(product2)

product3 = ProductData("product3", "여성 미니 몬트레조 버킷백 - 브라운 (펜디)", 1246000)
product3.makeProductData()
product_list.append(product3)

product4 = ProductData("product4", "NEW VISION DOUBLENECK (이티씨이)", 125000)
product4.makeProductData()
product_list.append(product4)

product5 = ProductData("product5", "여성 베아 울 가디건 - 빈티지 블랙 (비비안 웨스트우드)", 199000)
product5.makeProductData()
product_list.append(product5)

product6 = ProductData("product6", "OORIGINAL BLACK - 조리 블랙 (우포스)", 69000)
product6.makeProductData()
product_list.append(product6)

product7 = ProductData("product7", "XA 프로 3D V9 와이드 GTX - 블랙:팬텀:퓨터 (살로몬)", 228000)
product7.makeProductData()
product_list.append(product7)

product8 = ProductData("product8", "Deep One Tuck Sweat Shorts [Grey] (제로)", 32000)
product8.makeProductData()
product_list.append(product8)

product9 = ProductData("product9", "올데이 컴피 60수 셔츠 잉크 네이비 (애습)", 51000)
product9.makeProductData()
product_list.append(product9)

product10 = ProductData("product10", "매쉬 스트링 백팩 블랙 (네이키드니스)", 90000)
product10.makeProductData()
product_list.append(product10)

product11 = ProductData("product11", "콰오와 레이어드 테크 덕 다운 점퍼 (네셔널지오그래픽)", 419000)
product11.makeProductData()
product_list.append(product11)

product12 = ProductData("product12", "Sopy Collar Short-Sleeve BLACK (어반드레스)", 22500)
product12.makeProductData()
product_list.append(product12)

product13 = ProductData("product13", "컴퍼스 x 어 콜드 월* 척 70 티 (컨버스)", 65000)
product13.makeProductData()
product_list.append(product13)

product14 = ProductData("product14", "빅스튜던트 BLACK (잔스포츠)", 89000)
product14.makeProductData()
product_list.append(product14)

product15 = ProductData("product15", "남성 D 핸드 자켓 - 블루 (디젤)", 94000)
product15.makeProductData()
product_list.append(product15)

#JSON데이터 만들기
productJSON = {}
productJSON["date"] = "{}년{}월{}일".format( tdDate.year, tdDate.month, tdDate.day )

for i in range(24):
	sample_list = []
	for product in product_list:
		product.randomOrdersCnt()
		sample_list.append(product.printInfo())
	productJSON[i+1] = sample_list
	with open ("SalesData_product.json", "w") as json_file:
		json.dump(productJSON, json_file, default=str, ensure_ascii=False, indent=4)
	#print("{}번째 업데이트".format(i))
	time.sleep(1)
