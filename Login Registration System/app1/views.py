from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import UserProfile
from .forms import UserProfileForm, ContactForm

# Your views here

# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()

            # Create a UserProfile instance and link it to the user
            user_profile = UserProfile(user=my_user)
            user_profile.save()
            
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def UserProfileView(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=username)
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user': user,
        'user_profile': user_profile,
        'form': form,
    }

    return render(request, 'user_profile.html', context)


def edit_profile_view(request):
    # Retrieve the currently logged-in user
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=user.username)
    else:
        form = UserProfileForm(instance=user.userprofile)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'edit_profile.html', context)

def about_page_view(request):
    return render(request, 'about.html')


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This will save the data to the Contact model
            # You can add a success message or redirect to a thank you page here
            return redirect('thank_you')  # You can replace 'thank_you' with the appropriate URL

    # If the request method is not POST or the form is not valid, render the contact page with the form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
