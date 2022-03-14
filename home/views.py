from django.shortcuts import render
from django.http import HttpResponse
import pymysql
# Create your views here.

def index(request):
    db = pymysql.connect(host="www.oggy.co.in",
                     user="sql6418117",
                     passwd="Rajata316",
                     db="oggy")
    cur = db.cursor()
    cur.execute("select name, address, zomato_rating, index_image from rests_temp")
    data = cur.fetchall()
    data = list(data)
    data2 = []
    for x in data:
        data2.append(list(x))
    rest_names = "rajat"
    context = {
        'rest_list' : data2
    }
    return render(request, 'index.html', context)

def restaurant(request):
    rest_name = request.GET.get('name')
    db = pymysql.connect(host="www.oggy.co.in",
                     user="sql6418117",
                     passwd="Rajata316",
                     db="oggy")
    cur = db.cursor()
    cur.execute(f"""select * from rests_temp where name regexp "{rest_name}" """)
    data = cur.fetchall()
    data = list(data)
    data2 = []
    for x in data:
        data2.append(list(x))
    data2 = data2[0]
    images = []
    index_image = data2[20]
    index_image = index_image[0:-6]
    for x in range(1,6):
        images.append(index_image+str(x)+".webp")
    zomato_desc = data2[21]
    zomato_code = data2[22]
    magicpin_desc = data2[23]
    swiggy_offers = data2[15]
    dineout_offers = data2[16]
    zomato_desc_list = zomato_desc.split(",")
    zomato_code_list = zomato_code.split(",")
    swiggy_offers_list = swiggy_offers.split(",")
    s1desc, s2code = zip(*(s.split('|') for s in swiggy_offers_list))
    s1desc = list(s1desc)
    s2code = list(s2code)
    zomato_offers = zip(zomato_desc_list, zomato_code_list)
    swiggy_offers = zip(s1desc,s2code)
    magicpin_offers = magicpin_desc.split(',')

    context = {
        'name' : data2[1],
        'cuisines' : data2[5],
        'address' : data2[2],
        'timing' : data2[4],
        'zomato_rating' : data2[6],
        'swiggy_rating' : data2[7],
        'dineout_rating' : data2[8],
        'magicpin_rating' : data2[9],
        'direction' : data2[18],
        'image1' : images[0],
        'image2' : images[1],
        'image3' : images[2],
        'image4' : images[3],
        'zomato_link' : data2[10],
        'swiggy_link' : data2[11],
        'dineout_link' : data2[12],
        'magicpin_link' : data2[13],
        'zomato_offers' : zomato_offers,
        'swiggy_offers' : swiggy_offers,
        'dineout_offers' : dineout_offers,
        'magicpin_offers' : magicpin_offers,
        'magicpin_item' : magicpin_offers[0]
    }
    return render(request, 'restaurant.html', context)