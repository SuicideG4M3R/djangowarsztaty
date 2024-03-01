from django.urls import path
from .views import MyHome, RoomList, AddRoom, RoomDetail, RoomModify, RoomDelete, RoomReserve, MyTime

urlpatterns = [
    path('', MyHome.as_view(), name='index.html'),
    path('room/list/', RoomList.as_view(), name='room_list'),
    path('add/new/', AddRoom.as_view(), name='add_room'),
    path('room/<int:id>/', RoomDetail.as_view(), name='room_detail'),
    path('room/modify/<int:id>/', RoomModify.as_view(), name='room_modify'),
    path('room/delete/<int:id>/', RoomDelete.as_view(), name='room_delete'),
    path('room/reserve/<int:id>/', RoomReserve.as_view(), name='room_reserve'),
    path('time/', MyTime.as_view())
]
