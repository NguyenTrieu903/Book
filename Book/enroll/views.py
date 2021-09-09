from django import forms
from django.shortcuts import render, redirect
from .forms import ManagebookForm
from .models import ManageBook
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.


def emp(request):
    if request.method == "POST":
        form = ManagebookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
                # return redirect('/')

            except:
                pass
    else:
        form = ManagebookForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    context = {'show': ManageBook.objects.all()}
    return render(request, "show.html", context)


def edit(request, id):
    book = ManageBook.objects.get(pk=id)
    return render(request, 'edit.html', {'book': book})


def update(request, id):
    book = ManageBook.objects.get(pk=id)
    form = ManagebookForm(request.POST, instance=book)
    if form.is_valid:
        form.save()
        return redirect("/show")
        # return redirect('/')
    return render(request, 'edit.html', {'book': book})


def destroy(request, id):
    book = ManageBook.objects.get(pk=id)
    book.delete()
    return redirect("/show")
    # return redirect('/')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/show')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, "auth/login.html")

    context = {}
    return render(request, "auth/login.html", context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginpage')
    context = {'form': form}
    return render(request, "auth/register.html", context)
