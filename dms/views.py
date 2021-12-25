from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView, UpdateView
from django.contrib import messages
import pytesseract

try:
    from PIL import Image
except:
    import Image
from .forms import *
import datetime


def index(request):
    if request.user.is_authenticated:
        mail_list = Mails.objects.all()
        template = loader.get_template('mail_list.html')
        context = {
            'mail_list': mail_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')


# Create your noviews here.
def image_upload(request):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        if request.method == 'POST':
            form = MailForm(request.POST, request.FILES)
            if form.is_valid():
                # print(form.cleaned_data['mail_scan'])
                added_mail = form.save()
                if added_mail.mail_scan:
                    pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
                    content = pytesseract.image_to_string(Image.open(added_mail.mail_scan), lang='ara')
                    print(content)
                    added_mail.mail_text = content
                    added_mail.save()
                messages.success(request, "تم حفظ البريد الجديد")
                return redirect('success')
        else:
            form = MailForm()
        return render(request, 'addDoc.html', {'form': form, 'title': 'بريد جديد', 'btntitle': 'حفظ'})


class MailCreatView(CreateView):
    model = Mails
    form_class = MailForm
    template_name = 'addDoc.html'


def logout():
    return redirect('login.html')


def login():
    return redirect('login.html')


def success(request):
    form = MailForm()
    return render(request, 'addDoc.html', {'form': form, 'title': 'بريد جديد', 'btntitle': 'حفظ'})
    # return HttpResponse('successfully uploaded')


def success_edit(request):
    form = MailForm()
    # return render(request, 'addDoc.html', {'form': form, 'title': 'تعديل بريد', 'btntitle': 'حفظ التعديل'})
    return redirect('index')


def readOCR(request, mail_id):
    mail = get_object_or_404(Mails, pk=mail_id)
    pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
    content = pytesseract.image_to_string(Image.open(mail.mail_scan), lang='ara')
    return HttpResponse(content)


def view_img_form(request, img_url):
    return render(request, 'form_img.html', {'img_url': img_url})


def about(request):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        time = datetime.datetime.now()
        return render(request, 'about.html', {'time': time})


def table(request):
    if request.user.is_authenticated:
        mail_list = Mails.objects.all()
        template = loader.get_template('tables.html')
        context = {
            'mail_list': mail_list,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')


def detail(request, mail_id):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        mail = get_object_or_404(Mails, pk=mail_id)
        return HttpResponse("You're looking at detail mail %s." % mail.mail_type)


def mail_edit(request, mail_id):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        if request.method == 'POST':
            mail = Mails.objects.get(pk=mail_id)
            form = MailForm(request.POST, request.FILES, instance=mail)
            if form.is_valid():
                edited_mail = form.save()
                messages.success(request, "تم تعديل البريد بنجاح")
                # pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'
                # content = pytesseract.image_to_string(Image.open(edited_mail.mail_scan), lang='ara')
                # edited_mail.mail_text = content
                # edited_mail.save()
                return redirect('success_edit')
        else:
            mail = get_object_or_404(Mails, pk=mail_id)
            form = MailForm(instance=mail)
            return render(request, 'addDoc.html', {'form': form, 'title': 'تعديل بريد', 'btntitle': 'حفظ التعديل'})

        # return render(request, 'edit_mail.html', {'mail': mail})


def mail_remove(request, mail_id):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        mail = get_object_or_404(Mails, pk=mail_id)
        # return render(request, 'remove_mail.html', {'mail': mail})
        return HttpResponse("تم الحذف بنجاح %s." % mail.mail_title)


def mail_delete(request, mail_id):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        mail = get_object_or_404(Mails, pk=mail_id)
        return render(request, 'delete_mail.html', {'mail': mail})


def view_img(request, mail_id):
    if not request.user.is_authenticated:
        messages.success(request, "يجب تسجيل الدخول اولا")
        return redirect('login')
    else:
        mail = get_object_or_404(Mails, pk=mail_id)
        return render(request, 'print_img.html', {'mail': mail})


class DetailView(generic.DetailView):
    model = Mails
    template_name = 'edit_mail.html'


class MailsDeleteView(DeleteView):
    # specify the model you want to use
    model = Mails
    template_name = 'confirm_delete.html'

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "../../"
