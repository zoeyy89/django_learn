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
