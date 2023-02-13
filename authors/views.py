from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def register_view(request):
    request.session['number'] = request.session.get('number') or 1
    request.session['number'] += 1
    form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


'''raise levanta um erro'''


def register_create(request):
    if not request.POST:
        raise Http404()
    form = RegisterForm(request.POST)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
