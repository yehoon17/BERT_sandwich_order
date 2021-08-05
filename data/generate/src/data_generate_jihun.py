def menu():
  sandwich = ['페퍼로니 피자 썹','이탈리안 비엠티','에그마요','스테이크&치즈','써브웨이 클럽','로티세리 바비큐 치킨','폴드 포크 바비큐','치킨 데리야끼','스파이시 이탈리안','쉬림프','페퍼치킨 슈니첼','K-바비큐','터키 베이컨 아보카도','로스트 치킨','베지','터키','햄','참치','미트볼','비엘티']
  bread = ['화이트','하티','파마산 오레가노','위트','허니오트','플랫']
  cheese = ['아메리칸 치즈','슈레드 치즈','모짜렐라 치즈']
  toping = ['미트','쉬림프 더블업','에그마요','오믈렛','아보카도','베이컨','페퍼로니','치즈']
  vegetable = ['양상추','토마토','오이','피망','피클','올리브','할라피뇨','양파']
  sauce = ['랜치','마요네즈','스위트 어니언','허니 머드타드','스위트 칠리','핫 칠리','사우스 웨스트 치폴레','머스타드','홀스래디쉬','올리브 오일','레드와인 식초','소금','후추','스모크 바베큐']
  length = ['15cm','30cm']

  return sandwich, bread, cheese, toping, vegetable, sauce, length

def gen_data(): 

  import itertools
  import random

  # 데이터 담을 빈 리스트 생성
  data =[]
  data_1=[]
  data_2=[]
  data_3=[]

  sandwich, bread, cheese, toping, vegetable, sauce, length=menu()

  # 소스와 채소는 중복이 가능하니까 2,3개 선택할 수 있는 모든 경우의수 리스트 생성
  sauce_2 = []
  for i in range(len(sauce)):
    for j in range(i+1, len(sauce)):
      sauce_2.append([sauce[i],sauce[j]])

  veg_2 = []
  for i in range(len(vegetable)):
    for j in range(i+1, len(vegetable)):
      veg_2.append([vegetable[i],vegetable[j]])

  sauce_3 = []
  for i in range(len(sauce)):
    for j in range(i+1, len(sauce)):
      for k in range(j+1, len(sauce)):
        sauce_3.append([sauce[i],sauce[j],sauce[k]])

  veg_3 = []
  for i in range(len(vegetable)):
    for j in range(i+1, len(vegetable)):
      for k in range(j+1, len(vegetable)):
        veg_3.append([vegetable[i],vegetable[j],vegetable[k]])

  # 문장 틀에 맞게 문장 생성 (모든 슬롯 포함)
  for sandwich, bread, length, cheese, vegetable, sauce in itertools.product(sandwich, bread, length, cheese, vegetable, sauce):
    data.append('/sandwich;{0}/에 빵은 /bread;{1}/에 주시고, 길이는 /length;{2}/로, 치즈는 /cheese;{3}/, 채소는 /vegetable;{4}/ 빼주시고, 아 그리고 소스는 /sauce;{5}/로 주세요.'.format(sandwich,bread,length,cheese,vegetable,sauce))
    data.append('안녕하세요 /sandwich;{}/ /bread;{}/에다가 /length;{}/ 크기로 주시고, 치즈는 /cheese;{}/ 많이 주시고 채소 중에 /vegetable;{}/는 꼭 빼주시고 소스는 /sauce;{}/로 주세요.'.format(sandwich,bread,length,cheese,vegetable,sauce))
  
  # 생성된 데이터 랜덤 추출
  data = random.sample(data,600)


  # 문장 틀에 맞게 문장 생성 (모든 슬롯 포함)
  # 리스트 오류가 발생해 중간에 메뉴 업데이트
  sandwich, bread, cheese, toping, vegetable, sauce, length=menu()
  for sandwich in sandwich:
    data_1.append('메인은 /sandwich;{}/로 주세요.'.format(sandwich))
    data_1.append('/sandwich;{}/ 한 개 부탁드립니다.'.format(sandwich))
    data_1.append('/sandwich;{}/ 부탁합니다.'.format(sandwich))
    data_1.append('기본은 /sandwich;{}/ 주세요.'.format(sandwich))
  for bread in bread:
    data_1.append('빵은 /bread;{}/로 주세요.'.format(bread))
    data_1.append('/bread;{}/로 해주세요.'.format(bread))  
    data_1.append('빵은 /bread;{}/로 할게요.'.format(bread))
    data_1.append('/bread;{}/로 할게요.'.format(bread))
  for length in length:
    data_1.append('길이는 /length;{}/로 해주세요.'.format(length))
    data_1.append('/length;{}/로 할게요.'.format(length))
    data_1.append('/length;{}/로 주세요.'.format(length))
    data_1.append('크기는 /length;{}/로 주세요.'.format(length))
  for cheese in cheese:
    data_1.append('치즈는 /cheese;{}/로 주세요.'.format(cheese))
    data_1.append('/cheese;{}/로 넣어주세요.'.format(cheese))
    data_1.append('치즈 /cheese;{}/로 해주세요.'.format(cheese))
    data_1.append('/cheese;{}/로 부탁드립니다.'.format(cheese))
  for vegetable in vegetable:
    data_1.append('채소 중에 /vegetable;{}/는 빼주세요.'.format(vegetable))
    data_1.append('/vegetable;{}/는 빼주세요.'.format(vegetable))
    data_1.append('/vegetable;{}/는 안 넣어 주셔도 괜찮아요.'.format(vegetable))
    data_1.append('야채 중에 /vegetable;{}/는 넣지 말아주세요.'.format(vegetable))
  for sauce in sauce:
    data_1.append('소스는 /sauce;{}/ 주세요.'.format(sauce))
    data_1.append('/sauce;{}/로 넣어주세요.'.format(sauce))
    data_1.append('소스 /sauce;{}/로 해주세요.'.format(sauce))
    data_1.append('/sauce;{}/ 뿌려주세요.'.format(sauce))

  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for veg1, veg2 in veg_2:
    data_2.append('채소 중에 /vegetable;{}/랑 /vegetable;{}/는 빼주세요.'.format(veg1,veg2))
    data_2.append('야채 /vegetable;{}/, /vegetable;{}/는 안 넣어주셔도 돼요.'.format(veg1,veg2))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sauce1, sauce2 in sauce_2:
    data_2.append('소스 /sauce;{}/랑 /sauce;{}/ 주세요.'.format(sauce1,sauce2))
    data_2.append('/sauce;{}/, /sauce;{}/ 두 가지로 해주세요.'.format(sauce1,sauce2))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for bread, length in itertools.product(bread, length):
    data_2.append('빵은 /bread;{}/ 주시고, 길이는 /length;{}/로 해주세요.'.format(bread,length))
    data_2.append('/bread;{}/에 크기는 /length;{}/ 주세요.'.format(bread,length))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sandwich, cheese in itertools.product(sandwich, cheese):
    data_2.append('/sandwich;{}/에 치즈는 /cheese;{}/로 주세요.'.format(sandwich,cheese))
    data_2.append('/sandwich;{}/주시고 치즈는 /cheese;{}/로 올려주세요.'.format(sandwich,cheese))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sandwich, bread in itertools.product(sandwich, bread):
    data_2.append('/sandwich;{}/에 빵은 /bread;{}/로 주세요.'.format(sandwich,bread))
    data_2.append('저는 /sandwich;{}/ /bread;{}/에다가 주세요.'.format(sandwich,bread))


  # 문장 틀에 맞게 문장 생성 (모든 슬롯 포함)
  # 리스트 오류가 발생해 중간에 메뉴 업데이트
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for veg1, veg2, veg3 in veg_3:
    data_3.append('채소 중에 /vegetable;{}/랑 /vegetable;{}/랑 /vegetable;{}/는 빼주세요.'.format(veg1,veg2,veg3))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sauce1, sauce2, sauce3 in sauce_3:
    data_3.append('소스 /sauce;{}/랑 /sauce;{}/랑 /sauce;{}/ 주세요.'.format(sauce1,sauce2,sauce3))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sandwich, bread, length in itertools.product(sandwich, bread,length):
    data_3.append('/sandwich;{}/에 빵은 /bread;{}/로 주시고, 길이는 /length;{}/로 해주세요.'.format(sandwich,bread,length))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for sandwich, bread, cheese in itertools.product(sandwich, bread,cheese):
    data_3.append('/sandwich;{}/에 빵은 /bread;{}/로 주시고, 치즈는 /cheese;{}/ 넣어주세요.'.format(sandwich,bread,cheese))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for cheese, vegetable, sauce in itertools.product(cheese, vegetable, sauce):
    data_3.append('치즈는 /cheese;{}/로 주시고 채소는 /vegetable;{}/ 빼주시고, 소스는 /sauce;{}/로 주세요.'.format(cheese, vegetable, sauce))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for vegetable, [sauce1, sauce2] in itertools.product(vegetable,sauce_2):
    data_3.append('채소는 /vegetable;{}/ 빼주시고, 소스는 /sauce;{}/랑 /sauce;{}/로 주세요.'.format(vegetable, sauce1, sauce2))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for [veg1,veg2], sauce in itertools.product(veg_2,sauce):
    data_3.append('채소는 /vegetable;{}/랑 /vegetable;{}/ 빼주시고, 소스는 /sauce;{}/로 주세요.'.format(veg1,veg2,sauce))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for length,[veg1,veg2] in itertools.product(length, veg_2):
    data_3.append('크기는 /length;{}/로 해주시고 /vegetable;{}/랑 /vegetable;{}/ 빼주세요.'.format(length,veg1,veg2))
  sandwich, bread, cheese, toping, vegetable, sauce, length = menu()
  for length, vegetable, sauce in itertools.product(length, vegetable, sauce):
    data_3.append('크기는 /length;{}/로 해주시고 /vegetable;{}/ 빼주시고 소스는 /sauce;{}/로 주세요.'.format(length, vegetable, sauce))
  
  # 생성된 데이터 랜덤 추출
  data_3= random.sample(data_3,600)


  # 데이터 병합
  data.extend(data_1)
  data.extend(data_2)
  data.extend(data_3)

  return data
