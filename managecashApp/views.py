from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,logout
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    forms = UserCreateForm()
    context = {
        'forms':forms,
        'title':'Registration',
        'btn':'Register',
    }
    
    return render(request,'auth/register.html',context)


def loginPage(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('addcash')
    
    forms = UserAuthenticationForm()
    context = {
        'forms':forms,
        'title':'Login in your account',
        'btn':'login',
    }
    
    return render(request,'auth/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
def addCashPage(request):
    if request.method == "POST":
        form = AddCashForm(request.POST)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.user = request.user
            cash.save()
            return redirect('dashboard')

    form = AddCashForm()

    context = {
        'form': form,
        'title': 'Add Cash',
        'btn': 'Add'
    }

    return render(request, 'pages/baseForm.html', context)

@login_required
def expensePage(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')

    form = ExpenseForm()  

    context = {
        'form': form,
        'title': 'Expense Form',
        'btn': 'Add'
    }
    
    return render(request, 'pages/baseForm.html', context)

@login_required
def dashboardPage(request):
    cash_entries = AddCashModel.objects.filter(user=request.user)
    expenses = ExpenseModel.objects.filter(user=request.user)
    total_income = cash_entries.aggregate(total=Sum('amount'))['total'] or 0
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense
    
    context = {
    'total_income': total_income,
    'total_expense': total_expense,
    'balance': balance,
}
    return render(request, 'pages/dashboard.html', context)