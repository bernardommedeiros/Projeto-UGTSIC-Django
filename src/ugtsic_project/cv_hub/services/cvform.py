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

def update_cv(cv, data, files):
    cv.full_name = data.get('full_name', cv.full_name)
    cv.email = data.get('email', cv.email)
    cv.phone = data.get('phone', cv.phone)
    cv.education_level = data.get('education', cv.education_level)
    cv.observations = data.get('observations', cv.observations)
    cv.desired_position = data.get('desired_position', cv.desired_position)
    if files.get('cv_file'):
        cv.cv_file = files.get('cv_file')
    cv.save()
    return cv