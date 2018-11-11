from .models import Setting

def savva():
    result = Setting.objects.all()
    settings={}
    for item in result:
        settings[item.key]=item.value
    return settings

sttngs=savva()
