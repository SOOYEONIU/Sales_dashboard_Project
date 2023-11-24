"""
!sample data
{
	"date" : "2023년 00월 00일",
	"getOrderList" : [
		{
			"hour":1,
			"products":[ 
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수},
				...
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값, "누적주문수": 누적수}
			]
		},
		...
		{
			"hour":24,
			"products":[ 
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값},
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값},
				...
				{"pdName": "상품명(브랜드명)", "pdPrice": 20000, "pdOrdersCnt": random값}
			]
		}
	]
}
"""

import datetime
import random
import json

tdDate = datetime.datetime.now()

#shopping_sales_data = {}

#==========상품 정보 딕셔너리 생성 ==========
#products_info = []

class ProductData:
	def __init__(self, idV, pdName, pdPrice ):
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
		pdOrdersCnt = random.randrange(0,151)
		self.shopping_sales_data["pdOrdersCnt"] = pdOrdersCnt
		self.shopping_sales_data["cumulativeOrder"] += pdOrdersCnt

	def printInfo(self):
		return {"pdName": self.shopping_sales_data["pdName"], "pdPrice": self.shopping_sales_data["pdPrice"], "pdOrdersCnt": self.shopping_sales_data["pdOrdersCnt"], "cumulativeOrder": self.shopping_sales_data["cumulativeOrder"]}

class TodayOrderList : 
	def __init__(self, idV) :
		self.idV = idV
		self.productDummy = [];
		self.productJson = {};

	def pushDummyData(self, dummyData) :
		self.productDummy.append(dummyData)

	def randomValue(self):
		for productInfo in self.productDummy:
			productInfo.randomOrdersCnt()
		
	def makingJson(self):
		self.productJson = {}
		self.productJson["products"] = []
		
		for productData in self.productDummy :
			self.productJson["products"].append(productData)
		
		with open ("SalesData_total.json", "w") as json_file :
			json.dump(self.productJson, json_file, default=str,ensure_ascii=False, indent=4)


#===========END 상품 정보 딕셔너리 생성==========

todayOrderList = TodayOrderList("todayTotalData")

product1 = ProductData("product1", "MATIN LOGO CROP TOP IN WHITE (Matin Kim)", 39000)
product1.makeProductData
todayOrderList.pushDummyData(product1)


product2 = ProductData("product2", "여성 르 그랑 밤비노 도트백 - 블랙 (자크뮈스)", 559000)
todayOrderList.pushDummyData(product2)

product3 = ProductData("product3", "여성 미니 몬트조 버킷백 - 브라운 (펜디)", 1246000)
todayOrderList.pushDummyData(product1)

product4 = ProductData("product4", "NEW VISION DOUBLENECK (이티씨이)", 125000)
todayOrderList.pushDummyData(product4)

product5 = ProductData("product5", "여성 베아 울 가디건 - 빈티지 블랙 (비비안 웨스트우드)", 199000)
todayOrderList.pushDummyData(product5)

product6 = ProductData("product6", "OORIGINAL BLACK - 조리 블랙 (우포스)", 69000)
todayOrderList.pushDummyData(product6)

product7 = ProductData("product7", "XA 프로 3D V9 와이드 GTX", 228000)
todayOrderList.pushDummyData(product7)

product8 = ProductData("product8", "Deep One Tuck Sweat Shorts [Grey] (제로)", 32000)
todayOrderList.pushDummyData(product8)

product9 = ProductData("product9", "올데이 컴피 60수 셔츠 잉크 네이비 (애습)", 51000)
todayOrderList.pushDummyData(product9)

product10 = ProductData("product10", "매쉬 스트링 백팩 블랙 (네이키드니스)", 90000)
todayOrderList.pushDummyData(product10)

product11 = ProductData("product11", "카오와 레이어드 테크 덕 다운 점퍼 (네셔널지오그래픽)", 419000)
todayOrderList.pushDummyData(product11)

product12 = ProductData("product12", "Sopy Collar Shor-Sleeve BLACK (어반드레스)", 225000)
todayOrderList.pushDummyData(product12)

product13 = ProductData("product13", "캠버스 x 어 콜드 월* 척 70티 (컨버스)", 65000)
todayOrderList.pushDummyData(product13)

product14 = ProductData("product14", "빅스튜던트 BLACK (잔스포츠)", 89000)
todayOrderList.pushDummyData(product14)

product15 = ProductData("product15", "남성 D 핸드 자켓 - 블루 (디젤)", 94000)
todayOrderList.pushDummyData(product15)

for i in range(1, 25):
	todayOrderList.makingJson()
	todayOrderList.randomValue()
'''
productsD = [
	ProductData("product1", "MATIN LOGO CROP TOP IN WHITE (Matin Kim)", 39000),
	ProductData("product2", "여성 르 그랑 밤비노 도트백 - 블랙 (자크뮈스)", 559000),
	ProductData("product3", "여성 미니 몬트레조 버킷백 - 브라운 (펜디)", 1246000),
	ProductData("product4", "NEW VISION DOUBLENECK (이티씨이)", 125000),
	ProductData("product5", "여성 베아 울 가디건 - 빈티지 블랙 (비비안 웨스트우드)", 199000),
	ProductData("product6", "OORICINAL BLACK - 조리 블랙 (우포스)", 69000),
	ProductData("product7", "XA 프로 3D V9 와이드 GTX - 블랙:팬덤:퓨터 (살로몬)", 228000),
	ProductData("product8", "Deep One Tuck Sweat Shorts [Grey] (제로)", 32000),
	ProductData("product9", "올데이 컴피 60수 셔츠 잉크 네이비 (애습)", 51000),
	ProductData("product10", "매쉬 스트링 백팩 블랙 (네이키드니스)", 90000),
	ProductData("product11", "카오와 레이어드 테크 덕 다운 점퍼 (네셔널지오그래픽)", 419000),
	ProductData("product12", "Sopy Collar Short-Sleeve BLACK (어반드레스)", 22500),
	ProductData("product13", "캠버스 x 어 콜드 월* 척 70티 (컨버스)", 65000),
	ProductData("product14", "빅스튜던트 BLACK (잔스포츠)", 89000),
	ProductData("product15", "남성 D 핸드 자켓 - 블루 (디젤)", 94000),
]

for productData in productsD :
	productData.makeProductData()
	productData.randomOrdersCnt()
	products_info.append(productData.printInfo())
'''
#print(products_info)


