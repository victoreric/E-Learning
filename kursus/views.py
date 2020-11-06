from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Materi
from .forms import MateriForm

from django.contrib.auth import authenticate, login, logout

#with template base view
from django.views.generic import ListView, DetailView

from django.db.models import Q

def search(request):
    # ini for cari samua judul
    queryMateri = Materi.objects.all()
   
    queryCariJudul = request.GET.get('kolomCari')
    # print(queryCariJudul) 

    # ini for pilih-pilih judul saja
    # if queryCariJudul != '' and queryCariJudul is not None :
    #     queryMateri = queryMateri.filter(judul__icontains =queryCariJudul) 
    if queryCariJudul != '' and queryCariJudul is not None :
            queryMateri = queryMateri.filter(Q(judul__icontains = queryCariJudul)| Q(penulis__icontains = queryCariJudul) | Q(kategori__icontains = queryCariJudul)).distinct() 
     
    # print(queryMateri) 

    context = {
        'page_title' : 'Search Materi', 
        'queryset' :  queryMateri
    }
    return render(request,"kursus/search.html", context)


def LoginView(request):
    context= {
        'page_title' : 'войдите',  
    }
    user = None
    if request.method == 'POST' :
        # print(request.POST)
        username_login = request.POST['username']
        password_login = request.POST['password']
        # print(username_login)
        # print (password_login)
        #melakukan authenticate dengan database
        user = authenticate(username = username_login, password = password_login)
        # print(user)
        # melakukan login
        # menampilkan tulisan user di halaman html
        if user is not None :
            login(request, user)
            return redirect('kursus:list')
        else  :
            return redirect('kursus:login')

    #membuat kondisi jika user telah login
    # dan iseng mengetik login di urlbar.. pretlah
    if request.method == 'GET':
        if request.user.is_authenticated:
            # logika untuk user
            return redirect('kursus:list')
        # else :
             # logika untuk anonymous
    return render (request,'kursus/login.html', context)

@login_required
def LogoutView(request):
    context ={
        'page_title' : 'Logout'
    }
    if request.method == 'POST' :
        # print(request.POST)
        if request.POST['Logout'] == 'Да':
            # print('Proses logout')
            logout(request)
        return redirect('kursus:list')

    return render (request, 'kursus/logout.html', context)
   
# class MateriDeleteView(DeleteView):
#     model = Materi
#     template_name = "kursus/Materi_confim_delete.html"
#     success_url = reverse_lazy('kursus:manage')

@login_required
def MateriDelete(request, pk):
    item = Materi.objects.filter(id=pk)
    # print(item)
    context = {
        'page_title' : 'подтверждения Удаления ',
        'item' : item,
    }
    if request.method == 'POST' :
        Materi.objects.filter(id=pk).delete()
        return redirect('kursus:manage')
    
    return render (request, 'kursus/Materi_confim_delete.html', context)
    


# class MateriEditView(UpdateView):
#     model = Materi
#     template_name = "kursus/Materi_manage_edit.html"
#     form_class = MateriForm

@login_required
def MateriEdit(request, pk):
    Materi_update = Materi.objects.get(id=pk)
    
    data = {
        'judul'   : Materi_update.judul,
        'isi'     : Materi_update.isi,
        'kategori': Materi_update.kategori 
    }
    Materi_form = MateriForm(request.POST or None, initial = data, instance=Materi_update)
    
    if request.method == 'POST' :
        if Materi_form.is_valid():
            Materi_form.save()
        return redirect ('kursus:list')

    context = {
        "page_title" : 'Обновлять Статья',
        "form" : Materi_form,
    }
    
    return render(request,"kursus/Materi_create.html", context)
    

# class MateriManageView(ListView):
#     model = Materi
#     template_name = "kursus/Materi_manage.html"
#     extra_context ={
#         'page_title' : 'Manage Materi'
#     }
#     ordering = ['-published']
@login_required
def MateriManage(request):
    daftar_materi = Materi.objects.all().order_by('-published')
    
    context ={
        'page_title' : 'Упавления статьи',
        'daftar_materi' : daftar_materi,
    }
    
    
    return render (request, "kursus/Materi_manage.html", context )

# class MateriCreateView(CreateView):
    # from .forms import MateriForm
    # form_class  = MateriForm
    # template_name = "kursus/Materi_create.html"
    # model = Materi
    # fields = [
    #         'judul',
    #         'isi',
    #         'kategori',
    #         'penulis'
    #     ]
    # extra_context = {
    #     'page_title' : 'Create Materi'
    # }

@login_required
def MateriCreate (request):
    form = MateriForm(request.POST or None)

    if request.method == 'POST' :
        if form.is_valid():
            form.save()
        return redirect ('kursus:list')

    context ={
        'page_title' : 'Создания Статьи ',
        'form' : form,
    }
    return render(request,'kursus/Materi_create.html', context)
    
    
    
class MateriDetailView(DetailView):
    model = Materi
    template_name = "kursus/Materi_detail.html"

    extra_context = {
        'page_title' : 'Детаил'
    }
    #Menampilkan pilihan kategori di sisi kiri
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat= True).distinct()
        # print(kategori_list)
        self.kwargs.update({'kategori_list' : kategori_list}) 
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)



class MateriKategoriListView(ListView):
    model = Materi
    template_name = "kursus/Materi_kategori_list.html"
    ordering = ['-published']
 
    # menampilkan materi berdasarkan kategori
    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori = self.kwargs['kategori_input'])
        print(len(self.queryset))
        # print(self.kwargs)
        return super().get_queryset()

    #Menampilkan pilihan kategori di sisi kiri
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat= True).distinct(). exclude(kategori= self.kwargs['kategori_input'])
       
        self.kwargs.update({'kategori_list' : kategori_list}) 
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)

        
class MateriListView(ListView):
    # show all materi (object_list)
    model = Materi
    template_name = "kursus/Materi_list_anonymous.html"
    ordering = ['-published']
    # paginate_by = 2
    extra_context = {
        'page_title' : 'Списоков Статьи Materi',
    }

    #Menampilkan pilihan kategori di sisi kiri
    def get_context_data(self, *args, **kwargs):
        kategori_list = self.model.objects.values_list('kategori', flat= True).distinct()
        
        self.kwargs.update({'kategori_list' : kategori_list}) 
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
