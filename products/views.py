from django.http import HttpResponse
from rest_framework.response import Response
from products.serializers import ProductSerializer, ProductDetailsSerializer, CreateProductSerializer
from rest_framework.views import  APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


# Create your views here.
from rest_framework.decorators import api_view


from products.models import Product



def test_view(request):
    return HttpResponse('Hello World!')

@api_view(['GET'])
def products_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
#[{'id':1, 'title':..., 'description':..., 'price'}]
    return Response(serializer.data)

class ProductsListView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer




#TODO: 1. создовать, редактировать и удалять продукты могут только админы (permission)
#TODO: 2. Лагинация (разбивка листинга на страницы)
#TODO: 3. Фильтрация
#TODO: 4. Поиск продуктов по названию и описанию
#TODO: 5. ограничение количества запросов
#TODO: 6. тесты

#TODO: 7. Отзывы
#TODO: 8. Разобрать взаимодействие


#TODO:


# REST - архитектурный подход
# 1. Модель клиент = сервер
# 2. Отсутвие - состояния
# 3. Кеширование
# 4. Единообразие интерфейса
# 4.1 Определение ресурсов
# 4.2 управление ресурсом через представление
# 4.3 самодостаточные ообщение
# 4.4 гиперМедиа
# # 5. Слои
# 6. Код по требованию

# 'GET',  'POST',   'PUT',    'PATCH',           'DELETE'
# list ,   create,  update,   partial_update      destroy


# API (Application Programming Interface)  Homework
# паттерн MVC


#Product.objects.all() - выдаёт весь список обьектов модели
# SELECT * FROM product;


# Product.objects.create() - создаёт новый обьект
# INSERT INTO product ...

# Product.objects.update() - обновляет выбранные обьекты
# UPDATE product ...;
#
# Product.objects.delete() - удаляет обьекты
# DELETE FROM product;
#
#
# Product.objects.filter(условие)
# SELECT * FROM product WHERE условие;

# Операции сравнения
'='
# Product.objects.filter(price=10000)
# SELECT * FROM product WHERE price = 10000;

">"
# Product.objects.filter(price__gt=10000)
# SELECT * FROM product WHERE price > 10000;

"<"
# Product.objects.filter(price__lt=10000)
# SELECT * FROM product WHERE price < 10000;

">="
# Product.objects.filter(price__gte=10000)
# SELECT * FROM product WHERE price >= 10000;

"<="
# Product.objects.filter(price__lte=10000)
# SELECT * FROM product WHERE price <= 10000;

# BETWEEN
# Product.objects.filter(price__range=[50000, 80000])
# SELECT * FROM product WHERE price BETWEEN 50000 AND 80000;


# IN
# Product.objects.filter(price__in=[50000, 80000])
# SELECT * FROM product WHERE price IN (50000, 80000);


# LIKE
# ILIKE
#
# 'work%'
# Product.objects.filter(title__startswith='Apple')
# SELECT * FROM product WHERE title LIKE 'Apple%';
# Product.objects.filter(title__istartswith='Apple')
# SELECT * FROM product WHERE title ILIKE 'Apple%';
#
# '%work'
# Product.objects.filter(title__endswith='GB')
# SELECT * FROM product WHERE title LIKE '%GB';
#
# Product.objects.filter(title__iendswith='GB')
# SELECT * FROM product WHERE title ILIKE '%GB';
#
# '%work%'
# Product.objects.filter(title__contains='Samsung')
# SELECT * FROM product WHERE title LIKE '%Samsung%';

# Product.objects.filter(title__icontains='Samsung')
# SELECT * FROM product WHERE title ILIKE '%Samsung%';


'work'
# Product.objects.filter(title__exact='Apple Iphone 12')
# SELECT * from product WHERE title LIKE 'Apple Iphone 12';

# Product.objects.filter(title__iexact='Apple Iphone 12')
# SELECT * from product WHERE title ILIKE 'Apple Iphone 12';


# ORDER BY
#
# Product.objects.order_by('price')
# SELECT * FROM product ORDER BY price ASC;
#
# Product.objects.order_by('-price')
# SELECT * FROM product ORDER BY price DESC;
#
# Product.objects.order_by('price','title')
# SELECT * FROM product ORDER BY price DESC, title  ASC;

# LIMIT
# Product.objects.all()[:2]
# SELECT * FROM product LIMIT 2;

# Product.objects.all()[3:6]
# SELECT * FROM product LIMIT 3 OFFSET 3;

# Product.objects.first()
# SELECT * FROM product LIMIT 1;


# get() - возвращает один обьект

# Product.objects.get(id=1)
# SELECT * FROM product WHERE id=1;
#
# DoesNotExist - возникает, если не найден ни один обьект
# MultipleObjectsReturned - возникает, когда найдено больше одного обьекта

# count() - возвращает количество результатов
#
# Product.objects.count()
# SELECT COUNT(*) FROM product;
#
# Product.objects.filter(...).count()
# SELECT COUNT(*) FROM product WHERE ...;
#
#
# exclude()
# Product.objects.filter(price__gt=10000)
# SELECT * FROM product WHERE price > 10000;
#
# Product.objects.exclude(price__gt=10000)
# SELECT * FROM product WHERE NOT price > 10000;


# QuerySet - список обьектов модели             HOMEWORK
# HTTP методы ("GET", "POST", "PUT", "PATCH", "DELETE")      HOMEWORK

