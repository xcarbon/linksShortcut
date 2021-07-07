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

from linksShortcut.models import ConfigShortcutUrl,ShortcutUrl
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView
import datetime



#كلاس فورما لانشاء الرابط المختصر 
class CreateRowForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #نعمل لوب للحقول ونضيف عليهم كلاس البوت ستراب للتنسيق
        for k, v in self.fields.items():
            v.widget.attrs['class'] = "form-control"
            
        #نجلب اعدادات التطبيق والمميزات المسموحة  ونشيك اذا مثلا غير مفعل كلمة مرور سوف نحذف الحقل من الفورما  سوف ترجع البيانات على شكل لستة 
        list_pop_items = ConfigShortcutUrl.obj.get_available_fields()

        # هنا شيك اذا كان فعلا في حقول مفعله نبدى نحذفها من الفورم
        if len(list_pop_items):
            for field in list_pop_items:
                self.fields.pop(field)

    class Meta:
        #اسم المودل 
        model = ShortcutUrl
        #نجلب كل الحقول 
        fields = '__all__'
        #لانريد هذه الحقول بحيث كون الادمن هو المتحكم بها 
        exclude = ["status", "count_views", "created_by"]


#انشاء رابط مختصر 
class CreateRow(CreateView):
    # الصفحة التي سوف تكون فيها عرض الفورما 
    template_name = 'linksShortcut/create_url.html'
    #استدعاء المودل الي نبي نتعامل معه
    model = ShortcutUrl
    #استدعاء الفورما
    form_class = CreateRowForm

    ##هذه الميثود سوف تكون للتشيك على اعدادات التطبيق قبل ارجاع الفورما او تقدر توجه الشخص على اي صفحة 
    def dispatch(self, request, *args, **kwargs):
        # قبل عرض الصفحة نشيك على اعدادات التطبيق  من الذي استخدام التطبيق:  لا احد .. عضو .. الجميع 
        self.check_app = ConfigShortcutUrl.obj.get_first_object()
        #نشيك على الرقم من  المسموح 
        # 1   لا احد 
        # 2  الاعضاء 
        # 3 الجميع 
        ##################################################################################
        #اذا كان لا احد سوف نحوله الي الصفحة الرئيسية 
        if self.check_app.use_service == 1 : 
            return redirect('/')
        #هنا نتحقق اذا كان الموقع للاعضاء والذي طلب الصفحة زائر سوف نحوله الي صفجة تسجيل الدخول او التسجيل بالموقع 
        elif self.check_app.use_service == 2  and self.request.user.is_authenticated == False: 
            # نحوله الي صفحة تسجيل الدخول او الي صفحة التسجيل اختر ما تريد 
            return redirect('login')
        #اذا الموقع للجميع  لانعمل شي 
        else:
            pass
        return super().dispatch(request, *args, **kwargs)
    #نستخدم هذه الميثود للتحقق من الشخص واعدادات التطبيق قبل كل شي 


    #نضيف بيانات اضافية قبل انشاء الفورما وهي امر يوضح لنا ماذا نريد ان نعمل
    def get_context_data(self, **kwargs):
        create_obj = super(CreateRow, self).get_context_data(**kwargs)

        # html نضيف هذا الامر  ونقول للرندر اعرض لنا بيانات ال
        #الموجودة في  التمبلت ونتحقق هناك في التمبلت  
        create_obj['CMD'] = "Create"
        return create_obj


    #اذا كانت المدخلات في الفورمه غير صحيحة سوف نرجع البيانات مع الخطاء الموجود
    def form_invalid(self, form):
        return super().form_invalid(form)
        
    #اذا كانت المدخلات في الفورمه صحيحة سوف تنفذ هذه الميثود
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = str(self.request.user)
        obj.save()
        return super().form_valid(form)

    #اذا تم انشاء البيانات سوف ناخذ الكود ونحوله الي صفحة عرض الرابط المختصر الي هو كلاس ShowRow
    def get_success_url(self):
        return reverse_lazy('linksShortcut:CreateShow', kwargs={'code': str(self.object.shorten_url)})


# عرض الرابط المختصر بعد الانشاء 
class ShowRow(TemplateView):
    template_name = 'linksShortcut/create_url.html'


        #هنا نشيك الشخص الذي فتح معلومات  بعد اختصار الرابط اذا كان فعلا جاي من الفورما التي انشاء بها الرابط نسمح له غير ذالك نحوله لصفحة الخطاء  
    def dispatch(self, request, *args, **kwargs):
        try:
            #هناك طرق كثيرة واكثر حماية لكن نستخدم هذه  الطريقة 
            #نشيك هل فعل الشخص اتى من صفحة انشاء الرابط عن طريق HTTP_REFERER  
            # اذا كان لا سوف نوجهة الي صفحة انشاء الرابط  
            if not '/Create/' in str(request.META.get('HTTP_REFERER')):
                return redirect('/')

            return super().dispatch(request, *args, **kwargs)

        #لتفادي اي خطاء  نحوله ايضا الي الصفحة الرئيسية
        except:
            return redirect('/')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # ناتي ببيانات الرابط المختصر 
        GetData = get_object_or_404(ShortcutUrl, shorten_url=self.kwargs['code'])
        #هذا الامر لنقول للتمبلت نريد عرض الرابط  الذي تم اختصاره 
        context['CMD'] = "ShowRow"
        # data اسم الاوجكت في التمبلت راح يكون 
        context['data'] = GetData
        return self.render_to_response(context)




#########################  منطقة عرض الروابط المختصرة والتوجية  ##############################


##كلاس فورما  اذا كان يوجد كلمة مرور نستدعية 
class PasswordForm(forms.Form):
    password    = forms.CharField(label=_("ادخل كلمة المرور"), widget=forms.PasswordInput())



# فنكشن لفتح الرابط المختصر وهنا نتحكم اكثر في بعض الامور قبل التحويل الي الرابط الحقيقي
def open_url(request,code):
    link_correct = 'linksShortcut/open_url.html'
    link_correct_with_password = 'linksShortcut/open_urlpassword.html'
    link_error = 'linksShortcut/error_url.html'
    try:

        #نجلب بيانات الرابط
        get_data = get_object_or_404(ShortcutUrl,shorten_url=code)

        # اذا كانت حالة الرابط غير فعال نرجع صفحة الخطاء
        if not get_data.status:
            return render(request,link_error)
        
        # هنا نشيك هل في كلمة مرور على الرابط ام لا 
        # اذا كان ذالك نحول الشغل على صفحة كلمة المرور ليدخلها 
        if get_data.password:
            form_pass = PasswordForm()
            ##########################################
            # اذا كلمة المرور خطاء .. سوف نرجع الفورما 
            #ولكن هنا نريد ان نستخدم شي وهو  السيشن  ..  ك نوع من زيادة المعلومات وطريقة عمله  
            # وهو ان نجعل الشخص الذي يدخل كلمة المرور 3 مرات خطاء  نحوله لصفحة الخطاء ولا نجعله يدخل الي الصفحة مره اخرى 
            # طبعن هناك طرق كثير  اما عن طريق الايبي وتسجيله في قاعد البياانات 
            #  sessions ولكن نحن سوف نستخد  
            ##########################################
            #نشيك هل نحن قد قمنا بتسجيل سشن قبل ام لا اذا كان لا سوف نسجله ونجعل قيمة صفر 
            if not request.session.has_key('block'):
                request.session['block'] = 0
            # اذا كان نعم 
            else:
                # سوف نشيك هل فعلا تعدى وصل الي 3 مرات خطاء اذا كان ذالك سوف نحوله الي صفحة الخطاء 
                if request.session['block'] == 3 :
                    return render(request,link_error)
            #نعمل قاموس كي نرجع الفورما او تضيف معها بيانات ان اردت  

            print(request.session['block'])
            context = {
                "form":form_pass,
                #مثال اذا تبي تضيف مفتاح مع الداتا الي ترجع للتمبلت  وتستدعي المفتاح بالتمبلت
                # "msg": "مثال",
                }

            #هنا نشيك هل فعلا الشخص دخل الصفحة وحاول ارسال البيانات  .. لان نستخدم  التشيك من كلاس الفورما سوف نستخدم مباشرة .. كي ننوع وتصل بعض المفاهم للمبتدين  
            if request.method == 'POST': # and request.is_ajax()
                #نستدعي كلمة المرور التي تم تسجيلها اثناء انشاء الرابط المختصر  ونقارن هل متطابقة مع التي استقبالها من الفورما 
                if get_data.password == request.POST['password']:
                    #اذا نعم متطابقه لانعمل شي ونخلي الفنكشن تستمر
                    #هنا نضيف امر هل الشخص اخطاء بكلمة المرور من قبل اذا موجودة سوف نمسح السيشن 
                    if request.session.has_key('block'):
                        del request.session['block']
                else:
                    #اذا كانت كلمة المرور غير مطابقة سوف نضيف بالسيشن زيادة على رقم السيشن  
                    request.session['block'] += 1

                    return render(request,link_correct_with_password,context)

            else:
                return render(request,link_correct_with_password,context)


        #اذا كانت عدد ايام الرابط انتهت  نشيك هل فعلا  كانت هناك عدد أيام للرابط في هذا الحقل 
        # اذكرك  بالحقل المخفي الي في الموديل  هنا نستفيد منه  اذا كان  رقم 2 موجود  فمعناته ان الشخص استعمل عدد أيام للرابط وهنا نبدى نستخدمه
        if "2" in get_data.hidden_field:
            #نأتي بتاريخ انشاء الرابط 
            c_date = get_data.created_date
            #نضيف الايام المسجلة بتاريخ الانتهاء 
            add_days =  c_date + datetime.timedelta(days=get_data.expired_date)  # days, seconds, then other fields.
            #نسجل تاريخ اليوم الحالي
            date_now = datetime.datetime.now().date()
            # عملية مقارنه هل تاريخ اليوم اكبر من تاريخ الانتهاء اذا نعم  معناته تم انتهاء الرابط
            if date_now > add_days:
                #نعمل اغلاق لحالة الرابط 
                get_data.status = False
                #نحذف الرقم 2 من الحقل المخفي 
                get_data.hidden_field = get_data.hidden_field.replace('2','')
                # نحفظ البيانات 
                get_data.save()
                #نرجع الصفحة الغلط
                return render(request,link_error)

        #اذا كانت عدد مرات الضعط على الرابط انتهت  ونشيك هل فعلا  كانت هناك عدد محدد للرابط في هذا الحقل 
        # اذكرك  بالحقل المخفي الي في الموديل  هنا نستفيد منه  اذا كان  رقم 1 موجود  فمعناته ان الشخص استعمل عدد عدد محدد للرابط وهنا نبدى نستخدمه
        if "1" in get_data.hidden_field:
            #نشيك هل العدد المحدد لزيرات الرابط انتهت ؟
            if get_data.count_click == 0:
                #اذا عدد الزيارات للرابط انتهت نغلق حالة الرابط 
                get_data.status = False
                #نحذف الرقم 1 من الحقل المخفي 
                get_data.hidden_field = get_data.hidden_field.replace('1','')
                # نحفظ البيانات 
                get_data.save()
                #نرجع الصفحة الغلط
                return render(request,link_error)
            #اذا لم نتهتي ننزل رقم 
            else:
                get_data.count_click -= 1 

        ## نزيد عدد مشاهدها الرابط 
        get_data.count_views += 1 
        #نحفظ البيانات 
        get_data.save()

        ##############
        #نجلب وقت الانتظار  من اعدادات التطبيق  
        app_set = ConfigShortcutUrl.obj.get_first_object()
        #نحوله الي رقم صحيح 
        app_set = int(app_set.use_wait)
        ##############
        #هنا نشيك هل فعلا في وقت انتظار للصفحة في اعدادات التطبيق اذا كان لا يوجد سوف نحول الرابط دايركت 
        if app_set == 0:
            #get_data.redirect_url هذا الرابط المباشر الحقيقي الذي ادخله الشخص لختصرة  ناتبي به
            return redirect(get_data.redirect_url)


        ## هنا اذا كان في وقت انتظار في اعدادات التطبيق  نعرض الوقت الصفحة وفيها الوقت ثم نحولها بعد انتهاء الوقت  open_url.html  مع البيانات الي نحتاحها
        #نعمل قاموس ونضع في وقت الانتظار + الرابط  المباشر الحقيقي 
        context = {
            "time": app_set,
            "url": get_data.redirect_url
        }
        return render(request,link_correct,context)

    except:

        return render(request,link_error)

