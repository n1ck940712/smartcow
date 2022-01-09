from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import MyUser, Images, Annotation
from django.core import serializers
from django.utils.safestring import mark_safe
import json, csv

# main page
def index(request):
    if not request.user.is_authenticated:
        data = {
            'message': 'Login first.',
            'message_type': 'danger',
        }
        return redirect("signinfirst")
    else:
        if request.method == 'POST':
            for file in request.FILES.getlist('images'):
                Images.objects.create(user=request.user, file=file)
        images = Images.objects.filter(user=request.user)
        message = None
        data = {
            'user': request.user,
            'message': message,
            'images': images,
        }
        return render(request, "index.html", data)

def myannotated(request):
    if request.method == 'GET':
        images = Images.objects.filter(user=request.user, annotations__isnull=False)
        message = None
        data = {
            'user': request.user,
            'message': message,
            'images': images,
        }
        return render(request, "myannotated.html", data)

def annotate(request, img_id):
    if request.method == "GET":
        image = Images.objects.filter(pk=img_id)[0]
        if image.annotations:
            annotations = json.dumps(json.loads(image.annotations))
        else:
            annotations = None
        context = {
        "user": request.user,
        "image": image,
        "annotations": annotations,
        "message": None,
        }
        return render(request, "annotate.html", context)

def save_annotation(request):
    if request.method == "POST":
        img_id = request.POST.get('img_id')
        annotations_json = request.POST.get('annotations_json')
        annotations_json = mark_safe(annotations_json)
        image = Images.objects.get(id=img_id)
        image.annotations = annotations_json
        image.save()
        data = {
            'success': True,
            'message': '',

        }
    return JsonResponse(data)

def checkannotate(request, img_id):
    if request.method == "GET":
        image = Images.objects.filter(pk=img_id)[0]
        if image.annotations:
            annotations = json.dumps(json.loads(image.annotations))
        else:
            annotations = None
        context = {
        "user": request.user,
        "image": image,
        "annotations": annotations,
        "message": None,
        }
        return render(request, "checkannotate.html", context)


def download_csv(request):
    if request.method == 'POST':
        img_id = request.POST.get('img_id')
        image = Images.objects.get(pk=img_id)
        annotations = json.loads(image.annotations)
        response = HttpResponse(
            content_type='text/csv',
        )
        writer = csv.writer(response)
        for annotation in annotations:
            vehicle_type = annotation['body'][0]['value']
            coordinates = annotation['target']['selector']['value'].replace('xywh=pixel:', '').split(',')
            coordinates = [round(float(x), 1) for x in coordinates]
            coordinates.insert(0, str(image.file).split('/')[-1])
            coordinates.append(vehicle_type)
            writer.writerow(coordinates)
        
        return response


# user signin signout
def signin(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,email=email,password=password)
        if user:
            login(request,user)
            data = {
                "message":"Login successful",
                "message_type":'success'
            }
            return HttpResponseRedirect(reverse("index"))
        else:
            data = {
                "message":"asdfInvalid Credentials",
                "message_type":'danger'
            }
            return render(request, "login.html", data)
    return render(request, "login.html")

def signinfirst(request):
    data = {
        'message': 'Login first.',
        'message_type': 'danger',
    }
    return render(request, 'login.html', data)

def signout(request):
    logout(request)
    data = {
        'message':'Successfully logged out.',
        'message_type':'success'
    }
    return render(request, "login.html", data)

def register(request):
    reg_email = request.GET.get('reg_email')
    reg_password = request.GET.get('reg_password')
    reg_password2 = request.GET.get('reg_password2')
    reg_dob = request.GET.get('reg_dob')
    if not MyUser.objects.filter(email=reg_email).exists():
        if reg_password and reg_password2 and reg_password == reg_password2:
            newUser = MyUser.objects.create_user(email=reg_email,date_of_birth=reg_dob,password=reg_password)
            newUser.save()
            data = {
                'message': 'Registration successful. You can log in now.',
                'message_type': 'success',
            }
        else:
            data = {
                'message': 'Password does not match. Please try again',
                'message_type': 'danger',
            }
    else:
        data = {
                'message': 'Email address is already registered.',
                'message_type': 'danger',
        }

    return JsonResponse(data)


# export
def export(request):
    img_name = request.GET.get('img_name')
    data = {
        'data': serializers.serialize('json', 'test'),
    }
    return JsonResponse(data)