from ..models.cv import CV

def show_cv():
    return CV.objects.all()