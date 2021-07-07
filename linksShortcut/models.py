##############################################################################################################################################################################@
#   وهو تطبيق بسيط عبارة عن اختصار الروابط مع بعض المميزات تحويل الوقت او عدد محدد لاستخدام الرابط او وضع كلمة مرور M3fooos تم انشاء التطبيق من قبل                  @
#   وهو تطبيق بسيط جدا جدا ولكن هدفي هو ليس التطبيق ذاته او ربما لا تستخدمة في موقعك ولكن الهدف هو إيصال معلومة بان المبرمج ليس بالاكواد ولكن البرمجة الحقيقية       @
#   هو العقل الذي هو كيف يبني مخطط او خطة لعمل النظام وكيف يكون السيناريو لطريقة العمل من البداية الي النهائية                                                        @
#   وايضا انا تعمدة انني اكتب بهذه الصيغة لكي تصل غايتي وهي ان لكل شخص تفكير                                                                                            @
#   ووضعت ايضا بعض الطرق التي لديها بدائل كثيرة في كتابت الكود كي اضع لك بان تقدر تعملها بطرق اخر وتضيف حقول                                                         @
#   وتخفف الحقول وكيف لا تكرر الاكواد التي تتطلب في كل مرة تستخدمها وايضا تعمدة ايضا اضع شغلات مكررة كيف تفكر اكثر                                                     @
#   وايضا كتبت فوق كل سطر تقريباً ماذا يعمل, كي تعرف كيف نسير خطوة بخطوة                                                                                                 @
#   هذا العمل لوجة الله سبحانة وتعالى                                                                                                                                      @
#   لا اقبل ببيعه للاخرين .. فهو مجاني للجميع سواء استخدام شخصي او عام او تعديل او الدراسة منه                                                                            @
#   وهو موجة حق الاشخاص المبتدئين في جانغو وايضا موجة للاشخاص الذين يكتب الكود دون فهم ما يكتب او الذي لا ينظم الكود ويشربك الامور في بعضها البعض                       @
#   ويدخل في بعض المشاكل                                                                                                                                                    @
#   واخر الحديث الشكر لله دائما وأبداً                                                                                                                                     @
#   telegram اتواجد في                                                                                                                                                      @
#   @xking الحساب                                                                                                                                                           @
############################################################################################################################################################################@




# استخدام ادوات الجانقو لتتحقق من بعض البيانات في حقول الجدول
from django.core.validators import MinValueValidator  # MinLengthValidator
# لجلب الروابط
from django.urls import reverse
# اضافة الترجمة في حقول الموقع والادمن
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from django.db import models
##########################
import re
import string
import random

# هذا الكلاس نضع بعض الميثود لمعالجة البيانات وعدم تكرر كتابة الاكواد سوف يكون طرف ثالث فقط 
class AppTools():

    #فنكش للتحقق من رابط الموقع في اعدادات التطبيق  تاخذ قيمة وترجع لنا قاموس به بيانات ام صحيحة او خاطئة  
    def validate_url(self,value):
        errors = {
            "error":True,
        }
        if not value:
            errors["msg"] = _('الرجاء كتابة عنوان ')
            return errors

        value= value.strip().rstrip('/')
        #اذا اردة استخدام ادخال روابط localhost:8000  او 127.0.0.1
        re_exp = (r"^(http|https)://(www)?\.?([a-zA-Z0-9-_]+)(.|:)[a-zA-Z0-9]+\/?.+?$")
        #اذا اردة رفع الموقع على استضافة وتريد التحقق من الروابط الصحيحة فعل هذا
        # re_exp = (r"^(http|https)://(www)?\.?([a-zA-Z0-9-_]+)\.[a-zA-Z0-9]+\/.+$")
        check_value = re.match(re_exp, value)
        if check_value:
            return value
        else:
            errors["msg"] = _('أدخل عنوان صحيح')
            return errors


    #ميثود لتوليد الرابط حروف و ارقام
    def generate_url(self,count=2):
        char = string.ascii_letters + string.digits + "-_"
        _str = ''.join((random.choice(char) for i in range(count)))
        
        _list = list(_str)
        random.shuffle(_list)
        final_string = ''.join(_list)
        return final_string



class ConfigShortcutUrlTools(models.Manager):
    # جلب قيمة عدد خانات الرابط المحدد من قبل مدير الموقع
    def get_first_object(self):
        return super(ConfigShortcutUrlTools, self).get_queryset().all()[0]

    def get_available_fields(self):
        get_field = super(ConfigShortcutUrlTools, self).get_queryset().values('use_limited', 'use_expired_date', 'use_password').all()[0]
        back_list = []
        for key, value in get_field.items():
            if not value:
                if key == 'use_limited':
                    back_list.append('count_click')
                elif key == 'use_expired_date':
                    back_list.append('expired_date')
                elif key == 'use_password':
                    back_list.append('password')
        return back_list


# كلاس اعدادات التطبيق
class ConfigShortcutUrl(models.Model):
    select_service = (
        (1, _('لا احد')),
        (2, _('الاعضاء')),
        (3, _('الجميع')),
    )

    # متغيرات مساعدة لحقول الجدول
    help_url = _('https://www.example.com  مثال')
    help_service = _('من يستطيع استخدام التطبيق')
    help_use_limited = _('عند التفعيل يمكنك اضافة عدد استخدام الرابط')
    help_use_expired_date = _('عند التفعيل يمكنك استخدام تاريخ انتهاء للرابط')
    help_use_password = _('عند التفعيل يمكنك استخدام كلمة مرور للرابط')
    help_length_url = _('عدد خانات الروابط المختصرة [اقل عدد 2]')
    help_use_wait = _('الحقل يكون بالثواني ,القيمة الافتراضية 0  ثانية , تحويل بدون انتظار')

    # اسم الموقع
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name=_('اسم الموقع'))
    # رابط الموقع الذي سوف يعتمد عليه التطبيق
    url = models.URLField(max_length=50, help_text=help_url, blank=False, null=False, verbose_name=_("رابط الموقع"))
    # من يستطيع استخدام التطبيق
    use_service = models.IntegerField(help_text=help_service, default=3, choices=select_service, null=False, verbose_name=_("استخدام التطبيق"))
    # السماح لوضع  عدد محدد لاستخدام الرابط
    use_limited = models.BooleanField(help_text=help_use_limited, default=False, null=False, verbose_name=_("فعال / معطل ؟"))
    # السماح لوضع  تاريخ انتهاء للرابط
    use_expired_date = models.BooleanField(help_text=help_use_expired_date, default=False, null=False, verbose_name=_("فعال / معطل ؟"))
    # السماح انشاء كلمة مرور للرابط
    use_password = models.BooleanField(help_text=help_use_password, default=False, null=False, verbose_name=_("فعال / معطل ؟"))
    # عدد طول الرابط
    length_url = models.IntegerField(validators=[MinValueValidator(2)], help_text=help_length_url, blank=True, null=False, default=5, verbose_name=_("عدد طول الرابط"))
    # السماح لاستخدام وقت الانتظار قبل التحويل للرابط الاصلي
    use_wait = models.IntegerField(help_text=help_use_wait, default=0, validators=[MinValueValidator(0)], blank=False,  verbose_name=_(" وقت الانتظار"))

    objects = models.Manager()
    # استدعاء لكلاس المساعد
    obj = ConfigShortcutUrlTools()
    # صناعة ابجكت من كلاس المساعد في التحقق من معالجة البيانات
    AppT = AppTools()
    # اسم التطبيق في لوحة الادمن

    class Meta:
        verbose_name = _("إعدادات")
        verbose_name_plural = _("إعدادات")

    # ميثود لإسترجاع اسم الاوجبكت
    def __str__(self):
        return str(self.name)

    # ميثود لتنظيف الكود او للفلاترة  والتحقق من البيانات قبل الحفظ
    def clean(self):
        # للتحقق من ادخال عنوان الموقع في اعداادات التطبيق
        check_url = self.AppT.validate_url(self.url)
        if type(check_url) == dict:
            raise ValidationError({'url': check_url['msg']}, code='error_url')
        else:
            self.url = check_url

    # ميثود لحفظ البيانات
    def save(self, *args, **kwargs):

        super(ConfigShortcutUrl, self).save(*args, **kwargs)

########################################################################################################################
# كلاس مساعد للمودل نضع فيه جميع الادوات التي نحتاجها في فلترة او معالجة او استخراج بيانات من قاعدة البيانات
# ونجعله يرث كلاس به ميثود عامة لجميع التطبيق للمساعدة في بعض معالجة البيانات  واسم الكلا س الذي سوف نرث منه AppTools


class ShortcutUrlTools(models.Manager, AppTools):
    pass


class ShortcutUrl(models.Model):

    help_password = _('اتركة فارغ اذا لاتريد كلمة مرور')
    help_count_click = _('القيمة الافتراضية 0 استخدام لا محدود')
    help_status = _('عند التعطيل سيتم تعطيل الرابط')
    help_expired_date = _('الحقل يكون بالايام ,القيمة الافتراضية 0  لاينتهي')

    id = models.IntegerField(primary_key=True, editable=False, unique=True, blank=False, null=False, verbose_name='id')
    shorten_url = models.CharField(max_length=50, unique=True, blank=True, null=False, verbose_name=_('الرابط المختصر'))
    redirect_url = models.TextField(blank=False, null=False, verbose_name=_("ادخل الرابط"))
    password = models.CharField(help_text=help_password, max_length=50, blank=True, null=True, verbose_name=_('حماية الرابط بكلمة مرور'))
    #  هذا الحقل  راح نخليه مخفي وقيمته الافتراضية صفر  من نوع نص
    #(count_click = 1  ,  expired_date = 2  )  والسبب انا نريد ان نضيف حالة حقل  وكل حقل نعطية رقم  
    #هناك طرق كثيرة ولكن لا اريد اضافة حقول كثير او استخدم حقل جيسون فهذه سهله ويكون التطبيق للمبتدئين  
    hidden_field = models.CharField(max_length=3,default="0",editable=False,blank=True, null=True, verbose_name='hidden_field')
    count_click = models.IntegerField(help_text=help_count_click, default=0, validators=[MinValueValidator(0)], blank=False, verbose_name=_("عدد مرات استخدام الرابط"))
    expired_date = models.IntegerField(help_text=help_expired_date, default=0, validators=[MinValueValidator(0)], blank=False, verbose_name=_("عدد ايام إنتهاء الرابط"))

    status = models.BooleanField(default=True, help_text=help_status, blank=False, null=False, verbose_name=_("فعال / معطل ؟"))
    count_views = models.IntegerField(blank=True, null=False,  default=0, verbose_name=_("عدد زيارات الرابط"))
    created_by = models.CharField(max_length=255, null=False, verbose_name=_("إنشاء بواسطة"))
    created_date = models.DateField(auto_now_add=True, blank=True, null=False, verbose_name=_("تاريخ إنشاء الرابط "))
    objects = models.Manager()
    obj = ShortcutUrlTools()
    AppT = AppTools()

    class Meta:
        #unique_together = ['name', 'slug']
        verbose_name = _("اختصار الروابط")
        verbose_name_plural = _("اختصار الروابط")
        ordering = ('-id',)

    def __str__(self):
        return str(self.shorten_url)

    #نستخدم هذه الميثود لجلب اسم الرابط كامل مع اسم الموقع راح تاخذ اسم urls  
    def get_absolute_url(self):
        return reverse('linksShortcut:open-url', kwargs={'code': self.shorten_url})

    # ميثود لنتحكم في ارقام id
    # ونجعله عدم الاستمرار في الارقام سواء حذفنا اخر سجل بان يعطي رقم مستمر فجعلناها تاتي ب اخر رقم للسلاجت وتضيف عليه 1
    def increment_id(self):
        CheckRow = ShortcutUrl.objects.all().count()
        if not CheckRow:
            return 1
        else:
            CheckRow = ShortcutUrl.objects.all().order_by('id').last().id
            return CheckRow + 1

    # ميثود لتووليد الرابط
    def generate_shorten_url(self):
        # جلب قيمة عدد الخانات المحددة في اعدادات التطبيق لمعرفة عدد طول الرابط
        get_setting_app = ConfigShortcutUrl.obj.get_first_object()
        #######################################
        # سوف نستخدم وقت 300 ثانية  تساوي 5 دقائق لعملية انشاء الروابط المختصر ونشيك هل الرقم موجود او لا  اذا كان عدد اختصار الروابط امتلى سوف نرجع خطاء ونطلب زيادة عدد خانات اختصار الرابط
        # واذا كان الرابط غير موجود سوف نلغى الوقت ونرجع القيمة لاختصار الرابط دون استخدام الوقت
        import datetime
        # تسجل الوقت الحالي
        get_time = datetime.datetime.now()
        # نزيد على الوقت الحالي 300 ثانية  = 5 دقائق ونحفظة للمقارنة  وهذا وقت جدا طويل يعني انصح اذا بديت تنتظر اكثر من 5 ثواني يجب عليك زيادة عدد خانات الاختصارات
        add_time = get_time + datetime.timedelta(0, 300)  # days, seconds, then other fields.
        #######################################
        # عمل لوب حتى ياتي ب كود غير متكرر في قاعدة البيانات
        while True:
            # ننشى كود جديد
            _generate = self.AppT.generate_url(int(get_setting_app.length_url))
            # نشيك هل هو موجود في قاعدة البيانات
            CheckRow = ShortcutUrl.objects.filter(shorten_url=_generate)
            if CheckRow:
                # نجيب الوقت الحالي
                get_time = datetime.datetime.now()
                # نشيك هل انتهاء الوقت المحدد  اذا كان نعم سوف نوقف العملية ونرجع الخطاء على شكل قاموس
                if get_time > add_time:
                    return {
                        "error": True,
                        "msg": _("""
                        (تم المحاولة على البحث عن كود مختصر جديد ولكن لايوجد كود متاح )
                        (الرجاء الذهاب الي اعدادات التطبيق وزيادة عدد خانات الكود )
                        """)
                    }
                # اذا كان موجود نستمر في انشاء الكود بشكل برمز اخر
                continue
            else:
                return _generate

    def make_shorten_url(self):
        # نشيك على عملية انشاء الكود المختصير
        check_code = self.generate_shorten_url()
        if type(check_code) == dict:
            raise ValidationError({'redirect_url': check_code['msg']}, code='error_shorten_url')
        self.shorten_url = check_code

    def clean(self):
        # للتحقق من ادخال عنوان الموقع الذي نريد اختصارة
        check_url = self.AppT.validate_url(self.redirect_url)
        if type(check_url) == dict:
            raise ValidationError({'redirect_url': check_url['msg']}, code='error_redirect_url')
        else:
            self.url = check_url
        # نتصل بميثود لتوليد الكود
        if not self.shorten_url:
            self.make_shorten_url()

        #########################################################################################

        ## هناك طرق اخرى كثيرة ولكن انا اخترت هذه والهدف منها  التوسع في تفكير المبرمج المبتدئ في وجود حلول كثيرة  مع حقول قليلة
        #هنا نتحقق اذا كان هناك عدد محدد للرابط نضيف رقم 1 كي نعرف ان هذا الحقل كان بالسابق فعال 
        if self.count_click > 0 :
            # هنا نشيك اذا الرقم 1 الذي يرمز لعدد الضغطات موجود فعلا او لا اذا كان غير موجود نضع الرمز 1  
            if not "1" in self.hidden_field:
                #نضيف في الحقل المخفي انه فعال 
                self.hidden_field += "1"
        #اذا كان غير ذالك نمسح الرقم 1 
        else:
            # هنا نشيك اذا كان موجود نمسحهة 
            if "1" in self.hidden_field:
                #اذا كان موجود نحذفه  
                self.hidden_field = self.hidden_field.replace('1','')

        #هنا نتحقق اذا كان هناك عدد محدد للرابط نضيف رقم 2 كي نعرف ان هذا الحقل كان بالسابق فعال 
        if self.expired_date > 0 :
            # هنا نشيك اذا الرقم 2 الذي يرمز لعدد الضغطات موجود فعلا او لا اذا كان غير موجود نضع الرمز 2  
            if not "2" in self.hidden_field:
                #نضيف في الحقل المخفي انه فعال 
                self.hidden_field += "2"
        #اذا كان غير ذالك نمسح الرقم 2 
        else:
            # هنا نشيك اذا كان موجود نمسحهة 
            if "2" in self.hidden_field:
                #اذا كان موجود نحذفه  
                self.hidden_field = self.hidden_field.replace('2','')

        #########################################################################################


    def save(self, *args, **kwargs):
        # عند قبل حفظ اي سجل نضيف مفتاح السجل
        if not self.id:
            self.id = self.increment_id()

        super(ShortcutUrl, self).save(*args, **kwargs)
