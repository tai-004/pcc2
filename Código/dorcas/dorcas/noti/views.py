from django.shortcuts import render, redirect

from noti.models import Notifications

# Create your views here.

def ShowNotifications(request):
    user = request.user
    notifications = Notifications.objects.filter(user=user).order_by('-date')
    Notifications.objects.filter(user=user, is_seen=False).update(is_seen=True)

    context = {
        'notifications': notifications
    }

    return render(request, 'notifications.html', context)
