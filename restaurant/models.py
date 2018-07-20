from django.db import models

# Create your models here.


class Dish(models.Model):
    """餐馆里的一道菜"""
    name = models.CharField(max_length=10)
    prince = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    number_of_ordering = models.IntegerField(default=0)

    def __str__(self):
        """返回一道菜品的信息"""
        basic_txt = '菜名是：' + self.name + '，' + '价格是：' + str(self.prince)
        add_txt = '这道菜的销量是 :' + str(self.number_of_ordering)
        return basic_txt + '。' + add_txt


class Bill(models.Model):
    """
    记录单个客人的账单
    这个表的一个实例是，一道菜的详细订单信息，包括菜名，下单数量，客户对这道菜的要求
    整个表的内容是客人一次点单的信息，在结账完成之后，这个表清空
    """
    dish_name = models.CharField(max_length=10)
    dish_number = models.IntegerField(default=0)
    dish_require = models.CharField(max_length=50, default='无')

    def __str__(self):
        """显示信息"""
        txt = '菜名是：' + self.dish_name + ',' + '数量是:' + str(self.dish_number)
        add_txt = '客户的要求是：' + self.dish_require
        return txt + ',' + add_txt
