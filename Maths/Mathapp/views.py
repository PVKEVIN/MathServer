from django.shortcuts import render

def rightcylinder(request):
    context = {}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"
    
    if request.method == 'POST':
        print("POST method is used")
        
        # Print the entire request.POST object
        print('request.POST:', request.POST)
        
        r = request.POST.get('Radius', '0')  # Corrected key to retrieve radius
        h = request.POST.get('height', '0')  # Corrected key to retrieve height
        print('radius =', r)
        print('height =', h)
        
        area = (2 * 3.14 * int(r) * int(h)) + (2 * 3.14 * int(r) * int(r))
        context['area'] = area
        context['r'] = r
        context['h'] = h
        print('Area =', area)
    
    return render(request,'Mathapp/math.html', context)
