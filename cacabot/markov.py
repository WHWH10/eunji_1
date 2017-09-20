import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
import urllib.request
import os, re, json, random

#마르코프체인 딕셔너리 생성
def make_dic(words):
    tmp=["@"]
    dic={}
    for word in words:
        tmp.append(word)
        if len(tmp) <3 : continue
        if len(tmp) >3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word =="." :
            tmp=["@"]
            contiune
    return dic
#딕셔너리 데이터 등록
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1
#문장 만들기
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == ".": break
        w1, w2 = w2, w3
    ret = "".join(ret)
    #띄어쓰기
    params = urllib.parse.urlencode({
        "_callback":"",
        "q":ret
    })
    #네이버 맞춤법 검사기
    data = urllib.request.urlopen("https://m.search.naver.com/p/csearch/dcontent/spellchecker.nhn?" + params)
    data = data.read().decode("utf-8")[1:-2]
    #data = json.loads(data)
    data = data["message"]["result"]["html"]
    data = soup = BeautifulSoup(data, "html.parser").getText()
    #리턴
    return data
def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

#문장 읽어들이기
#dict_file = "markov-con.json"
if not os.path.exists(dict_file):
    #fp =
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("body > text")
    text = body.getText()
    text = text.replage("...", "")
    #형태소 분석
    twitter = Twitter()
    malist = twitter.pos(text, norm = True)
    words = []
    for word in malist:
        if not word[1] in ["Punctuation"] :
            words.append(word[0])
        if word[0] = ".":
            words.append(word[0])
    #딕셔너리 생성
    dic = make_dic(words)
#    json.dump(dic, open(dict_file, "w", encoding="utf-8")
else:
#    dic = json.load(open(dict_file,"r"))

#문장만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("---")
