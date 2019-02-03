from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUp,EditForm
from .models import Ticket,User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render_to_response
from .forms import ModeDate



def index(request):
    form=ModeDate()
    return render(request,'index.html',{'form': form})

#Функция поиска. Тот самый гет запрос после которого авторизованный пользователь перестает таковым быть.
def search(request):
    if 'q' and 'a' and 't' in request.GET and request.GET['q'] and request.GET['a'] and request.GET['t']:
        q = request.GET['q']
        a = request.GET['a']
        t = request.GET['t']
        tickets = Ticket.objects.filter(arpoint__icontains=q,dpoint__icontains=a,adate__exact=t,status__exact='a')
        return render_to_response('search_result.html',
                                  {'tickets': tickets, 'query': q,'a':a,'time':t})
    else:
        return HttpResponse('Please submit a search term.')

#Функция, которая подразумевает, что я беру ячейку ticket.place из таблицы из шаблона search_result,
# и билет с таким номером места у меня привязывается к текущему пользователю и меняет status с а на b
def book(request):
    obj=Ticket.objects.filter(place=int(request.GET["place"]))
    obj.update(status='b')
    obj.update(user=request.user)
    obj.save()
    return render(request,'alltickets.html')
class Books(LoginRequiredMixin, generic.ListView):
    model = Ticket
    template_name = 'alltickets.html'
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user,status__exact='b')
def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUp()
    return render(request, 'signup.html', {'form': form})

def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('alltickets')
    else:
        form=EditForm(instance=request.user)
    return render(request,'profile_edit.html',{'form':form})

