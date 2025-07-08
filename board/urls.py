from django.urls import path
from .views import message_list
from .views import message_list, MessageListCreateAPIView


app_name = 'board'

urlpatterns = [
    # 這裡的空字串 '' 代表 /，會對應到 message_list（HTML 頁面）
    path('', message_list, name='message_list'),
    path('api/messages/', MessageListCreateAPIView.as_view(), name='api_messages'),
]
