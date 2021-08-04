import random

# 메뉴 및 선택지
sandwiches = [
    "페퍼 치킨 슈니첼",
    "페퍼로니 피자 썹",
    "쉬림프",
    "로스트 치킨",
    "에그마요",
    "K-바비큐",
    "로티세리 바비큐 치킨",
    "풀드 포크 바비큐",
    "이탈리안 비엠티",
    "비엘티",
    "미트볼",
    "햄",
    "참치",
    "써브웨이 클럽",
    "터키",
    "베지",
    "스테이크 & 치즈",
    "터키 베이컨 아보카도",
    "스파이시 이탈리안",
    "치킨 데리야끼",
]
breads = ["화이트", "하티", "파마산 오레가노", "위트", "허니오트", "플랫"]
cheeses = ["아메리칸", "슈레드", "모짜렐라"]
toppings = ["미트", "쉬림프 더블업", "에그마요", "오믈렛", "아보카도", "베이컨", "페퍼로니", "치즈"]
vegetables = ["양상추", "토마토", "오이", "피망", "피클", "올리브", "할라피뇨", "양파"]
sauces = [
    "랜치",
    "마요네즈",
    "스위트 어니언",
    "허니 머스타드",
    "스위트 칠리",
    "핫 칠리",
    "사우스 웨스트 치폴레",
    "머스타드",
    "홀스래디쉬",
    "올리브 오일",
    "레드와인 식초",
    "소금",
    "후추",
    "스모크 바베큐",
]
lengths = ["15cm", "30cm"]

# 연결어 선택지
veges = ["채소", "야채"]
together = ["이랑", "랑", "하고"]
conn = ["으로", "로"]
sentence_conn = ["주시고", "해주시고", "하고", "해주세요.", "부탁드립니다.", "해주십시오.", "주십시오.", "할게요."]
finish = ["해주세요.", "부탁드립니다.", "해주십시오.", "주십시오.", "할게요.", "주세요.", "해줘요."]
exclude = ["빼주세요.", "빼주시고", "빼줘요.", "빼주십시오."]
top = ["토핑은", "추가토핑은", "추가 토핑은"]
add = ["추가", ""]
top2 = ["랑", "하고"]


def gen_data():
    sentences = []
    for i in range(300):
        order1 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order2 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 길이는 /length;{random.choice(lengths)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order3 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} {random.choice(veges)}는 /vegetable;{random.choice(vegetables)}/ {random.choice(exclude)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order4 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 길이는 /length;{random.choice(lengths)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} {random.choice(veges)}는 /vegetable;{random.choice(vegetables)}/ {random.choice(exclude)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order5 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} {random.choice(veges)}는 /vegetable;{random.choice(vegetables)}/{random.choice(together)} /vegetable;{random.choice(vegetables)}/ {random.choice(exclude)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order6 = f"/sandwich;{random.choice(sandwiches)}/{random.choice(conn)} {random.choice(sentence_conn)} 길이는 /length;{random.choice(lengths)}/{random.choice(conn)} {random.choice(sentence_conn)} 빵은 /bread;{random.choice(breads)}/{random.choice(conn)} {random.choice(sentence_conn)} 치즈는 /cheese;{random.choice(cheeses)}/{random.choice(conn)} {random.choice(sentence_conn)} {random.choice(veges)}는 /vegetable;{random.choice(vegetables)}/{random.choice(together)} /vegetable;{random.choice(vegetables)}/ {random.choice(exclude)} 소스는 /sauce;{random.choice(sauces)}/{random.choice(conn)} {random.choice(finish)}"
        order7 = f"{random.choice(top)} /topping;{random.choice(toppings)}/{random.choice(conn)} {random.choice(add)}{random.choice(finish)}"
        order8 = f"{random.choice(top)} /topping;{random.choice(toppings)}/{random.choice(top2)} /topping;{random.choice(toppings)}/ {random.choice(add)}{random.choice(finish)}"

        sentences.append(order1)
        sentences.append(order2)
        sentences.append(order3)
        sentences.append(order4)
        sentences.append(order5)
        sentences.append(order6)
        sentences.append(order7)
        sentences.append(order8)

    sentences = set(sentences)
    sentences = list(sentences)

    return sentences
