from django.urls import path

from patient_data_app import views

urlpatterns=[

path('',views.home,name='home'),
path('login', views.login, name='login'),
path('logincode',views.logincode,name='logincode'),
path('forgot',views.forgot,name='forgot'),
path('forgot_password',views.forgot_password,name='forgot_password'),
path('fpwd1',views.fpwd1,name='fpwd1'),
path('resetForm',views.resetForm,name='resetForm'),
path('hosp_reg',views.hosp_reg,name='hosp_reg'),
path('hospitalreg', views.hospitalreg, name='hospitalreg'),
path('logout',views.logout,name='logout'),


path('ahome',views.ahome,name='ahome'),
path('hosp_verification',views.hosp_verification,name='hosp_verification'),
path('accpt_hosp/<int:id>',views.accpt_hosp,name='accpt_hosp'),
path('reject_hosp/<int:id>',views.reject_hosp,name='reject_hosp'),
path('hosp_verification_search',views.hosp_verification_search,name='hosp_verification_search'),
path('view_block_hosp',views.view_block_hosp,name='view_block_hosp'),
path('block_hosp/<int:id>',views.block_hosp,name='block_hosp'),
path('unblock_hosp/<int:id>',views.unblock_hosp,name='unblock_hosp'),
path('view_blockhosp_search',views.view_blockhosp_search,name='view_blockhosp_search'),

path('view_dr',views.view_dr,name='view_dr'),
path('view_dr_search',views.view_dr_search,name='view_dr_search'),
path('view_patient_ad',views.view_patient_ad,name='view_patient_ad'),
path('view_patient_search',views.view_patient_search,name='view_patient_search'),




path('hhome',views.hhome,name='hhome'),
path('update_profile',views.update_profile,name='update_profile'),
path('update_profile_action',views.update_profile_action,name='update_profile_action'),
path('mng_dep',views.mng_dep,name='mng_dep'),
path('search_mng_dep',views.search_mng_dep,name='search_mng_dep'),
path('add_dept',views.add_dept,name='add_dept'),
path('add_dept_action',views.add_dept_action,name='add_dept_action'),
path('edit_dept/<int:dept_id>',views.edit_dept,name='edit_dept'),
path('edit_dept_action',views.edit_dept_action,name='edit_dept_action'),
path('dlt_depart/<int:id>',views.dlt_depart,name='dlt_depart'),
path('mng_dr',views.mng_dr,name='mng_dr'),
path('add_dr',views.add_dr,name='add_dr'),
path('add_dr_action',views.add_dr_action,name='add_dr_action'),
path('edit_dr/<int:id>',views.edit_dr,name='edit_dr'),
path('edit_dr_action',views.edit_dr_action,name='edit_dr_action'),
path('dlt_dr/<int:id>',views.dlt_dr,name='dlt_dr'),
path('mng_dr_search',views.mng_dr_search,name='mng_dr_search'),
path('mng_app',views.mng_app,name='mng_app'),
path('mng_app_search',views.mng_app_search,name='mng_app_search'),
path('dlt_app/<int:id>',views.dlt_app,name='dlt_app'),
path('edit_app/<int:id>',views.edit_app,name='edit_app'),
path('breakdoc/<int:id>',views.breakdoc,name='breakdoc'),
path('joindoc/<int:id>',views.joindoc,name='joindoc'),
path('edit_app_action',views.edit_app_action,name='edit_app_action'),
path('pat_reg',views.pat_reg,name='pat_reg'),
path('view_pat',views.view_pat,name='view_pat'),
path('view_pat_search',views.view_pat_search,name='view_pat_search'),
path('add_app/<pid>',views.add_app,name='add_app'),
path('add_app_action',views.add_app_action,name='add_app_action'),
path('searchslot',views.searchslot,name='searchslot'),
path('seldoc',views.seldoc,name='seldoc'),
path('reg_code',views.reg_code,name='reg_code'),






path('dhome',views.dhome,name='dhome'),
path('edit_dr_self',views.edit_dr_self,name='edit_dr_self'),
path('edit_dr_action_self',views.edit_dr_action_self,name='edit_dr_action_self'),
path('add_record',views.add_record,name='add_record'),
path('add_record_action',views.add_record_action,name='add_record_action'),
path('view_appointment',views.view_appointment,name='view_appointment'),
path('view_appointment_search',views.view_appointment_search,name='view_appointment_search'),
path('view_pat_dr/<int:id>/<int:aid>',views.view_pat_dr,name='view_pat_dr'),
path('view_prev_rec/<int:id>',views.view_prev_rec,name='view_prev_rec'),
path('prev_rec_search',views.prev_rec_search,name='prev_rec_search'),
path('view_prev_rec1',views.view_prev_rec1,name='view_prev_rec1'),






path('and_logincode',views.and_logincode,name='and_logincode'),
path('and_reg_code',views.and_reg_code,name='and_reg_code'),
path('forgotpasss',views.forgotpasss,name='forgotpasss'),
path('and_viewappointment',views.and_viewappointment,name='and_viewappointment'),
path('verifyotp',views.verifyotp,name='verifyotp'),
path('accept_booking',views.accept_booking,name='accept_booking'),
path('view_prev_rec_and',views.view_prev_rec_and,name='view_prev_rec_and'),
path('prev_rec_search_and',views.prev_rec_search_and,name='prev_rec_search_and'),
path('prev_rec_search_andnew',views.prev_rec_search_andnew,name='prev_rec_search_andnew'),
path('and_update_profile',views.and_update_profile,name='and_update_profile'),
path('viewprofile',views.viewprofile,name='viewprofile'),



]