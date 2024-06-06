"""ds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ds_app import views

urlpatterns = [
    path('admin_home', views.admin_home),
    path('blockaunb', views.blockaunb),
    path('blockaunbExp', views.blockaunbExp),
    path('expertreg', views.expertreg),
    path('feedback', views.feedback),
    path('', views.login),
    path('manage_expert', views.manage_expert),
    path('reply', views.reply),
    path('verify_doc', views.verify_doc),
    path('complaints', views.complaints),
    path('login_code', views.login_code),
    path('logout', views.logout),
    path('view_user', views.view_user),
    path('exper_code',views.exper_code),
    path('manage_expert_search',views.manage_expert_search),
    path('verify_doc_search',views.verify_doc_search),
    path('feedback_search',views.feedback_search),
    path('docreg',views.docreg),
    path('doctor_code',views.doctor_code),
    path('view_user_search',views.view_user_search),
    path(' blockaunbExp_search',views. blockaunbExp_search),
    path('blockaunb_search',views.blockaunb_search),
    path('complaints_search',views.complaints_search),
    path('manage_expert_edit_post',views.manage_expert_edit_post),
    path('manage_expert_delete/<id>',views.manage_expert_delete),
    path('manage_expert_edit/<id>',views.manage_expert_edit),
    path('blockaunb_block/<id>',views.blockaunb_block),
    path('blockaunb_unblock/<id>',views.blockaunb_unblock),
    path('blockaunbExp_block/<id>',views.blockaunbExp_block),
    path('blockaunbExp_unblock/<id>', views.blockaunbExp_unblock),
    path('verify_doc_accept/<id>', views.verify_doc_accept),
    path('verify_doc_reject/<id>', views.verify_doc_reject),
    path('user_accept/<id>', views.user_accept),
    path('user_reject/<id>', views.user_reject),
    path('adminreply/<id>',views.adminreply),
    path('reply_post',views.reply_post),
    path('expert_home',views.expert_home),
    path('doctor_home',views.doctor_home),
    path('manage_tips',views.manage_tips),
    path('manage_tips_post',views.manage_tips_post),
    path('manage_tip_delete/<id>',views.manage_tip_delete),
    path('view_doubt',views.view_doubt),
    path('searchdoubt',views.searchdoubt),
    path('sendreplycode',views.sendreplycode),
    path('sendreply/<int:id>',views.sendreply),
    path('manage_schedule',views.manage_schedule),
    path('prescription/<int:id>',views.prescription),
    path('view_booking',views.view_booking),
    path('manage_schedule_post',views.manage_schedule_post),
    path('prescription_post',views.prescription_post),
    path('prescription_delete/<id>',views.prescription_delete),
    path('manage_schedule_delete/<id>',views.manage_schedule_delete),
    path('manage_schedule_edit/<int:id>',views.manage_schedule_edit),
    path('manage_schedule_edit_post',views.manage_schedule_edit_post),
    path('view_booking_delete/<id>',views.view_booking_delete),
    path('login_post',views.login_code1),
    path('register',views.registration),
    path('viewtips_app',views.viewtips_app),
    path('viewdoc',views.viewdoctor),
    path('viewdoctor_all',views.viewdoctor_all),
    path('schedules',views.viewshedule),
    path('viewreply',views.view_complaintreply),
    path('view_doubtreply',views.view_doubtreply),
    path('sendcomplaint',views.send_complaint_app),
    path('send_feedback_app',views.send_feedback_app),
    path('send_doubt_app',views.send_doubt_app),
    path('booking',views.booking),
    path('viewdep',views.viewdep),
    path('AV_symptoms',views.AV_symptoms),
    path('AV_symptoms1',views.AV_symptoms1),
    path('viewbooking',views.viewbooking),
    path('downloadprescription',views.downloadprescription),
    path('predict',views.predict),
    path('imagepredict',views.imagepredict),
    path('viewtips',views.viewtips),
    path('view_message2',views.view_message2),
    path('in_message2',views.in_message2),
    path('viewexpert',views.viewexpert),



path('chatwithuser', views.chatwithuser, name='chatwithuser'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),
    path('forgotpassword1',views.forgotpassword1),


]
