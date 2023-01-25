from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import *
from django.template import loader



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password2')
        password = request.POST.get('password')
        select_va=request.POST.get('select')
        file=request.FILES.get('file')

        if password == password1 :
            insert=Userone(name=name,email=email,gender=select_va,password=password1,username=username,avatar=file)
            insert.save()
            return redirect('log')
        else:
            return HttpResponse('password does not match!!!!')
    return render(request,'register.html')



def log(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('pass')
        check_user=Userone.objects.filter(username=uname,password=passw)
        check_admin = adminpage.objects.filter(user_name=uname, password=passw)
        if check_user:
            for user in check_user:
                request.session['id']=user.id
                return redirect('home',request.session['id'])
        elif check_admin:
            for admin in check_admin:

                request.session['id']=admin.id
                return redirect('homeadmin')
        else:
            errors=[]
            errors.append('!!!!Please enter valid username or password!!!!')
            return render(request,'login.html',{'errors':errors})
    return render(request,'login.html')

def homeadmin(request):
    return render(request,'homeadmin.html')

def logout(request):
    try:
        del request.session['id']
    except:
        return redirect('log')
    return redirect('log')


def home(request,pk):
    if 'id' in request.session:
        current_user=request.session['id']
        user_obj=get_object_or_404(Userone,id=current_user)
        query = request.POST.get('s')
        qs = game_details.objects.all()

        if query is not None:
            qs = qs.filter(game_name__icontains=query)

            return render(request, 'home.html', {'objlist': qs})
        return render(request,'home.html',{'user':user_obj,'objlist':game_details.objects.all()})

def feedbacks(request,pk):
    user_obj = get_object_or_404(Userone, id=request.session['id'])
    if request.method == 'POST':
        i = feedback(feedbacks=request.POST.get('fd'), name=user_obj, reply=0)
        i.save()
        return redirect(home,user_obj.id)
    return render(request,'feedbacks.html',{'user':user_obj.id})
def viewgames(request):
    query = request.POST.get('s')
    qs = game_details.objects.all()

    if query is not None:
        qs = qs.filter(game_name__icontains=query)
        return render(request, 'games.html', { 'cat': qs})
    return render(request, 'games.html', { 'cat': game_details.objects.all()})


def payment(request,pk):
    dataa = game_details.objects.get(pk=pk)
    user = Userone.objects.get(pk=request.session['id'])
    if request.method=='POST':
        if len(request.POST.get('cvc'))==3 and len(request.POST.get('name'))>=4 and len(request.POST.get('id'))==12 :
            data=Payment_details(card_holder_name=request.POST.get('name'),card_number=request.POST.get('id'),card_cvc=request.POST.get('cvc'),card_year=request.POST.get('year'),email=user,game_name=dataa)
            data.save()
            return redirect('processing',dataa.id)
        else:
            messages.success(request,'!!!!! Enter valid details !!!!!!')
            return render(request,'payment.html',{'game':dataa})
    return render(request,'payment.html',{'card':Payment_details.objects.filter(email=user.id),'game':dataa,'user':user.id})


def profile(request,pk):
    context={'objectlist':get_object_or_404(Userone,pk=pk)}
    return render(request,'view_profile.html',context)


def update_profile(request,pk):
    get_obj =  get_object_or_404(Userone, pk=pk)
    templates = loader.get_template('update.html')
    if request.method=='POST':
        Userone.objects.filter(id=get_obj.id).update(name=request.POST.get('name'),gender=request.POST.get('gender'),email=request.POST.get('mail'))
        messages.info(request,'Updated profile successfully')
        return redirect('profile',pk)
    return HttpResponse(templates.render({'form':get_obj,'user':get_obj.id},request))

def changepro(request,pk):
    get_obj = get_object_or_404(Userone, pk=pk)
    if request.method == 'POST':
        get_obj.avatar = request.FILES.get('file')
        get_obj.save()
        return redirect(profile, get_obj.id)
    return render(request, 'changepic.html', {'user': get_obj.id})

def update_password(request,pk):
    get_obj =  get_object_or_404(Userone, pk=pk)
    templates=loader.get_template('update.html')
    if request.method=='POST':
        if request.POST.get('cpass')==get_obj.password:
            messages.info(request, "Incorrect Password")
            if request.POST.get('pass') == request.POST.get('pass1'):
                Userone.objects.filter(id=get_obj.id).update(password=request.POST.get('pass1'))
                messages.info(request,"Password Changed successfully")
                return redirect('profile',pk)
            else:
                messages.info(request, "Password do not match")

    return HttpResponse(templates.render({'form1':get_obj,'user':get_obj.id},request))

def creategame(request):
    if request.method == 'POST':
        game_name=request.POST.get('name')
        game_video1 = request.FILES.get('video1')
        game_video2 = request.FILES.get('video2')
        game_file= request.FILES.get('file')
        game_amt = request.POST.get('amt')
        game_avatar = request.FILES.get('avatar')
        game_image = request.FILES.get('image')
        game_type = request.POST.get('select')

        if game_type == 'free':
            p=game_details(game_amt='0',game_type=game_type,game_name=game_name,game_video1=game_video1,game_video2=game_video2,game_avatar=game_avatar,game_file=game_file,game_images=game_image)
            p.save()
        else:
            p=game_details(game_amt=game_amt,game_type=game_type,game_name=game_name,game_video1=game_video1,game_video2=game_video2,game_avatar=game_avatar,game_file=game_file,game_images=game_image)
            p.save()
    return render(request,'creategame.html')



def editgame(request,pk):
    get_obje=get_object_or_404(game_details,pk=pk)
    # get_instance=GameForm(instance=get_obj)
    templates = loader.get_template('editgame.html')
    context={
        'game':get_obje,
    }

    if request.method=='POST':
        game_name = request.POST.get('name')
        # game_video1 = request.FILES.get('video1')
        # game_video2 = request.FILES.get('video2')
        # game_file = request.FILES.get('file')
        game_amt = request.POST.get('amt')
        # game_avatar = request.FILES.get('avatar')
        # game_image = request.FILES.get('image')
        game_type = request.POST.get('select')

        if game_type == 'free':
            game_details.objects.filter(id=get_obje.id).update(game_amt='0', game_type=game_type, game_name=game_name)

            messages.success(request, 'game updated......')
        elif game_type == 'paid':
            game_details.objects.filter(id=get_obje.id).update(game_amt=game_amt, game_type=game_type, game_name=game_name)
            messages.success(request, 'game updated......')
        else:
            messages.success(request, 'Could not update......')
        return redirect('homeadmin')
    return HttpResponse(templates.render(context,request))

def avatar(request,pk):
    get_obj = get_object_or_404(game_details, pk=pk)
    if request.method == 'POST':
        get_obj.game_avatar = request.FILES.get('file')
        get_obj.save()
        return redirect(editgame, get_obj.id)
    return render(request,'changeavatar.html',{'avatar':get_obj.game_avatar})

def file(request,pk):
    get_obj = get_object_or_404(game_details, pk=pk)
    if request.method == 'POST':
        get_obj.game_file = request.FILES.get('file')
        get_obj.save()
        return redirect(editgame, get_obj.id)
    return render(request,'changeavatar.html',{'file':get_obj.game_file})

def image(request,pk):
    get_obj = get_object_or_404(game_details, pk=pk)
    if request.method == 'POST':
        get_obj.game_images = request.FILES.get('file')
        get_obj.save()
        return redirect(editgame, get_obj.id)
    return render(request,'changeavatar.html',{'image':get_obj.game_images})

def v1(request,pk):
    get_obj = get_object_or_404(game_details, pk=pk)
    if request.method == 'POST':
        get_obj.game_video1 = request.FILES.get('file')
        get_obj.save()
        return redirect(editgame, get_obj.id)
    return render(request,'changeavatar.html',{'v1':get_obj.game_video1})

def v2(request,pk):
    get_obj = get_object_or_404(game_details, pk=pk)
    if request.method == 'POST':
        get_obj.game_video2 = request.FILES.get('file')
        get_obj.save()
        return redirect(editgame, get_obj.id)
    return render(request,'changeavatar.html',{'v2':get_obj.game_video2})


def deletegame(request,pk):
    del_obj = get_object_or_404(game_details,pk=pk)
    if del_obj:
        del_obj.delete()
        messages.error(request,"Successfully Deleted")
        return redirect('viewgames')
    messages.error('Could not delete these app')
    return redirect('creategame')

def feeds(request):
    # feedback.objects.filter(reply=0).update(reply=2)
    return render(request,'feedbackadmin.html',{'feedback':feedback.objects.all().order_by('feedbacks')})

def feedss(request,pk):
    # feedback.objects.filter(id=pk).update(reply=2)
    return render(request,'feedbackadmin.html',{'feedback':feedback.objects.all().order_by('feedbacks')})

def gamepage(request,pk):
    game= get_object_or_404(game_details, pk=pk)
    user = get_object_or_404(Userone, pk=request.session['id'])
    game1 = get_object_or_404(game_details, pk=pk)
    rev = review.objects.filter(game_name=game1.id)

    return render(request,'usergamepage.html',{'game':game,'rev':rev,'user':user.id,})

def deletereview(request,pk):
    rev=review.objects.get(pk=pk)
    obj=rev.game_name.id
    if rev:
        rev.delete()
        messages.success(request, 'Deleted Successfully')
        return redirect('gamepage',obj)
    else:
        messages.error(request, 'Occured error during deletion ')
        return redirect('gamepage', obj)


def processing(request,pk):

    return render(request,'processing.html', {'pro':game_details.objects.get(id=pk),'user':get_object_or_404(Userone, pk=request.session['id'])})

def processing1(request, pk):
    game= game_details.objects.get(pk=pk)
    user=get_object_or_404(Userone,id=request.session['id'])
    u=Account.objects.get(email=user.id)
    s=int(game.game_amt)

    p=int(u.bal)
    if  s<=p :
        up=p-s
        acc=Account.objects.filter(id=u.id).update(bal=up)
        return redirect('paid',game.id)
    elif s>p:
        messages.error(request,'######## Insufficient Balance #########')
        return redirect('home',user.id)

def paid(request,pk):
    user = get_object_or_404(Userone, pk=request.session['id'])
    return render(request,'paid.html',{'game':game_details.objects.get(pk=pk),'user':user.id})


def reviews(request,pk):
    user = get_object_or_404(Userone, pk=request.session['id'])
    game = get_object_or_404(game_details, pk=pk)
    if request.method=='POST':
        d=review(game_name=game,review=request.POST.get('txt'),reply_review='0',name=user)
        d.save()
        return redirect('gamepage',game.id)
    return render(request,'review.html',{'user':user.id})