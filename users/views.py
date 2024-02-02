from django.shortcuts import render
from users.models import CustomUser
from django.contrib.auth.models import Group
# Create your views here.
def change_user_role(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_role = request.POST.get('role')

        # Змінюємо роль користувача
        user = CustomUser.objects.get(email=email)
        user.role = new_role
        user.save()

    return render(request, 'change_role.html')

def add_user_to_group(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        group_name = request.POST.get('group_name')

        # Додаємо користувача до групи
        group = Group.objects.get(name=group_name)
        user = CustomUser.objects.get(email=email)
        group.user_set.add(user)

    return render(request, 'add_to_group.html')



user = CustomUser.objects.create_user(email='example@example.com', username='example_user', password='password123')

superuser = CustomUser.objects.create_superuser(email='admin@example.com', username='admin', password='adminpassword123')


user = CustomUser.objects.get(email='example@example.com')
user.role = 'admin'
user.save()

group = Group.objects.get(name='group_name')
user = CustomUser.objects.get(email='example@example.com')
group.user_set.add(user)
