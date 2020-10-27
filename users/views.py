from django.shortcuts import render , HttpResponse ,HttpResponseRedirect,redirect , Http404
from django.views import generic
from .models import Profile
from django.views.generic import DetailView , UpdateView
from django.urls import reverse_lazy,reverse
from .forms import CreateUserForm ,UpdateProfileForm , UpdateUserForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import json


def UserRegisterView(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid() and ( form['first_name'].value() != '' and form['last_name'].value() != '' ):

            form.save()

            user =  get_object_or_404( User , username = form['username'].value() )


            profile = Profile.objects.create( user = user )
            profile.save()


            return HttpResponseRedirect(reverse('login'))


        errors = form.errors.as_json()

        if form['first_name'].value() == '' or form['last_name'].value() == '':
            errors = eval(errors)
            errors.update(  { 'last_name':[{'message':'First name and Last name requiered!'}] }  )
            errors = json.dumps( errors )

        
        return render( request , 'registration/register.html' , {'form': form, 'errors': errors } )

        
    form = CreateUserForm()
    return render( request , 'registration/register.html' , {'form': form} )


def ProfileDetailView( request , username ):

    user = get_object_or_404( User , username = username )

    profile = get_object_or_404( Profile , user = user )


    return render( request , 'registration/profile_detail.html' , {'profile':profile} )

@login_required( login_url= 'login')
def UpdateProfileView(request , username):

    if request.user.username != username:
        raise Http404

    errors = '' 
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid() and ( user_form['first_name'].value() != '' and user_form['last_name'].value() != '' ) :
            user_form.save()
            profile_form.save()
            return redirect('home')
        errors = 'Enter all requirements!'

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'errors' : errors
    }

    return render(request, 'registration/update_profile.html', context)

        




