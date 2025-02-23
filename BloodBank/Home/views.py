# from django.shortcuts import render , redirect
# from Home.models import Donor
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate , login , logout 
# from django.contrib.auth.decorators import login_required 

# @login_required(login_url='/login-page/')
# def main_page(request):
#     return render(request , 'index.html')
# # def register_p(request):
# #     return render(request , 'blood.html')
# def contact_page(request):
#     return render(request , 'contact.html')
# def about_page(request):
#     return render(request , 'about.html')

# @login_required(login_url='')    
# def search_page(request):
#     context = {}
#     if request.GET.get('donor_bloodtype') :
#         queryset = Donor.objects.all()
#         queryset = queryset.filter(donor_bloodtype__icontains = request.GET.get('donor_bloodtype'), donor_city__icontains=request.GET.get('donor_city'))
#         context = {'donors': queryset}

#     return render(request , 'search.html', context)


from django.shortcuts import render, redirect
from Home.models import Donor
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail

from Home.utils import send_email_to_donor



@login_required(login_url='')  
def main_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Message from {user_email}"
            body = f"\nEmail: {user_email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                user_email,  # Visitor's email (optional)
                ['zaeempathan11@gmail.com'],  # Your email (where you receive messages)
                fail_silently=True,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('main-page')  # Redirect back to the contact page

    else:
        print("the form was invalid")
        form = ContactForm()

    return render(request, "index.html", {"form": form})

# def contact_page(request):
#     if request.method == "POST":
#         donor_email = request.POST.get("email")
#         donor_message = request.POST.get("message")
#         if donor_email:
#             send_email_to_donor(donor_email, donor_message)
#             return redirect("search-page")
#     return render(request, 'contact.html')

def about_page(request):
    return render(request, 'about.html')

# def send_email(request, donor_email):
#     send_email_to_donor(donor_email = donor_email)
#     return redirect('/search-page/')

@login_required(login_url='')  # Fix empty login_url
def search_page(request):
    context = {}

    if request.GET.get('donor_bloodtype') or request.GET.get('donor_city'):
        queryset = Donor.objects.all()

        # Filter only if values exist
        blood_type = request.GET.get('donor_bloodtype')
        city = request.GET.get('donor_city')

        if blood_type:
            queryset = queryset.filter(donor_bloodtype__icontains=blood_type)
        if city:
            queryset = queryset.filter(donor_city__icontains=city)

        context = {'donors': queryset}

    return render(request, 'search.html', context)




# def register_p(request):
#     if request.method == "POST":
#         data = request.POST
#         donor_name = data.get('donor_name')
#         donor_email = data.get('donor_email')
#         donor_phone  = data.get('donor_phone')
#         donor_bloodtype = data.get('donor_bloodtype')
#         donor_pass = data.get('donor_pass')
#         donor_city = data.get('donor_city')

#         Donor.objects.create(
#             donor_email = donor_email,
#             donor_name = donor_name,
#             donor_phone = donor_phone,
#             donor_bloodtype = donor_bloodtype,
#             donor_city = donor_city
#         )

#         user = User.objects.filter(username = donor_name)

#         if user.exists():
#             messages.info(request, "username already taken")
#             return redirect("/register-p/")

#         user=User.objects.create(
#           username = donor_name
#         )
#         user.set_password(donor_pass) #for encrypting the pass in django we use set_password 
#         user.save()
#         messages.info(request, "account created succesfully")
#         return redirect('/')
        
#     return render(request,'blood.html')
    
#     def register_p(request):
#         return redirect('/register-p/')


def register_p(request):
    if request.method == "POST":
        data = request.POST
        donor_name = data.get('donor_name')
        donor_email = data.get('donor_email')
        donor_phone = data.get('donor_phone')
        donor_bloodtype = data.get('donor_bloodtype')
        donor_pass = data.get('donor_pass')
        donor_city = data.get('donor_city')

        # Check if the username already exists
        # if User.objects.filter(username=donor_name).exists():
        #     messages.error(request, "Username already taken")
        #     return redirect("/")
        if User.objects.filter(username=donor_email).exists():
            messages.error(request, "Email already taken, you are Already a User")
            return redirect("/")

        # Create the User first
        user = User.objects.create_user(username=donor_email, password=donor_pass)
        user.save()

        # Now create the Donor instance
        donor = Donor.objects.create(
            user=user,  # Linking Donor to User model
            donor_email=donor_email,
            donor_name=donor_name,
            donor_phone=donor_phone,
            donor_bloodtype=donor_bloodtype,
            donor_city=donor_city
        )
        messages.error(request, "Registered Successfully")
        return redirect('/')
        

    return render(request, 'blood.html')


# def login_page(request):
#     if request.method == 'POST':
#         donor_name = request.POST.get("donor_name")
#         donor_pass = request.POST.get("donor_pass")

#         if not User.objects.filter(username = donor_name).exists():
#             messages.error(request, "donor name does not exist")
#             return redirect("/")

#         zn = authenticate(username = donor_name , password = donor_pass)

#         if zn is None :
#             messages.error(request, "wrong password")
#             return redirect("/")
#         else :
#             login(request, zn)
#             return redirect("/main-page/")

#     return render(request,'login.html')

def login_page(request):
    if request.method == 'POST':
        donor_email = request.POST.get("donor_email")
        donor_pass = request.POST.get("donor_pass")

        user = authenticate(username=donor_email, password=donor_pass)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("/")

        login(request, user)
        #  messages.error(request, "Email already taken, you are Already a User")
        return redirect("/main-page/")

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('/')



from django.core.mail import send_mail
from django.conf import settings

def send_email_to_donor(donor_email , donor_message):
    """
    Sends an email to the donor when a user requests contact.
    """
    subject = "Blood Donation Request"
    message = (donor_message)
    print(f"the email is being send to to {donor_email}")
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Sender email from settings
        [donor_email],  # Dynamic recipient
        fail_silently=True,  # Set to True to suppress errors
    )
    return redirect("search-page")

def send_email(request , email):
    context = {"email":email}
    if request.method == "POST":
        donor_email = email
        donor_message = request.POST.get("message")
        if donor_email:
            send_email_to_donor(donor_email, donor_message)
            return redirect("search-page")
    
    
    return render(request , "blood-request.html" , context)

from .forms import ContactForm

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = f"New Contact Message from{name} "
            body = f"\nEmail: {user_email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                user_email,  # Visitor's email (optional)
                ['zaeempathan11@gmail.com'],  # Your email (where you receive messages)
                fail_silently=True,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact-page')  # Redirect back to the contact page

    else:
        print("the form was invalid")
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
