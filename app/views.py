import hashlib
import random
import time
from django.core.cache import cache
from django.shortcuts import render, redirect
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtype, Goods, User


# Create your views here.
def home(request):
    # 轮播图
    wheels = Wheel.objects.all()
    # 导航
    navs = Nav.objects.all()
    # 每日必购
    mustbuys = Mustbuy.objects.all()
    # 商品
    shops = Shop.objects.all()
    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclass_list = shops[3:7]
    shopcommends = shops[7:11]
    # 商品列表
    mainshows = Mainshow.objects.all()

    response_dir = {
        'wheels':wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptabs': shoptabs,
        'shopclass_list': shopclass_list,
        'shopcommends': shopcommends,
        'mainshows': mainshows
    }

    return render(request, 'home/home.html', context=response_dir)



# def market(request, categoryid=104749):
def market(request, childid='0', sortid='0'):
    # 分类信息
    foodtypes = Foodtype.objects.all()
    index = int(request.COOKIES.get('index', '0'))
    # 获取分类ID
    categoryid = foodtypes[index].typeid
    # 子类
    if childid == '0':
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)
    # 排序
    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':
        goods_list = goods_list.order_by('price')
    elif sortid == '3':
        goods_list = goods_list.order_by('-price')

    # 获取子类
    childtypenames = foodtypes[index].childtypenames
    # 存储子类信息
    childtype_list = []
    for item in childtypenames.split('#'):
        item_arr = item.split(':')
        temp_dir = {
            'name': item_arr[0],
            'id': item_arr[1]
        }
        childtype_list.append(temp_dir)

    response_dir = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list': childtype_list,
        'childid': childid
    }

    return render(request, 'market/market.html', context=response_dir)


def cart(request):
    temp = random.randrange(4,63)
    return render(request, 'cart/cart.html', context={'temp':temp})


def mine(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
    return render(request, 'mine/mine.html', context={'user':user})


def login(request):
    return render(request, 'mine/login.html')

def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        passoword = generate_password(request.POST.get('password'))

        user = User()
        user.email = email
        user.password = passoword
        user.name = name
        user.save()

        token = generate_token()
        cache.set(token, user.id, 60*60*24*3)
        request.session['token'] = token
        return redirect('axf:mine')