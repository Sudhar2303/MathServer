# Ex.05 Design a Website for Server Side Processing
## Date: 26/11/2023

## AIM:
To design a website to find total surface area of a square prism in server side.

## FORMULA:
![image](https://github.com/selvasachein/MathServer/assets/120453887/8ecc8d12-b9a9-43df-be0b-711f299d796d)

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
### math.html:
```
<html>

<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Area of Square Prism</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        body {
            background-color:rgb(0, 0, 0);
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
            background: rgb(142, 152, 7);
            background: linear-gradient(90deg, rgb(163, 178, 190) 9%, rgba(7,142,150,1) 56%);
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
        }

        .formelt {
            color: whitesmoke;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }

        h1 {
            color: white;
            text-align: center;
            padding-top: 20px;
        }
        input{
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
            <h1>Area of a Square Prism</h1>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    Side : <input type="text" name="length" value="{{a}}"></input>(in m)<br />
                </div>
                <div class="formelt">
                    Height : <input type="text" name="breadth" value="{{h}}"></input>(in m)<br />
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input><br />
                </div>
                <div class="formelt">
                    Area : <input type="text" name="area" value="{{area}}"></input>m<sup>2</sup><br />
                </div>
            </form>
        </div>
    </div>
</body>

</html>
```
### views.py:
```
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
```
### urls.py:
```
from django.contrib import admin
from django.urls import path
from app5 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/',views.prismarea,name="areaofrectangle"),
    path('',views.prismarea,name="areaofrectangleroot")
]
```
## Output:

![Alt text](<Screenshot (307).png>)
![Screenshot (305)](https://github.com/Sudhar2303/MathServer/assets/133684710/a60f1c83-22c8-469f-b71a-cc9c1f6a049b)

## RESULT:
The program for performing server side processing is completed successfully.
