# -*- coding: utf-8 -*-
import json
import re
import sys

from django.shortcuts import render
from django.http import HttpResponse
from xml.dom.minidom import parseString
from django.template import RequestContext, Template
from django.utils.encoding import python_2_unicode_compatible
##--<< CST_token 인증처리
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from . models import CaKeyfriend
from . models import CaKeyboard
from . models import CaMessage
from . models import CaChatroom
from django.utils import timezone
from django.http import JsonResponse
from .import functions

RowCount = 1000
@csrf_protect
# Create your views here.
#abc= "한글1".decode('utf-8')
@csrf_exempt
@python_2_unicode_compatible
def keyboardpage(request):
    print("###---<<<  keyboardpage  >>>---###")
    print("@request.method : "+ request.method)
    print("@HttpRequest.path_info : "+ request.path_info)
    print("@HttpRequest.path : "+ request.path)
    print("@req.META[SERVER_NAME] : "+ request.META["SERVER_NAME"])
    print("@req.META[CONTENT_LENGTH] : "+ request.META["CONTENT_LENGTH"])
    print("@req.META[CONTENT_TYPE] : "+ request.META["CONTENT_TYPE"])
    print("@req.META[HTTP_HOST] : "+ request.META["HTTP_HOST"])
    print("@req.META[REMOTE_ADDR] : "+ request.META["REMOTE_ADDR"])
    print("@req.META[REMOTE_HOST] : "+ request.META["REMOTE_HOST"])
    print("@HttpRequest.scheme : "+ request.scheme)
    print("@req.META[REQUEST_METHOD] : "+ request.META["REQUEST_METHOD"])
    print("@req.META[SERVER_PORT] : "+ request.META["SERVER_PORT"])

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['견적내기', '컨텐츠 조회', '문의하기']
    })

@csrf_exempt
@python_2_unicode_compatible
def messagepage(request):
    global  RowCount
    RowCount = RowCount + 1
    print(RowCount)
    print("###---<<<  messagepage  >>>---###")
    print("---------------------------------")
    print("@request.method : "+ request.method)
    print("@HttpRequest.path_info : "+ request.path_info)


    eun = ['현대자동차', '기아자동차', 'BMW', '폭스바겐']
    hyundai = ['뉴 i30(PD)', '뉴 i40', '그랜저 하이브리드(HG)', '그랜저 하이브리드(IG)', '그랜저(IG)', '뉴 맥스크루즈', '벨로스터', '그랜드 스타렉스', '싼타페 더 프라임', '쏘나타 뉴 라이즈', '쏘나타 뉴 라이즈 플러그인 하이브리드', '쏘나타 뉴 라이즈 하이브리드', '쏠라티', '뉴 아반떼(AD)']
    AVAN_DICT= {'1.6 GDi Style':53089,'1.6 GDi Value Plus':53091, '1.6 GDi Smart':53092, '1.6 GDi Modern':53093, '1.6 GDi Premium':53094, '1.6 VGT Style':53096, '1.6 VGT Smart':53098, '1.6 VGT Smart Special':53099, '1.6 VGT Premium':53100, '1.6 T-GDi SPORT':53101, '1.6 T-GDi SPORT 7DCT':53102, '1.6 T-GDi SPORT Extreme Selection':53103, '1.6 T-GDi SPORT Original':53104 }
    AVAN = ['1.6 GDi Style','1.6 GDi Value Plus', '1.6 GDi Smart', '1.6 GDi Modern', '1.6 GDi Premium', '1.6 VGT Style', '1.6 VGT Smart', '1.6 VGT Smart Special', '1.6 VGT Premium', '1.6 T-GDi SPORT', '1.6 T-GDi SPORT 7DCT', '1.6 T-GDi SPORT Extreme Selection', '1.6 T-GDi SPORT Original']
    button_info = ['견적내기', '컨텐츠 조회', '문의하기','취소하기']
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    msgRtnType = body.get('type')
    msgRtnContent = body.get('content')
    msgRtnUserKey = body.get('user_key')

    print("@ b.type(): "+ msgRtnType)
    print("@ b.content(): "+ msgRtnContent)
    print("@ b.user_key(): "+ msgRtnUserKey)

    #camessage = CaMessage(userkey=msgRtnUserKey, msgtype=msgRtnType, message=msgRtnContent, updatedate=timezone.now(), inputdate=timezone.now())
    #camessage.save()

    if "문의하기" in msgRtnContent:
        response = '<카이즈유>' + '\n' + '카이즈유에게 바라는점이 있으면 아래의 링크를 클릭해주세요'
        return JsonResponse({
                'message': {
                    'text': response,
                    'photo': {
                        'url': 'http://file.carisyou.com/upload/2017/05/15/FILE_201705150608369290.jpg',
                        'width': 640,
                        'height': 480
                    },
                    'message_button': {
                        'label': '사이트 구경하기',
                        'url': 'http://m.carisyou.co.kr'
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['견적내기', '컨텐츠 조회', '문의하기']
            }
        })

    if "취소하기" in msgRtnContent:
        return JsonResponse({
            'message': {
                'text' : '취소되었습니다.',
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : button_info
            }
        })

    if "컨텐츠 조회" in msgRtnContent:
        return JsonResponse({
            'message': {
                'text': '원하는 기능을 선택하세요',
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['등록순위','통계보기', '이벤트']
            }
        })

    if "견적내기" in msgRtnContent:
        return JsonResponse({
            'message' : {
                'text' : '카이즈유 챗봇을 이용해주셔서 감사합니다.\n우선 국산차, 수입차를 선택해주세요.',
                'photo' : {
                    'url' : 'http://file.carisyou.com/upload/2017/02/28/FILE_201702280247178240.jpg',
                    'width' : 640,
                    'height' : 480,
                },
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['국산차', '수입차']
            }
        })

    if "국산차" in msgRtnContent:
        return JsonResponse({
            'message': {
                'text' : '국산차를 선택하셨군요.\n다음으로 브랜드를 선택해주세요'
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['현대자동차', '기아자동차', '취소하기']
            }
        })

    if "수입차" in msgRtnContent:
        return JsonResponse({
            'message': {
                'text' : '수입차를 선택하셨군요.\n다음으로 브랜드를 선택해주세요'
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['폭스바겐', 'BMW', '취소하기']
            }
        })

    if '멜론검색:' in msgRtnContent:
        query = msgRtnContent[6:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + functions.melon_search(query)

        return JsonResponse({
            'message': {
                'text' : response,
            },
        })

    if msgRtnContent in eun:
        car_brand = msgRtnContent
        response = functions.car_brandname(car_brand)
        return JsonResponse({
            'message': {
                'text' : '카이즈유에서 견적을 보고싶은 자동차의 차종명을 입력해주세요~\n차종명을 정확히 입력해주셔야 제가 알아들을 수 있어요~\n' + response + '\n' + '\nex)뉴 i30(PD), 그랜저 하이브리드(HG) 등',
            },
        })

    if msgRtnContent in hyundai:
        car_type = msgRtnContent
        response = functions.car_type1(car_type)

        return JsonResponse({
            'message': {
                'text': '등급명 : 기본 차량 가격\n' + response,
            },
        })

    if msgRtnContent in AVAN:
        car_price = msgRtnContent
        response = functions.Car_Price(car_price)
        url1 = functions.Car_PriceUrl(car_price)
        return JsonResponse({
                'message': {
                    'text' : '현대 2017 뉴 아반떼(AD)\n' + car_price + '\n' + response,
                    'photo' : {
                        'url' : 'http://file.carisyou.com/newcar/color/5117_hyundai_newavante2016_100.png',
                        'width' : 640,
                        'height' : 480
                    },
                    'message_button' : {
                        'label' : '상세견적보러가기',
                        'url' : url1 ,
                    }
                },
                'keyboard' : {
                    'type' : 'buttons',
                    'buttons' : button_info
            }
        })


    if "등록순위" in msgRtnContent:
        name = msgRtnContent
        response = functions.car_rank(name)

        return JsonResponse({
                'message': {
                    'text': '국내차 등록순위' + response,
                    'photo': {
                        'url' : 'http://file.carisyou.com/upload/2017/09/07/FILE_201709070226435330.jpg',
                        'width' : 640,
                        'height' : 480
                    },
                    'message_button': {
                        'label': '등록순위',
                        'url': 'http://www.carisyou.com/theme/top10/63?selectedYear=&selectedMonth=00&pageIndex=1'
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['등록순위','통계보기', '이벤트', '취소하기']
            }
        })

        '''
        return JsonResponse({
            'message' : {
                'text' : '국내차 등록순위' + response ,
            },
            'message_button': {
                'label': '등록순위',
                'url': 'http://m.carisyou.co.kr'
            },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : button_info
            }
        })
        '''
    if "통계보기" in msgRtnContent:
        return JsonResponse({
            'message': {
                'text' : '카이즈유 통계',
                'photo': {
                    'url' : 'http://image.kyobobook.co.kr/images/book/large/970/l1400000281970.jpg',
                    'width' : 640,
                    'height' : 480
                },
                'message_button' : {
                    'label' : '통계보기',
                    'url' : 'http://m.carisyou.com/magazine/STATS'
                }
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['등록순위','통계보기', '이벤트', '취소하기']
            }
        })

    if "이벤트" in msgRtnContent:
        return JsonResponse({
            'message' : {
                'photo' : {
                    'url' : 'http://file.carisyou.com/upload/2017/09/01/FILE_201709010921074070.jpg',
                    'width' : 640,
                    'height' : 480
                },
                'message_button' : {
                    'label' : '이벤트 참여하기',
                    'url' : 'http://www.carisyou.com/event/ing'
                }
            },
            'keyboard' : {
                'type' : 'buttons',
                'buttons' : ['등록순위','통계보기', '이벤트', '취소하기']
            }
        })

    else :
        return JsonResponse({
            'message': {
                'text' : '잘못된 접근입니다.'
            },
            'keyboard' : {
                'type': 'buttons',
                'buttons' : button_info
            }
        })

    rows = CaMessage.objects.filter(message='네') #DB내용찾기-filtering


    print("-----------------  RtnVal  ---------------------")
    #print(RtnVal)
    print("------------------------------------------------")
    return HttpResponse(json.dumps(msgRtnContent))

@csrf_exempt
def friendpage(request):
    print("###---<<<  friendpage  >>>---###")
    print("@request.method : "+ request.method)
    print("@HttpRequest.path_info : "+ request.path_info)

    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        msgRtnUserKey = body.get('user_key')

        keyfriend = CaKeyfriend(userkey=msgRtnUserKey, updatedate=timezone.now(), inputdate=timezone.now())
        keyfriend.save()
        print("@@--<< 추가된 친구입니다.: "+ msgRtnUserKey)
    elif request.method == 'DELETE':
        print("@@--<< 차단된 친구입니다. : "+ request.path)
    else:
        print("@@--<< 정의되지 않은 접근입니다.. : "+ request.path)

    return HttpResponse({})

@csrf_exempt
def chatroompage(request):
    print("###---<<<  chatroompage  >>>---###")
    print("@request.method : "+ request.method)
    print("@HttpRequest.path_info : "+ request.path_info)

    #user_key = request.GET.get('request.path_info')
    chatroom = CaChatroom(userkey=request.path_info, updatedate=timezone.now(), inputdate=timezone.now())
    chatroom.save()

    if request.method == 'DELETE':
        print("@@--<< 채팅방을 나갔습니다. "+  request.path)
    else:
        print("@@--<< 정의되지 않은 접근입니다.. : "+ request.path)

    return HttpResponse({})
