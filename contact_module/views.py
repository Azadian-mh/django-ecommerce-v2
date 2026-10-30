from msilib.schema import ListView

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfil
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView


# Create your views here.

class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_module.html'
    success_url = '/contact-us'

    def get_context_data(self, *args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


def stor_file(file):
    with open('temp/image.png', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfil
    fields = '__all__'
    success_url = '/contact-us/create-profile/'


class ProfilesView(ListView):
    model = UserProfil
    template_name ='contact_module/profiles_list_page.html'
    context_object_name = 'profiles'




    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, 'contact_module/create_profile_page.html',
    #                   {'form': form})
    #
    #
    # def post(self, request):
    #     submitted_form = ProfileForm(request.POST, request.FILES)
    #     if submitted_form.is_valid():
    #         # stor_file(request.FILES['Profiles'])
    #         profile = UserProfil(image=request.FILES["user_image"])
    #         profile.save()
    #         return redirect('/contact-us/create-profile/')
    #
    #     return render(request, 'contact_module/create_profile_page.html',
    #                   {'form': submitted_form})









# def contact_us_page(request):
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             # print(contact_form.cleaned_data)
#             # contact = ContactUs(
#             #     title=contact_form.cleaned_data.get('title'),
#             #     full_name=contact_form.cleaned_data.get('full_name'),
#             #     email=contact_form.cleaned_data.get('email'),
#             #     message=contact_form.cleaned_data.get('message'),
#             # )
#             # contact.save()
#             contact_form.save()
#             return redirect('home_page')
#     else:
#         # contact_form = ContactUsForm()
#           contact_form = ContactUsModelForm()
#
#
#     return render(request, 'contact_module/contact_us_module.html',{
#         'contact_form': contact_form,
#     })





