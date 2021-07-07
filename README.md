# تطبيق اختصار الراوبط  على إطار العمل  بايثون  جانقو 
Python Web Application links shortcut ,  framework Django

#السلام عليكم
اقدم لكم تطبيق بايثون على إطار العمل جانغو وهو تطبيق اختصار للروابط  . تطبيق بسيط جداً جداً والهدف من هذا التطبيق هو التعرف على طريقة عمل جانقو وكيف تتعامل وكيف تفكر في البرمجة وطريقة التفكير 
وايضا الغاية من التطبيق ليس الاستخدام ولكن الفهم  في كتابة الكود  للمبتدئين وايضاً يمكن الاستفادة الاكواد 

- هذا العمل لوجة الله   وهو مجاني  لا احلل ببيعة . وهو مجهود شخصي لنشر الفائدة
- يمكنك استخدام التطبيق لموقعك او التعديل عليه او تطويرة .. الخ
- ## تنوية لن يتم تحديث التطبيق او تطويرة من قبلي . هذا فقط للاستفادة منه إذا تحتاجة 
- ### طبعاً لا يخلو تطبيق من بعض الاخطاء سواء بالنسيان او عدم اختبارة بشكل جيد ..الخ 


# طريقة التركيب بسيطة جداً 

انقل مجلد التطبيق
 الي مشروعك linksShortcut 
 
settings.py ثم  اكتب اسم التطبيق في 
```python
>INSTALLED_APPS= [

	'linksShortcut',
]
```
urls اضف روابط التطبيق في ملف  الخاص بمشروعك

```python
    
include  لاتنسنى استدعاء   
from django.urls import path,include
urlpatterns = [
    path('links_Shortcut/', include('linksShortcut.urls'),name='linksShortcut'),
]

```
فعل البية الافتراضية

اعمل مايقريشن للتطبيق 

```python

python manage.py makemigrations linksShortcut
 
```


اعمل مايقريد

```python

python manage.py migrate

```
ثم شغل السيرفر 


```python
python manage.py runserver
```

ادخل الي لوحة التحكم من قائمة اختصار الروابط   ادخل على إعدادات
 ثم اضف اعدادات  
 
ثم ادخل 

```python
http://localhost:8000/links_Shortcut/Create/
```

انتهى 

######   telegram اتواجد في                                                                                                                                                      
###   @xking المعرف    


انتهى 
