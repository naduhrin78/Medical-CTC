from md_ctc.models import Profile

def get_avatar(backend, strategy, details, response,
    user=None, *args, **kwargs):

    url = None

    profile = Profile.objects.get(user=user)

    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]

    if url:
        profile.avatar = url
        profile.save()
