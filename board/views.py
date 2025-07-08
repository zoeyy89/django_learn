from django.shortcuts import render, redirect
from .models import Message

def message_list(request):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        Message.objects.create(name=name, content=content)
        return redirect("board:message_list")
    messages = Message.objects.all().order_by("-created_at")
    return render(request, "board/list.html", {"messages": messages})
