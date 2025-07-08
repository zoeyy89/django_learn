from .models import Message

def get_all_messages():
    return Message.objects.all().order_by('-created_at')

def create_message(user, content):
    return Message.objects.create(user=user, content=content)