import ctypes
import os

from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from common.models import User
from config import my_settings
from .models import Portfolio, Order, Category
from django.core.paginator import Paginator
import json


def index(request):
    return render(request, 'body/main.html')


def portfolio(request):
    """ 포트폴리오 페이지 """
    return render(request, 'navbar/portfolio/portfolio.html')


def portfolioDesign(request):
    """ 포트폴리오 - 제품 디자인 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=1).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/design.html', context)


def portfolioMachineDesign(request):
    """ 포트폴리오 - 기계시스템 설계 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=2).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/machine_design.html', context)


def portfolioHWmachine(request):
    """ 포트폴리오 - H/W 기구설계 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=3).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/HW_machine.html', context)


def portfolio3d(request):
    """ 포트폴리오 - 3D 프린팅 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=4).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/3d.html', context)


def portfolioMockup(request):
    """ 포트폴리오 - 목업 CNC 가공 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=5).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/mockup.html', context)


def portfolioCnc(request):
    """ 포트폴리오 - 부품 CNC 가공 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=6).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/cnc.html', context)


def portfolioSdm(request):
    """ 포트폴리오 - Smart Digital Mold 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=7).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/sdm.html', context)


def portfolioMold(request):
    """ 포트폴리오 - 금형 제작 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=8).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/mold.html', context)


def portfolioInjectionMolding(request):
    """ 포트폴리오 - 사출 성형 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=9).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/injection_molding.html', context)


def portfolioEquipmentDesign(request):
    """ 포트폴리오 - 판금 절곡 페이지 """
    portfolio_list = Portfolio.objects.filter(category_index=10).order_by('board_index')

    # 페이징
    page = request.GET.get('page', '1')
    paginator = Paginator(portfolio_list, 8)
    page_obj = paginator.get_page(page)

    context = {'portfolio_list': page_obj}
    return render(request, 'navbar/portfolio/equipment_design.html', context)


def reviewBest(request):
    """ 후기 - 베스트후기 페이지 """
    return render(request, 'navbar/review/review_best.html')


def reviewRecent(request):
    """ 후기 - 최신순 페이지 """
    return render(request, 'navbar/review/review_recent.html')


def reviewHighRating(request):
    """ 후기 - 높은평점순 페이지 """
    return render(request, 'navbar/review/review_high_rating.html')


def reviewLowRating(request):
    """ 후기 - 낮은평점순 페이지 """
    return render(request, 'navbar/review/review_low_rating.html')


def body_onlyIdea_onlyIdea(request):
    # onlyIdea 메인
    return render(request, 'body/onlyIdea/onlyIdea_home.html')


def onlyIdea_detail(request):
    # onlyIdea 상세설명

    return render(request, 'body/onlyIdea/onlyIdea_detail.html')


def body_prototyping_prototyping_home(request):
    # 시제품 제작 메인
    return render(request, 'body/prototyping/prototyping_home.html')


def prototyping_detail(request):
    # 시제품 상세설명
    return render(request, 'body/prototyping/prototyping_detail.html')


def navbar_about_ceo(request):
    return render(request, 'navbar/about/ceo.html')


def navbar_about_history(request):
    return render(request, 'navbar/about/history.html')


def navbar_about_ideology(request):
    return render(request, 'navbar/about/ideology.html')


def navbar_about_route(request):
    return render(request, 'navbar/about/route.html')


def navbar_about_test(request):
    return render(request, 'navbar/about/test.html')


def body_production_home(request):
    # 양산 홈
    return render(request, 'body/production/production_home.html')


def production_detail(request):
    # 양산 상세설명
    return render(request, 'body/production/production_detail.html')


# ##### 주문 페이지 #####
def order_home(request):
    return render(request, 'order/order_home.html')


def order_confirmation(request):
    return render(request, 'order/order_confirmation.html')


def order_form_onlyIdea(request):
    if request.method == "POST":
        method = request.POST.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_onlyIdea.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_onlyIdea.html')


def order_form_prototyping(request):
    if request.method == "POST":
        method = request.POST.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_prototyping.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_prototyping.html')


def order_form_production(request):
    if request.method == "POST":
        method = request.POST.get('method', False)
        context = {'method': method}
        contextDict = json.dumps(context)
        return render(request, 'order/order_form_production.html', {'contextDict': contextDict})

    return render(request, 'order/order_form_production.html')


# 주문서 내용을 DB로 저장하는 함수
def make_order_form(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']  # 회사명
        business_num = request.POST['business_num']  # 사업자 등록번호
        name = request.POST['name']  # 담당자
        email = request.POST['email']  # 이메일
        phone_num = request.POST['phone_num']  # 연락처
        title = request.POST['title']  # 제품 제목
        description = request.POST['description']  # 제품 설명
        material = request.POST['material']  # 소재
        quantity = request.POST['quantity']  # 제품 수량
        size = request.POST['size']  # 크기(가로/세로/높이)
        path = request.POST['input_file']  # 파일(경로?)
        etc = request.POST['etc']  # 기타
        category_index = request.POST['category_index']  # 카테고리 인덱스
        userid = request.POST['userid']  # 사용자 아이디
        print(path)
        

        # category_index와 매칭되는 한글 이름 출력
        category = Category.objects.get(category_index=category_index)

        # userid DB 있다면
        if User.objects.filter(userid=userid).exists():
            # 받아온 정보로 Order 객체 생성
            order = Order.objects.create(
                company_name=company_name,
                business_num=business_num,
                name=name,
                email=email,
                phone_num=phone_num,
                title=title,
                description=description,
                material=material,
                quantity=quantity,
                size=size,
                path=path,
                etc=etc,
                category_index=category,
                userid=User.objects.get(userid=userid)
            )
            order.save()

            # 이메일 전송
            mail = EmailMessage(subject='주문서입니다.',
                                body=f'주문 들어왔습니다.\n\n'
                                     f'<<주문자 정보>>\n'
                                     f'담당자: {name}\n'
                                     f'이메일: {email}\n'
                                     f'연락처: {phone_num}\n\n'
                                     f'회사명: {company_name}\n'
                                     f'사업자 등록번호: {business_num}\n\n'
                                     f'유형: {category.category_sub}\n\n'
                                     f'제품 제목: {title}\n'
                                     f'제품 설명: {description}\n'
                                     f'소재: {material}\n'
                                     f'제품 수량: {quantity}\n'
                                     f'크기(가로/세로/높이): {size}\n'
                                     f'기타: {etc}',
                                to=[my_settings.EMAIL['EMAIL_HOST_USER']]
                                )

            # mail.attach_file(path)
            mail.send()

            return render(request, 'order/order_confirmation.html', {'order': order,
                                                                     'category_sub': category.category_sub})
        # 뒤로가기 문제
        else:
            # print('잘못된 접근입니다.')
            # ctypes.windll.user32.MessageBoxW(0, '잘못된 접근입니다.', '주문서 창            ')
            return redirect('/')
    # 뒤로가기 문제
    else:
        # print('잘못된 접근입니다.')
        # ctypes.windll.user32.MessageBoxW(0, '잘못된 접근입니다.', '에러 창            ')
        return redirect('/')


# ##### 마이페이지 #####
def mypage_home(request):
    return render(request, 'navbar/mypage/mypage_home.html')


def mypage_order_history(request):
    return render(request, 'navbar/mypage/mypage_order_history.html')


def mypage_update_info(request):
    return render(request, 'navbar/mypage/mypage_update_info.html')


def mypage_info(request):
    return render(request, 'navbar/mypage/mypage_info.html')
