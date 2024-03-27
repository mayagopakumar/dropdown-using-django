# views.py
from django.shortcuts import render
from .models import Items

def dropdown_view(request):
    category = request.GET.get('category')
    print("Selected category:", category)  # Debugging statement
    if category=='all':
        items = Items.objects.all()
    else:
        items = Items.objects.filter(category=category)


    # items = Items.objects.all()  # Default queryset
    # if category and category != 'all':
    #     items = Items.objects.filter(category=category)
    return render(request, 'index.html', {'items': items})
