from django.shortcuts import render,redirect,HttpResponse
from .models import Enrollment,CertificateRequest
from .forms import certificate_form,Create_Account_Form,login_form
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.http import FileResponse
# from django.shortcuts import get_object_or_404
# from .models import CertificateRequest


# Create your views here.


def Create_Account(request):
    try:
        if request.method == "POST":
            uname = request.POST.get('username')
            email = request.POST.get('email')
            passw = request.POST.get('password')
            print(uname,email,passw)
        
        try:

            if User.objects.filter(username=uname).first():
                messages.success(request,'username is taken')

            if User.objects.filter(email=email).first():
                messages.success(request,'email is taken')
            
            else:
                user = User(username=uname,email=email)
                user.set_password(passw)
                user.save()
                messages.success(request,'Account created !!')


        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
  
    return render(request,'create_account.html')


def login_handle(request):


    try:

        if request.method == "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username,password)
           
            if not username or not password:
                messages.success(request,'Boths fields are required !')

            user_obj = User.objects.filter(username=username).first()
            user = authenticate(username=username,password=password)

            if user_obj is None:
                messages.success(request,'User Not found !')
            print(user_obj)

            if user is not None:
                login(request,user)
                return redirect('/form/')
            
            if user is None:
                messages.success(request,'Wrong Password !!')

        
    except Exception as e:
        print(e)

    return render(request,'Login.html')


@login_required(login_url='/')
def logouthandle(request):

    try:

        logout(request)
    
    except Exception as e:
        print(e)

    return redirect("/")
    


@login_required(login_url='/')
def certificate_output(request):
    # data = Enrollment.objects.filter(user=request.user)
    data = CertificateRequest.objects.filter(user = request.user,status = 'approved')
    print('this is my data>>>>',data)
    # for i in data:
    #     print(i.status)
    for i in data:
        if i.status == 'pending':
            return HttpResponse('certificate on process')
        
        if i.status == 'approved':
            return render(request,'regex_certificate.html',{'data':data})
        
        if i.status == 'denied':
            return HttpResponse('Your certificate process deninded')

        # print(data[0].status)

@login_required(login_url='/')
def certificateform(request):
    if request.method == "POST":
        form = certificate_form(request.POST)
        if form.is_valid():
            user = request.user
            course = form.cleaned_data['certification']
            enrollment_date = form.cleaned_data['enrollment_date']
            completion_date = form.cleaned_data['completion_date']
            
            if Enrollment.objects.filter(user=user,certification=course).first():
                messages.success(request,'This user and this ceritficate alraedy registered')
            
            else:

                Enrollment(user=user,certification=course,enrollment_date=enrollment_date,completion_date =completion_date).save()
                print(user,course,enrollment_date,completion_date)
                data = Enrollment.objects.filter(user=request.user,certification=course)
                return redirect(f'/certificate_request/{data[0].id}/')


    form = certificate_form()
    context = {

        'form':form
    }
    return render(request,'certification_form.html',context)


@login_required(login_url='/')
def certificate_request(request,id):
    data = Enrollment.objects.filter(id=id)
    print(data,'<<<<data')
    print(data[0].user)
    print(data[0].certification)
    from datetime import date

    a = date.today()
    b = str(a)
    c = b.split('-')
    c[2] = str(Enrollment.objects.filter(user=request.user)[0].id)
    d = 'REG/OTF/'+'/'.join(c)


    CertificateRequest(user=data[0].user,certification = data[0].certification,enrollment=data[0],status = 'pending',issuing_authority = d).save()

    return redirect('/certificate/')



# def download_certificate(request, certificate_id):
#     certificate = get_object_or_404(CertificateRequest, pk=certificate_id)
#     certificate_file_path = certificate.file.path  # Replace with the actual file path
#     response = FileResponse(open(certificate_file_path, 'rb'))
#     response['Content-Type'] = 'application/pdf'  # Set the appropriate content type
#     response['Content-Disposition'] = f'attachment; filename="{certificate.title}.pdf"'

#     return response






   


