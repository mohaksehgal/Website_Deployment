from django.urls import path
from . import views
from django.views.generic.base import TemplateView


app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    # path('logged/', views.logged_in, name='logged_in'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login1/', views.after_register, name='after_register'),
    path('clients/', views.clients, name='clients'),
    path('vision/', views.vision, name='vision'),
    path('principle/', views.principle, name='principle'),
    path('whatwedo/', views.whatwedo, name='whatwedo'),
    path('strength/', views.strength, name='strength'),
    # path('L_T_MIS/', views.L_T_MIS, name='L_T_MIS'),
    # path('L_T_BILLING/', views.L_T_BILLING, name='L_T_BILLING'),
    # path('L_T_SALARY/', views.MASTER_SALARY_TW, name='L_T_TW'),
    path('IDFC_TW_BILLING/', views.IDFC_TW_BILLING, name='IDFC_TW_BILLING'),
    path('login/IDFC_TW_MIS.html', views.IDFC_TW_MIS, name='IDFC_TW_MIS'),
    path('login/SLICE_CC_MIS.html', views.SLICE_MIS, name='SLICE_MIS'),
    path('IDFC_TW_SALARY/', views.MASTER_SALARY_TW, name='IDFC_TW_SALARY'),
    path('IDFC_TW_TC_SALARY/', views.IDFC_TW_SALARY_TC, name='IDFC_TW_SALARY_TC'),
    # path('L_T_TW_TC_SALARY/', views.L_T_TW_SALARY_TC, name='L_T_TW_SALARY_TC'),
    path('login/IDFC_HL_MIS.html', views.IDFC_HL_MIS, name='IDFC_HL_MIS'),
    # path('IDFC_HL_SALARY/', views.MASTER_SALARY_IDFC, name='IDFC_HL_SALARY'),
    path('IDFC_HL_BILLING/', views.IDFC_HL_BILLING, name='IDFC_HL_BILLING'),
    # path('FULLERTON_OTR_MIS/', views.FULLERTON_OTR_MIS, name='FULLERTON_OTR_MIS'),
    # path('FULLERTON_OTR_BILLING/', views.FULLERTON_OTR_BILLING, name='FULLERTON_OTR_BILLING'),
    path('FULLERTON_RECOVERY_MIS/', views.FULLERTON_RECOVERY_MIS, name='FULLERTON_RECOVERY_MIS'),
    # path('FULLERTON_RECOVERY_SALARY/', views.MASTER_SALARY_FULLERTON, name='MASTER_SALARY_FULLERTON'),
    path('FULLERTON_RECOVERY_BILLING/', views.FULLERTON_RECOVERY_BILLING, name='FULLERTON_RECOVERY_BILLING'),
    # path('FULLERTON_OTR_MIS/FULLERTON_FR_MIS/', views.FULLERTON_FR_MIS, name='FULLERTON_FR_MIS'),
    # path('FULLERTON_OTR_BILLING/FULLERTON_FR_BILLING', views.FULLERTON_FR_BILLING, name='FULLERTON_FR_BILLING'),
    path('login/BAJAJ_MIS.html', views.BAJAJ_MIS, name='BAJAJ_MIS'),
    path('login/MAGMA_MIS.html', views.MAGMA_MIS, name='MAGMA_MIS'),
    path('BAJAJ_PL_MIS/', views.BAJAJ_PL_MIS, name='BAJAJ_PL_MIS'),
    path('BAJAJ_CD_BILLING/', views.BAJAJ_BILLING, name='BAJAJ_BILLING'),
    path('MAGMA_BILLING/', views.MAGMA_BILLING, name='MAGMA_BILLING'),
    path('SLICE_CC_BILLING/', views.SLICE_BILLING, name='SLICE_BILLING'),
    # path('BAJAJ_CD_SALARY/', views.BAJAJ_SALARY, name='BAJAJ_SALARY'),
    path('Employee_database/', views.employee_database, name='employee_database'),
    # path('down/', views.L_T_PERFORMANCE_DOWNLOAD, name='L_T_DOWNLOAD'),
    path('down1/', views.IDFC_TW_PERFORMANCE_DOWNLOAD, name='IDFC_TW_DOWNLOAD'),
    path('down99/', views.IDFC_TW_MASTER_DOWNLOAD, name='IDFC_TW_MASTER_DOWNLOAD'),
    path('down2/', views.IDFC_HL_PERFORMANCE_DOWNLOAD, name='IDFC_HL_DOWNLOAD'),
    # path('down3/', views.FULLERTON_OTR_PERFORMANCE_DOWNLOAD, name='FULLERTON_OTR_DOWNLOAD'),
    # path('down4/', views.FULLERTON_RECOVERY_PERFORMANCE_DOWNLOAD, name='FULLERTON_RECOVERY_DOWNLOAD'),
    # path('down24/', views.FULLERTON_RECOVERY_BILLING_DOWNLOAD, name='FULLERTON_BILLING_DOWNLOAD'),
    # path('down25/', views.FULLERTON_RECOVERY_SALARY_DOWNLOAD, name='FULLERTON_SALARY_DOWNLOAD'),
    path('down5/', views.BAJAJ_CD_PERFORMANCE_DOWNLOAD, name='BAJAJ_CD_DOWNLOAD'),
    # path('down6/', views.L_T_BILLING_DOWNLOAD, name='L_T_BILLING_DOWNLOAD'),
    path('down7/', views.IDFC_TW_BILLING_DOWNLOAD, name='IDFC_TW_BILLING_DOWNLOAD'),
    path('down8/', views.IDFC_HL_BILLING_DOWNLOAD, name='IDFC_HL_BILLING_DOWNLOAD'),
    # path('down9/', views.FULLERTON_OTR_PERFORMANCE_DOWNLOAD, name='FULLERTON_OTR_DOWNLOAD'),
    # path('down10/', views.FULLERTON_RECOVERY_PERFORMANCE_DOWNLOAD, name='FULLERTON_RECOVERY_DOWNLOAD'),
    path('down11/', views.BAJAJ_CD_BILLING_DOWNLOAD, name='BAJAJ_CD_BILLING_DOWNLOAD'),
    # path('down12/', views.L_T_SALARY_FIXED_DOWNLOAD, name='L_T_SALARY_FIXED_DOWNLOAD'),
    # path('down13/', views.L_T_SALARY_INCENTIVE_PIVOT_DOWNLOAD, name='L_T_SALARY_INCENTIVE_PIVOT_DOWNLOAD'),
    # path('down14/', views.L_T_SALARY_INCENTIVE_DOWNLOAD, name='L_T_SALARY_INCENTIVE_DOWNLOAD'),
    path('down15/', views.IDFC_TW_SALARY_FIXED_DOWNLOAD, name='IDFC_TW_SALARY_FIXED_DOWNLOAD'),
    path('down16/', views.IDFC_TW_SALARY_INCENTIVE_PIVOT_DOWNLOAD, name='IDFC_TW_SALARY_INCENTIVE_PIVOT_DOWNLOAD'),
    path('down17/', views.IDFC_TW_SALARY_INCENTIVE_DOWNLOAD, name='IDFC_TW_SALARY_INCENTIVE_DOWNLOAD'),
    path('down18/', views.BAJAJ_CD_SALARY_DOWNLOAD, name='BAJAJ_CD_SALARY_DOWNLOAD'),
    path('down19/', views.IDFC_HL_SALARY_DOWNLOAD, name='IDFC_HL_SALARY_DOWNLOAD'),
    path('down20/', views.IDFC_HL_TL_INCENTIVE_DOWNLOAD, name='IDFC_HL_TL_INCENTIVE_DOWNLOAD'),
    path('down21/', views.IDFC_HL_FINAL_SALARY_INCENTIVE_DOWNLOAD, name='IDFC_HL_FINAL_SALARY_INCENTIVE_DOWNLOAD'),
    path('down22/', views.IDFC_TW_TC_SALARY_DOWNLOAD, name='IDFC_TW_TC_SALARY_DOWNLOAD'),
    path('down23/', views.BAJAJ_PL_BILLING_DOWNLOAD, name='BAJAJ_PL_BILLING_DOWNLOAD'),
    path('down24/', views.BAJAJ_PL_PERFORMANCE_DOWNLOAD, name='BAJAJ_PL_PERFORMANCE_DOWNLOAD'),
    path('down25/', views.BAJAJ_CD_MASTER_DOWNLOAD, name='BAJAJ_CD_MASTER_DOWNLOAD'),
    path('down26/', views.BAJAJ_PL_MASTER_DOWNLOAD, name='BAJAJ_PL_MASTER_DOWNLOAD'),
    # path('down23/', views.L_T_TC_SALARY_DOWNLOAD, name='L_T_TC_SALARY_DOWNLOAD'),
    path('login/NAV.html', views.NAV, name='NAV'),
    # path('login/salary.html', views.MASTER_SALARY_TW, name='L_T_TW'),
    path('bajaj_salary/', views.BAJAJ_SALARY, name='BAJAJ_SALARY'),
    path('login/bajaj_salary1.html', views.BAJAJ_PL_SALARY, name='BAJAJ_PL_SALARY'),
    # path('login/IDFC-HL_Salary.html', views.MASTER_SALARY_IDFC, name='IDFC_HL_SALARY'),
    path('IDFC-HL_Salary/', views.MASTER_SALARY_IDFC, name='IDFC_HL_SALARY'),
    # path('login/FULLERTON_RECOVERY_SALARY.html', views.MASTER_SALARY_FULLERTON, name='MASTER_SALARY_FULLERTON'),
    path('login/IDFC_TW_TL_ANALYSIS.html', views.IDFC_TW_TL_ANALYSIS, name='IDFC_TW_TL_ANALYSIS'),
    path('TL_SALARY/', views.IDFC_TW_TL_SALARY, name='IDFC_TW_TL_SALARY'),
    path('Active_IDFC_TW_employees/', views.IDFC_TW_EMPLOYEES, name='IDFC_TW_EMPLOYEES'),
    path('Active_FULLERTON_RECOVERY_employees/', views.FULLERTON_RECOVERY_EMPLOYEES, name='FULLERTON_RECOVERY_EMPLOYEES'),
    path('Active_IDFC_HL_employees/', views.IDFC_HL_EMPLOYEES, name='IDFC_HL_EMPLOYEES'),
    path('Active_BAJAJ_CD_employees/', views.BAJAJ_CD_EMPLOYEES, name='BAJAJ_CD_EMPLOYEES'),
    path('IDFC_TW_ANALYSIS/', views.IDFC_TW_ANALYSIS, name='IDFC_TW_ANALYSIS'),
    path('FULLERTON_RECOVERY_ANALYSIS/', views.FULLERTON_RECOVERY_ANALYSIS, name='FULLERTON_RECOVERY_ANALYSIS'),
    path('BAJAJ_CD_ANALYSIS/', views.BAJAJ_CD_ANALYSIS, name='BAJAJ_CD_ANALYSIS'),
    path('IDFC_HL_ANALYSIS/', views.IDFC_HL_ANALYSIS, name='IDFC_HL_ANALYSIS'),
]