from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse ('hi')

def about_us(request):
    return HttpResponse('Найдите работу или работника мечты')

def contacts(request):
    return HttpResponse('''<div>Phone: +996777123456<br>
                        Email: office@handhunter.kg</div>''')

def address(request):
    return HttpResponse(
        '''
        <ul>
            <li>hunter@gmail.com</li>
            <li>employee@gmail.com</li>
            <li>hr@gmail.com</li>
        </ul>
        '''
    )