from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def LogInView(request):
    if request.user.is_authenticated:
        return redirect('about_us_url')
    if request.method == 'GET':
        return render(request=request, template_name='log_in.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        # authenticate - Делает запрос в БД, ищет пользователя с таким username, хэширует пароль и сравнивает.
        # Если данные верны, то мы получим объект user. Если нет, то None.
        if user is not None:
            login(request, user)
            # login - регистрирует юзера в системе как юзера который уже вошел и выдает ему sessionid.
            # sessionid и csrftoken Джанго хранит в БД в своей таблице. После выхода из системы, он их удаляет.
            return redirect('about_us_url')
        return redirect('log_in_url')


def LogOutView(request):
    if request.user.is_authenticated:
        logout(request)
        # logout - находит связанные с юзером sessionid и csrftoken и удаляет их из БД.
    return redirect('log_in_url')

