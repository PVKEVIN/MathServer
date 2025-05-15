# Ex.05 Design a Website for Server Side Processing
## 212224040159
## P Kevin
## Date:15.05.2025
## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
mathapp.html
```
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>POWER OF LAMP IN INCANDESCENT BULB</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        body {
            background-color: white;
        }

        .edge {
            display: flex;
            height: 100vh;
            width: 100%;
            justify-content: center;
            align-items: center;
        }

        .box {
            display: block;
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background: linear-gradient(90deg, rgb(29, 5, 166) 9%, rgb(101, 26, 26) 56%);
            border-radius: 10px;
            box-shadow: rgba(239, 5, 24, 0.35) 0px 5px 15px;
        }

        .formelt {
            color: whitesmoke;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }

        h1 {
            color: rgb(249, 249, 249);
            text-align: center;
            padding-top: 20px;
        }

        input {
            margin: 5px;
            padding: 5px;
            border-radius: 5px;
            border: none;
        }
    </style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>POWER OF LAMP IN INCANDESCENT BULB</h1>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    INTENSITY: 
                    <input type="text" name="Intensity" value="{{ I }}"> (in A)<br />
                </div>
                <div class="formelt">
                    RESISTANCE: 
                    <input type="text" name="Resistance" value="{{ R }}"> (in Ω)<br />
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"><br />
                </div>
                <div class="formelt">
                    POWER: 
                    <input type="text" name="Power" value="{{ Power }}"> W<br />
                </div>
            </form>
        </div>
    </div>
</body>
</html>
```
views.py
```
from django.shortcuts import render

def powerlamp(request):
    context={}
    context['Power'] = ""
    context['I'] = ""
    context['R'] = ""
    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('Intensity','')
        R = request.POST.get('Resistence','')
        print('request=',request)
        print('Intensity=',I)
        print('Resistence=',R)
        Power = int(I) * int(I) * int(R)
        context['Power'] = Power
        context['I'] = I
        context['R'] = R
        print('Power=',Power)
    return render(request,'mathapp/mathapp.html',context)
```
urls.py
```
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('PowerOfLampFilamentInAnIncandescentBulb/',views.powerlamp,name="PowerOfLampFilamentInAnIncandescentBulb"),
    path('',views.powerlamp,name="PowerOfLampFilamentInAnIncandescentBulb"),
]
```

## SERVER SIDE PROCESSING:
![image](https://github.com/user-attachments/assets/fcdcd899-dbb2-4c8c-b273-234a58baa2e8)

## HOMEPAGE:
![image](https://github.com/user-attachments/assets/23b77e63-5410-4cc3-b568-a292e190e960)


## RESULT:
The program for performing server side processing is completed successfully.
