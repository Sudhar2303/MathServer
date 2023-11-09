from django.shortcuts import render

def prismarea(request):
    context={}
    context['area'] = "0"
    context['a'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        a = request.POST.get('length','0')
        h = request.POST.get('breadth','0')
        print('request=',request)
        print('Length=',a)
        print('Breadth=',h)
        area = 2*(int(a)**2) + 4*int(a)*int(h)
        context['area'] = area
        context['a'] = a
        context['h'] = h
        print('Area=',area)
    return render(request,'mathapp/math.html',context)