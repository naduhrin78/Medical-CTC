from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from md_ctc.forms import UserForm, ScanForm
from md_ctc.models import Scan
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout
from md_ctc.reports import check_for_contrast


def result(request):
    form = ScanForm(data=request.POST)
    user = request.user
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = user
        if 'fileUpload' in request.FILES:
            profile.ct_scan = request.FILES.get('fileUpload')

        else:
            return HttpResponseRedirect('/')

        profile.save()

        try:
            img_url = str(profile.ct_scan.url).split('/')[3]
            profile.cancer = check_for_contrast(img_url)

        except Exception as e:
            print(e.with_traceback())

        profile.save()

    else:
        print(form.errors)


def index(request):
    if request.method == 'POST':
        result(request)

    l = get_pics(str(request.user))
    context_dict = {}

    if l:
        context_dict={'scan_history': l}
    return render(request, 'md_ctc/index.html',context_dict)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ScanForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ScanForm(instance=request.user.profile)
    return render(request, 'md_ctc/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def get_pics(email):
    l = []
    for scan in Scan.objects.all():
        if str(scan.user) == email:
            try:
                l.append(scan)
            except:
                continue
    return l[::-1]


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
