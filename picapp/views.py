import datetime as dt
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Category,Location


# Create your views here.


def pics_today(request):
    # date = dt.date.today()
    display = Image.objects.all()
    return render(request, 'gallery/pics.html',{'display':display})
#
# def convert_dates(dates):
#
#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)
#
#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
#
#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def pics_today(request):
#     date = dt.date.today()
#
#     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>pics for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"display": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
