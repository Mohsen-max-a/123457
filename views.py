from django.shortcuts import render,redirect
from .models import Your_Post,Photo
from .forms import UserName_Your1,Photo_Form
from django.contrib.auth.models import User
from .forms import User_serach_Form
from .models import CustomUser
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User_serach_Form

# Create your views here.
def game(request):
    get_post = Your_Post.objects.all()
    context = {
        "post": get_post
    } 

   
    return render(request,
                  "registration/index.html",context) 
def user_names(request):

    form = UserName_Your1()

    if request.method == "POST":

       form = UserName_Your1(request.POST)

  #  else:
       # form = UserName_Your(request.Post)
    if form.is_valid():
        date = form.cleaned_data
        User.objects.create_user(username=date["user_name"],email=date["email"],first_name=date["first_name"],last_name=date["last_name"],password="password_1")     
    context = {
        "form":form
    }    
    return render(request,"registration/login.html",context)
def upload_photo(request):
    context = {}
    if request.method == "POST":
        form = Photo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("photo_list")
        else:
            form = Photo_Form()
            context["form"]=form
    return render(request, "registration/upload.html", context)

def photo_list(request):
    get_image = Photo.objects.all()
    context = {"image": get_image}
    return render(request, "registration/photo_list.html", context)
def finish(request):
    get_post = Your_Post.objects.all()
    context = {
        "post": get_post
    } 
    return render(request, "registration/finished_proJect.html", context)
def serach_users(request):
    # views.py
    form = User_serach_Form()
    results = []

    if "query" in request.GET:
        form = User_serach_Form(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = CustomUser.objects.filter(
                Q(username__icontains=query) |
                Q(user_name__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )  # Adjust fields as necessary

    # Pagination
    paginator = Paginator(results, 10)  # Show 10 users per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"form": form, "page_obj": page_obj, "search": "search"}
    return render(request,"registration/search_users.html",context)