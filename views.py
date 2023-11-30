from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from patient_app.forms import UserInfoForm
from patient_app.models import UserInfo, Chats
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
import openai

openai.api_key = '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'

history = []

def get_info(request):
    form = UserInfoForm(request.POST or None)

    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.fields["user"] = request.user
            message = form.save(commit=False)
            message.save()
            return redirect("ask")
    else:
        return render(request, "patient_app/user_info.html", {"form": form})

def ask(request):

    User = get_object_or_404(UserInfo, pk = request.user)

    if request.method == "POST":
        question = request.POST.get('message')

        history.append({"role": "user", "content": question})
        render_to_string('patient_app/ask_page.html', {'history': history})

        assistant_role = "You are a helpful assistant for medical patients. You aid medical patients and refer them to doctors and resources \
                         but do not provide them with diagnoses. Answer in 100 words or less."
        assitant_intro = "Hello. I am your virtual health advisor."
        
        my_name = f"My name is '{User.name}"
        my_age = f"I am '{User.age}' years old"
        my_sex = ""
        if User.sex == 'm':
            my_sex = "I am a male"
        else:
            my_sex = "I am a female"
        my_location = f"I live in '{User.location}"
        my_conditions = f"I have these health conditions: '{User.health}'"

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "system", "content": assistant_role}, 
                                                                                    {"role": "assistant", "content": assitant_intro},
                                                                                    {"role": "user", "content": my_name}, {"role": "user", "content": my_age}, {"role": "user", "content": my_sex}, 
                                                                                    {"role": "user", "content": my_location}, {"role": "user", "content":my_conditions}, {"role": "user", "content": question}, *history], temperature = 0.5)
        #result = json.loads(response['choices'][0])

        history.append(response['choices'][0]['message'])
        print(response['choices'][0])
        
        return render(request, 'patient_app/ask_page.html', {'history': history})
    
    else:
        return render(request, "patient_app/ask_page.html")


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('info')
        
    else:
        form = UserCreationForm()
    return render(request, 'patient_app/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('ask')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'patient_app/login.html', {'error_message': error_message})
    else:
        return render(request, 'patient_app/login.html')

def home(request):
    return render(request, 'patient_app/home.html')

def contact_page(request):
    return render(request, 'patient_app/contact.html')

def about_page(request):
    return render(request, 'patient_app/about.html')

def logout_page(request):
    history.clear()
    auth.logout(request)
    logout_message = "You have been successfully logged out."
    return render(request, 'patient_app/home.html', {'logout_message': logout_message})

    
        
# Create your views here.
