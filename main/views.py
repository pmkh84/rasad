from django.shortcuts import render, redirect
from .models import member_data, PresenceRecord, form_info, admin_data
from .form import form_type, presance_form, login
from django.forms import formset_factory
import urllib
def main_page(request):

    members = member_data.objects.order_by('member_sedigh')
    initial_data = [{'member': m.id} for m in members]

    PresenceFormSet = formset_factory(presance_form, extra=len(initial_data))

    if request.method == 'POST':
        formset = PresenceFormSet(request.POST)
        type_form = form_type(request.POST)
        if formset.is_valid() and type_form.is_valid():
            type_f = request.POST.get('type_choice')
            date_f = request.POST.get('forms_date')
            entry = form_info(form_type = type_f, form_date =date_f )
            entry.save()
            for form in formset:
                print(form.cleaned_data)
            for form in formset:
                cd = form.cleaned_data
                member = cd.get('member')
                present = cd.get('present', False)
                if member:
                    PresenceRecord.objects.create(member=member, present=present)
            return redirect('download_scv')  # نام درست در urls.py
    else:
        formset = PresenceFormSet(initial=initial_data)

    type_form = form_type()
    paired_data = zip(members, formset.forms)

    return render(request, 'home.html', {
        'formset': formset,
        'type': type_form,
        'pairs': paired_data
    })
import csv
from django.http import HttpResponse
from .models import PresenceRecord

  # ساخت فایل CSV برای دانلود
import csv
from django.http import HttpResponse
from .models import PresenceRecord

def export_present_members(request):
    # فقط اعضای حاضر
    present_records = PresenceRecord.objects.filter(present=True)
    file_name = form_info.objects.order_by('-id').first()
    file_nam = str(form_info.objects.order_by('-id').first())
    file_date = str(file_name.form_date)
    print(file_name)
    # آماده‌سازی فایل برای دانلود
    safe_file_name = urllib.parse.quote(f"{file_nam} {file_date}.csv")

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f"attachment; filename*=UTF-8''{safe_file_name}"

    writer = csv.writer(response)
    writer.writerow(['نام عضو'])  # فقط عنوان ستون

    for record in present_records:
        writer.writerow([record.member.member_name])
    return response    
    # پاک‌سازی پس از دانلود

   # present_records.delete()

    return response
def finish(request):   
    if request.method == 'POST':
        PASSWORD = 'sedigh_rasad(313)'
        #رمز واردشده
        U_pass = request.POST.get('pass_word')
        #نام کاربر
        U_name = request.POST.get('name')
        if U_pass == PASSWORD:
            user = admin_data(admin_name = U_name)
            user.save()
            return redirect('members')
        else:
            return redirect('done')
    if request.method == 'GET':    
        present_records = PresenceRecord.objects.filter(present=True)
        present_records.delete()
        login_form = login 
        return render(request, "finish.html", {'login': login_form})
