from django.urls import path

from . import views

app_name = 'itrencotech'

urlpatterns = [
    path('', views.index, name='index'),
    
    # 로그인
    path('login/', views.login, name='login'),   # 로그인 페이지
    path('login/signUp/', views.signUp, name='signUp'), # 회원가입 페이지
    path('login/findIdPasswd/', views.findIdPasswd, name='findIdPasswd'),  # ID찾기/비밀번호 찾기 선택
    path('login/findId/', views.findId, name='findId'),  # ID찾기
    
    # 포트폴리오
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/machineDesign', views.portfolioMachineDesign, name='portfolio_machine_design'), # 기계 설계
    path('portfolio/design', views.portfolioDesign, name='portfolio_design'),  # 제품 디자인
    path('portfolio/3d', views.portfolio3d, name='portfolio_3d'), # 3D 프린팅

    path('portfolio/mockup', views.portfolioMockup, name='portfolio_mockup'),  # 목업
    path('portfolio/cnc', views.portfolioCnc, name='portfolio_cnc'), # CNC 가공
    path('portfolio/equipmentDesign', views.portfolioEquipmentDesign, name='portfolio_equipment_design'),  # 판금 절곡
    path('portfolio/mold', views.portfolioMold, name='portfolio_mold'), # 사출 금형
    
    # 고객 후기
    path('review/best', views.reviewBest, name='review_best'), # 베스트 후기
    path('review/recent', views.reviewRecent, name='review_recent'), # 최신순
    path('review/highRating', views.reviewHighRating, name='review_high_rating'), # 평점높은순
    path('review/lowRating', views.reviewLowRating, name='review_low_rating'), # 평점낮은순

    # ONLY IDEA, 시제품 제작
    path('onlyIdea/onlyIdea_home/', views.body_onlyIdea_onlyIdea, name='onlyIdea'),
    path('prototyping/prototyping_home/', views.body_prototyping_prototyping_home, name='prototyping'),

    path('onlyIdea/onlyIdea_mechanical_design/',
            views.body_onlyIdea_onlyIdea_mechanical_design, name='mechanical_design'), # 기계설계
    path('onlyIdea/onlyIdea_production_design/',
            views.body_onlyIdea_onlyIdea_production_design, name='production_design'), # 제품디자인
    
    path('prototyping/3DPrinting/', views.body_prototyping_3Dprinting, name='3Dprinting'), # 3D 프린팅
    path('prototyping/mockUp/', views.body_prototyping_mockUp, name='mockUp'), # 목업
    path('prototyping/CNC/', views.body_prototyping_CNC, name='CNC'), # CNC 가공
    path('prototyping/sheeting_bending/', 
            views.body_prototyping_sheeting_bending, name='sheeting_bending'),  # 판금 절곡

    # 양산
    path('production/home', views.body_production_home, name='body_production_home'),
    path('production/mold/', views.body_production_mold, name='body_production_mold'),
    path('production/cnc/', views.body_production_cnc, name='body_production_cnc'),
    path('production/press/', views.body_production_press, name='body_production_press'),

    # 회사 소개
    path('about/ceo/', views.navbar_about_ceo, name='navbar_about_ceo'),
    path('about/history/', views.navbar_about_history, name='navbar_about_history'),
    path('about/ideology/', views.navbar_about_ideology, name='navbar_about_ideology'),
    path('about/route/', views.navbar_about_route, name='navbar_about_route'),
    path('about/test/', views.navbar_about_test, name='navbar_about_test'),

    # 주문
    path('order/order_home/', views.order_home, name='order_home'),
    path('order/order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order/order_form_onlyIdea/', views.order_form_onlyIdea, name='order_form_onlyIdea'),
    path('order/order_form_prototyping/', views.order_form_prototyping, name='order_form_prototyping'),
    path('order/order_form_production/', views.order_form_production, name='order_form_production'),


]
