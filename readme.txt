##--<< 정규식
http://pythex.org/
https://docs.python.org/2/library/re.html

http://simplesolace.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EC%A0%95%EA%B7%9C%EC%8B%9D
##--<< 문자열
http://simplesolace.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EB%AC%B8%EC%9E%90%EC%97%B4

import re

##--<< 처음부터 영문자만 리턴받기
[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]
p=re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+').match("py123").group()
m=p.match("py123")

print(re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣0-9]+').match("12한글4567py123").group())


p=re.compile('[^0]')   #0을 젱외
p=re.compile('[a|b]')   #a 또는 b
p=re.compile('[^0-9]')   # 숫자가 아닌 모든문자
p=re.compile('[^a-zA-Z0-9_]')   # 숫자나 문자가 아닌것
p=re.compile('[a-zA-Z0-9]+')

p=re.compile('[a-z]+')
m=p.match("py123")
m.group()
print(m.group())


>>> type('파이썬')
(type 'str')
>>> type(u'파이썬')
(type 'unicode')
>>> s='파이썬'
>>> u=u'파이썬'
>>> s==u
False
>>> s.decode('cp949')==u
True
>>> s==u.encode('cp949')
True
