from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templates/index.html')

def add_expenses(request):
    return render(request,'templates/expenses/add-expenses.html')
