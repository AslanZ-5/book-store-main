from .models import Category


def categories(request):
    return {
        'categories': Category.objects.filter(level=0) # level 0 is parent level of the  MPTT model
    }
