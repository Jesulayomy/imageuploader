import random

from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image


def home(request):
  """Displays the Home Page"""
  if request.method == "POST":
      form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        return redirect('/')
  form = ImageForm()
  img = Image.objects.all()
  img = [image.to_dict() for image in img]
  random.shuffle(img)

  num_images = len(img)
  if num_images > 100:
    displayed_images = img[19:]
  elif num_images > 50:
    displayed_images = img[9:]
  elif num_images > 25:
    displayed_images = img[4:]
  elif num_images > 10:
    displayed_images = img[2:]
  else:
    displayed_images = img

  return render(request, "myapp/home.html", {"img": displayed_images, "form": form})


def everyone(request):
  """Displays the everyone Page"""
  if request.method == "POST":
      form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        return redirect('/')
  form = ImageForm()
  img = Image.objects.all()
  img_dict = [image.to_dict() for image in img]
  return render(request, "myapp/home.html", {"img": img_dict, "form": form})
