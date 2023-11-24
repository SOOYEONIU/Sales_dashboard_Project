"""
productInfo = {
	"hours" : 1,
	"products" : {
		"상품명1" : {"가격": 1000, "판매량": random},
		"상품명2" : {"가격": 1000, "판매량": random},
		...
		"상품명13" : {"가격": 1000, "판매량": random},
		"상품명14" : {"가격": 1000, "판매량": random},
		"상품명15" : {"가격": 1000, "판매량": random},
	}
}
"""

import json
import random
import datetime

now = datetime.datetime.now()
"""
sales_value = 0;
sales_value = random.randrange(0, 1001)
"""

product_info = {
	"date" : "{}년 {}월 {}일".format( now.year, now.month, now.day ),
	"hours": 20, 
	"products": {
		"5PK ARCHON SELVEDGE WIDE (유니온블루)": {"가격": 198000, "판매량": random.randrange(0, 1001)}, 
		"FAN STAND 3Z 탁상용 무선 선풍기 (루메나)": {"가격": 34900, "판매량": random.randrange(0, 1001)}, 
		"남성 이스트/웨스트 크로커다일 엠보싱 레더 반지갑 (생로랑)": {"가격": 760000, "판매량": random.randrange(0, 1001)},
		"여성 베아 울 가디건 (비비안 웨스트우드) ": {"가격": 730000, "판매량": random.randrange(0, 1001)}, 
		"캠퍼스 00s - 블랙:화이트 (아디다스)": {"가격": 129000, "판매량": random.randrange(0, 1001)}, 
		"공용 스몰 크루아상 크로스백 - 다크초콜릿 (르메르)": {"가격": 1093000, "판매량": random.randrange(0, 1001)}, 
		"OORIGINAL BLACK - 조리 블랙 (우포스)": {"가격": 69000, "판매량": random.randrange(0, 1001)}, 
		"여성 몰디드 타코 크로스백 - 블랙 (르메르)": {"가격": 1735000, "판매량": random.randrange(0, 1001)}, 
		"FAN PRIME 3 탁상용 무선 선풍기 (루메나)": {"가격": 54900, "판매량": random.randrange(0, 1001)}, 
		"여성 스몰 트리오페 틴 숄더백 - 브라운 (셀린느)": {"가격": 3350000, "판매량": random.randrange(0, 1001)}, 
		"삼바 OG - 그린:화이트 (아디다스)": {"가격": 139000, "판매량": random.randrange(0, 1001)}, 
		"남성 BB 레이저 디스트로이드 볼캡 - 블랙:화이트 (발렌시아가)": {"가격": 490000, "판매량": random.randrange(0, 1001)}, 
		"PENOMECO) 후드 티셔츠 (페노메코)": {"가격": 109000, "판매량": random.randrange(0, 1001)}, 
		"남성 버로우드 BD 셔츠 - 베이지 (아워 레가시)": {"가격": 399000, "판매량": random.randrange(0, 1001)}, 
		"남성 모노그램 로고 셔츠 - 블랙  (버버리)": {"가격": 810000, "판매량": random.randrange(0, 1001)},
		"삼바 OG - 크림:살몬 (아디다스)": {"가격": 139000, "판매량": random.randrange(0, 1001)}
	}
}

with open ("20h.json", "w") as json_file :
	json.dump(product_info, json_file, ensure_ascii=False)
