import random, string
from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def home(request):
    short_url = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original = form.cleaned_data['original_url']
            url_obj, created = URL.objects.get_or_create(original_url=original)
            if created:
                url_obj.short_code = generate_short_code()
                url_obj.save()
            short_url = request.build_absolute_uri(f"/{url_obj.short_code}/")
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url})

def redirect_to_original(request, code):
    url = get_object_or_404(URL, short_code=code)
    return redirect(url.original_url)
