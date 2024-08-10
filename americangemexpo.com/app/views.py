# myapp/views.py

from django.shortcuts import render,redirect
from .models import Domaindata

def domain(request):
    data = Domaindata.objects.all()
    return render(request, 'index1.html', {'data': data})

def url_view(request):
    path = request.path
    url_component = path.strip('/').split('-')

    all_objects = Domaindata.objects.all()
    match_found = False

    for i in url_component:
        for obj in all_objects:
            if i == obj.keyword:
                match_found = True
                obj.min_count += 1
                obj.save()

                if obj.min_count >= obj.max_count:
                    return redirect(obj.url2)
                else:
                    return redirect(obj.url1)

    # If no match was found, redirect to the default URL
    if not match_found:
        return redirect('https://www.influencerhiring.com/')
  # Replace 'your_default_url' with the actual URL or named URL pattern


