from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required

@login_required
def message_list(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.user = request.user
            msg.save()
            return redirect('board:message_list')
    else:
        form = MessageForm()

    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'board/list.html', {'form': form, 'messages': messages})


# 新增 API View 到 board/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MessageSerializer
from .service import get_all_messages, create_message

class MessageListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        messages = get_all_messages()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            create_message(user=request.user, content=serializer.validated_data['content'])
            return Response({"message": "留言成功"}, status=201)
        return Response(serializer.errors, status=400)
