{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1a9eeb68",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random\n",
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "5bc1e79a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#길이\n",
    "length=['15cm','30cm','15센치','30센치','15센티','30센티']\n",
    "\n",
    "#샌드위치\n",
    "sandwich=['페퍼로니 피자썹', '이탈리안 비엠티', '에그마요', '스테이크 치즈',\n",
    "          '써브웨이 클럽','로티세리 바비큐 치킨','햄', '참치', '미트볼',\n",
    "          '풀드 포그 바비큐','치킨 데리야끼', '스파이시 이탈리안','쉬림프'\n",
    "          ,'베지', '터키','비엘티','페퍼 치킨 슈니첼','K-바비큐', '터키 베이컨 아보카도','로스트 치킨']\n",
    "\n",
    "#빵\n",
    "bread=['화이트', '하티', '파마산 오레가노', '위트', '허니오트', '플랫']\n",
    "\n",
    "#치즈\n",
    "cheese=['아메리칸 치즈', '슈레드 치즈', '모짜렐라 치즈']\n",
    "\n",
    "#추가토핑\n",
    "add_topping=['미트', '쉬림프 더블업', '에그마요', '오믈렛',\n",
    "             '아보카도', '베이컨','페퍼로니','치즈']\n",
    "\n",
    "#야채제거\n",
    "vegtable=['양상추 ','토마토','오이','피망','피클','올리브','할라피뇨','양파']\n",
    "\n",
    "#소스\n",
    "sauce=['랜치','마요네즈','스위트 어니언','허니 머스타드','스위트 칠리',\n",
    "       '핫 칠리','사우스 웨스트 치폴레','머스타드','홀스래디쉬',\n",
    "       '올리브 오일','레드와인 식초','소금','후추','스모크 바베큐',]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "66d0b3a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#기타 문장 추가\n",
    "list_ect = [\n",
    "    #영업시간 관련사항\n",
    "          '영업시간은 언제부터 언제까지 인가요?',\n",
    "          '지금 주문 가능한가요?',\n",
    "    #질의응답 관련사항\n",
    "          '그냥 채팅으로 주문하면 되는건가요?',\n",
    "    #배달,방문포장 관련\n",
    "          '배달요금이 따로 있나요',\n",
    "          '배달 가능한가요?',\n",
    "          '방문포장 가능한가요?',\n",
    "          '배달 가능 지역이 어디까지 인가요?',\n",
    "    #메뉴 추천\n",
    "          '메뉴가 너무 많은데 추천 해주세요',\n",
    "          '메뉴 추천 해주세요',\n",
    "    #불만사항 예상답변: 죄송합니다 저희매장에서 더욱 신경쓰도록 하겠습니다.\n",
    "          '여기 알바생이 불친절 하던데 클레임은 어떻게 걸까요',\n",
    "          '음식이 너무 짜요',\n",
    "          '왜 이렇게 오래 걸리나요?',\n",
    "          '아 몰라 사장 나오라고 그래',\n",
    "    #시간 안내\n",
    "          '나오는데 얼마나 걸릴까요?',\n",
    "          '배고픈데 빨리 해주세요',\n",
    "    #기타\n",
    "          '노래 좀 불러줘',\n",
    "          '오 맛있어요 다음에도 주문 할 게요',\n",
    "    #주문취소 및 변경\n",
    "          '주문 취소 가능할까요?',\n",
    "          '혹시 주문 취소 하려는데 괜찮을까요?',\n",
    "          '오이 빼달라는걸 잊어서 오이 지금이라도 뺄 수 있을까요?',\n",
    "          '아 맞다 제가 오이를 못먹어서 오이도좀 빼주세요',\n",
    "           ]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "70ac75ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 접목어\n",
    "leng =['','길이','길이는']\n",
    "sand =['','고기','고기는']\n",
    "brea =['','빵','빵은']\n",
    "chee =['','치즈','치즈는']\n",
    "sauc =['','소스','소스는']\n",
    "together = ['','이랑','랑','하고']\n",
    "cont = ['','으로', '로']\n",
    "con = ['','주시고', '해주시고', '하고','해주세요', '부탁드립니다', '해주십시오', '주십시오', '할게요']\n",
    "finish = ['','해주세요.', '부탁드립니다.', '해주십시오.', '주십시오.', '할게요.', '주세요.', '해줘요.']\n",
    "exclude = ['빼고']\n",
    "vege = ['','채소','야채']\n",
    "top = ['','토핑은','추가토핑은','추가 토핑은']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c08c73ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['길이는 /length;30센티/  ', '고기는 /sandwich;로스트 치킨/ 로 ', ' /bread;파마산 오레가노/ 으로 ', '치즈는 /cheese;슈레드 치즈/ 로 ', '채소 /vegetable;양파/ 빼고 ', '소스 /sauce;마요네즈/ 으로 ']\n"
     ]
    }
   ],
   "source": [
    "#순서섞기 리스트 저장\n",
    "s_l = f'{random.choice(leng)} /length;{random.choice(length)}/ {random.choice(cont)} '\n",
    "s_s = f'{random.choice(sand)} /sandwich;{random.choice(sandwich)}/ {random.choice(cont)} '\n",
    "s_b = f'{random.choice(brea)} /bread;{random.choice(bread)}/ {random.choice(cont)} '\n",
    "#s_at = f'{random.choice(top)} /add_toping;{random.choice(add_topping)}/ {random.choice(together)}'\n",
    "s_ch = f'{random.choice(chee)} /cheese;{random.choice(cheese)}/ {random.choice(cont)} '\n",
    "s_ev = f'{random.choice(vege)} /vegetable;{random.choice(vegtable)}/ {random.choice(exclude)} '\n",
    "s_sa = f'{random.choice(sauc)} /sauce;{random.choice(sauce)}/ {random.choice(cont)} '\n",
    "lists=[s_l,s_s,s_b,s_ch,s_ev,s_sa]\n",
    "print(lists)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "d57e075f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#사용 함수들\n",
    "#중복 난수 제거\n",
    "def Random_eliminate():\n",
    "    exlist = []                               \n",
    "    for i in range(0,5):\n",
    "        a = random.randint(0,5)       \n",
    "        while a in exlist :\n",
    "            a = random.randint(0,5)\n",
    "        exlist.append(a)\n",
    "    return exlist\n",
    "\n",
    "#2d to 1d\n",
    "def flatten(input):\n",
    "    flat = []\n",
    "    for i in input:\n",
    "        for j in i:\n",
    "            new_list.append(j)\n",
    "    return new_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "b3703139",
   "metadata": {},
   "outputs": [],
   "source": [
    "#순서 재정렬 및 누적저장\n",
    "data = []\n",
    "def gen_data() :\n",
    "    for i in range(1,2001):\n",
    "        temp = [Random_eliminate()]\n",
    "        ttemp = flatten(temp)\n",
    "        tttemp = lists[ttemp[0]]+f'{random.choice(con)} '+lists[ttemp[1]]+f'{random.choice(con)} '+lists[ttemp[2]]+f'{random.choice(con)} '+lists[ttemp[3]]+f'{random.choice(con)} '+lists[ttemp[4]]+f'{random.choice(finish)}'\n",
    "        data.append(tttemp)\n",
    "        if i ==2000:\n",
    "            for j in range(0,len(list_ect)):\n",
    "                data.append(list_ect[j])\n",
    "    return data"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
