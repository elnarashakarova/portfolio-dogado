from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Certificates, Projects
# Portfolio

def index(request):

    # Home
    #home = Home.objects.latest('updated')    ### original code was just this line for home
    
    try:
        home = Home.objects.latest('updated')
    except Home.DoesNotExist:
        home = None

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    #portfolios = Portfolio.objects.all()
    
    # Projects
    projects = Projects.objects.all()
    
    # Certificate
    certificates = Certificates.objects.all()
    

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'projects': projects,
        'certificates': certificates,
        #'portfolios': portfolios
    }


    return render(request, 'index.html', context)
