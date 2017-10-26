import json
import requests
from bs4 import BeautifulSoup

def melon_search(query):
    params = {
        'jscallback': '_',
        'query': query,
    }
    jsonp_string = requests.get('http://www.melon.com/search/keyword/index.json', params=params).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')

    meta = json.loads(json_string)
    messages = []
    if 'SONGCONTENTS' in meta:
        for song in meta['SONGCONTENTS']:
            messages.append('''[{ALBUMNAME}] {SONGNAME} by {ARTISTNAME} - http://www.melon.com/song/detail.htm?songId={SONGID}'''.format(**song))

    if messages:
        message = '\n'.join(messages)
    else:
        message = '검색어 "{}"에 대한 노래 검색결과가 없습니다.'.format(query)
    return message

def car_type1(car_type):
    eun = {'뉴 i30(PD)' : 5506, '뉴 i40' : 5510, '그랜저 하이브리드(HG)' : 5309, '그랜저 하이브리드(IG)' : 5489, '그랜저(IG)' : 5384, '뉴 맥스크루즈' : 5386, '벨로스터': 4969, '그랜드 스타렉스' : 5344, '싼타페 더 프라임' : 5438, '쏘나타 뉴 라이즈' : 5456, '쏘나타 뉴 라이즈 플러그인 하이브리드' : 5555, '쏘나타 뉴 라이즈 하이브리드' : 5520, '쏠라티' : 5401, '뉴 아반떼(AD)' : 5462}
    name = eun.get(car_type)

    jsonp_string = requests.get('http://www.carisyou.com/' + str(name)).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')

    meta = json.loads(jsonp_string)
    messages = []
    messages1 = []

    for i in meta:
        messages.append(i['carGradeNm'])
        messages1.append(i['salePrice'])
        total = dict(zip(messages, messages1))

    #for key in sorted(total):
    #    message = "%s: %s" % (key, total[key])
    #    return message
        message = '\n'.join(['%s: %s' % (key, value) for (key, value) in total.items()])

    return message

def Car_Price(car_price):
    eun = {'1.6 GDi Style':53089,'1.6 GDi Value Plus':53091, '1.6 GDi Smart':53092, '1.6 GDi Modern':53093, '1.6 GDi Premium':53094, '1.6 VGT Style':53096, '1.6 VGT Smart':53098, '1.6 VGT Smart Special':53099, '1.6 VGT Premium':53100, '1.6 T-GDi SPORT':53101, '1.6 T-GDi SPORT 7DCT':53102, '1.6 T-GDi SPORT Extreme Selection':53103, '1.6 T-GDi SPORT Original':53104 }
    name = eun.get(car_price)

    jsonp_string = requests.get('http://www.carisyou.com/' + str(name)).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')

    meta = json.loads(jsonp_string)
    messages = []
    messages1 = []

    for i in meta:
        #print(meta)
        F = meta['firstPrice'].split('.')
        T = meta['totalPrice'].split('.')

    message = '초기 비용 : {} 만원\n총 비용 : {} 만원'.format(F[0], T[0])

    return message

def Car_PriceUrl(car_price):
    eun = {'1.6 GDi Style':53089,'1.6 GDi Value Plus':53091, '1.6 GDi Smart':53092, '1.6 GDi Modern':53093, '1.6 GDi Premium':53094, '1.6 VGT Style':53096, '1.6 VGT Smart':53098, '1.6 VGT Smart Special':53099, '1.6 VGT Premium':53100, '1.6 T-GDi SPORT':53101, '1.6 T-GDi SPORT 7DCT':53102, '1.6 T-GDi SPORT Extreme Selection':53103, '1.6 T-GDi SPORT Original':53104 }
    name = eun.get(car_price)

    url = 'http://www.carisyou.com/' + str(name)

    return url

def car_rank(name):

    try:
        html = requests.get('https://www.carisyou.com').text
    except:
        return 555
    soup = BeautifulSoup(html, 'html.parser')

    title_list = soup.select('.list_con span[class*=name]')
    data = []

    for title in title_list:
        data.append(title.text)

    if name.find('등록순위') != -1:
        #for idx, title in enumerate(title_list, 1):
            #if idx < 4:
                #return "{}{} {}".format(idx, '위', title.text)
        message = '\n1위 : ' + data[0] + '\n2위 : ' + data[1] + '\n3위 : ' + data[2] + '\n수입차 등록순위' + '\n1위 : ' + data[3] +'\n2위 : ' + data[4] + '\n3위 :' + data[5]
    else:
        message = '잘못된 접근입니다.'
    return message

def car_brandname(car_brand):

    eun = {'현대자동차' : 904, '기아자동차' : 1193, 'BMW' : 212, '폭스바겐' : 2331 }
    name = eun.get(car_brand)

    jsonp_string = requests.get('http://www.carisyou.com/' + str(name)).text
    json_string = jsonp_string.replace('_(', '').replace(');', '')

    meta = json.loads(jsonp_string)
    messages = []

    for i in meta:
        messages.append(i['carClassNm'])

    if messages:
        message = '\n'.join(messages)

    return message
