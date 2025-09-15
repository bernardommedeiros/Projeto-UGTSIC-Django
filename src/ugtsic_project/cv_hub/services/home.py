from ..models.cv import CV

def show_cv(user):
    # retorna o CV do usuário, se existir, limitando-o a apenas um
    cv = CV.objects.filter(user=user).first() 
    return cv
