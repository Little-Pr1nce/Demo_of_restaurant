from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
from .models import Dish, Bill


def index(request):
    """显示主页"""
    return render(request, 'restaurant/homepage.html')


def menu(request):
    """显示所有的菜品"""
    dishes = Dish.objects.order_by('prince')
    content = {'dishes': dishes}
    return render(request, 'restaurant/menu.html', content)


def dish_detail(request, dish_id):
    """显示详细的菜品信息"""
    dish = Dish.objects.get(id=dish_id)
    name = dish.name
    price = dish.prince
    number = dish.number_of_ordering
    if number >= 3:
        txt = '这道菜卖的很好，是我们的招牌菜'
    else:
        txt = '这道菜是我们的新菜，你可以尝试一下'

    content = {'dish': dish, 'name': name, 'price': price, 'txt': txt}

    return render(request, 'restaurant/dish.html', content)


def order_dish(request, dish_id):
    """点单"""
    dish = Dish.objects.get(id=dish_id)  # 得到当前的菜

    if request.method != 'POST':
        """如果当前访问不是POST，显示表单页面"""
        name = dish.name
        content = {'name': name}
        return render(request, 'restaurant/order_dish.html', content)

    else:
        """客户提供点菜的要求"""
        number = request.POST['number']  # 客户点了几道这个菜
        require = request.POST['require']  # 客户对这道菜的要求
        dish.number_of_ordering = dish.number_of_ordering + int(number)  # 更新菜的销量数据
        dish.save()  # 保存到数据库
        bill = Bill(dish_name=dish.name, dish_number=number, dish_require=require)
        bill.save()  # 把点的菜保存到bill里
        return HttpResponseRedirect(reverse_lazy('restaurant:menu'))


def get_bill(request):
    """显示客户点的所有菜"""

    # 如果用户只是来查看这个页面
    if request.method != "POST":
        bills = Bill.objects.order_by('dish_name')
        content = {'bills': bills}
        return render(request, 'restaurant/bill.html', content)
    else:
        # 用户要结账，就清空bill这个表
        Bill.objects.all().delete()
        return HttpResponseRedirect(reverse_lazy('restaurant:index'))



