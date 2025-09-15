from ..models.cv import CV

def create_cv(user, data, files):
    cv = CV.objects.create(
        user=user,
        full_name=data.get('full_name'),
        email=data.get('email'),
        phone=data.get('phone'),
        education_level=data.get('education'),
        observations=data.get('observations'),
        desired_position=data.get('desired_position'),
        ip_address=data.get('ip_address'),
        cv_file=files.get('cv_file'),
    )
    return cv