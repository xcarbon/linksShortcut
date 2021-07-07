
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



#استدعاء الادمن لتسجلية في لوحة التحكم وايضا التعديل فيه 
from django.contrib import admin

# استدعاء المودل  الذي نريد ان نسجلة او انعدل عليه 
from .models import ConfigShortcutUrl,ShortcutUrl



#كلاس للتحكم في اعدادت جدول اعدادت التطبيق عن طريق لوحة التحكم 
@admin.register(ConfigShortcutUrl)
class ConfigShortcutUrlAdmin(admin.ModelAdmin):
    list_display = ['name', 'url',"use_service",'length_url','use_wait']
    # list_editable = ['assortment']
    # form = AppenFieldForViewDataJson

    #وضعنا هذة الميثود كي لايكون هناك اكثر من سجل في اعدادات التطبيق 
    def has_add_permission(self, request, obj=None):
        # هنا نشيك اذا كان لايوجد سجل للاعدادات نسمح ان تضيف اعدادات
        get_setting_app = ConfigShortcutUrl.objects.all().count()
        # اذا كان لايوجد سجل نسمح للادمن انه يضيف سجل واحد فقط 
        if not get_setting_app:
            return True
        else:
            return False

# كلاس للتحكم في اعدادات جدول اختصارات الروابط في لوحة التحكم 
@admin.register(ShortcutUrl)
class ShortcutUrlAdmin(admin.ModelAdmin):
    #عرض البيانات في جدول اختصار الروابط
    list_display = ['shorten_url', 'count_views',"created_by",'created_date','status','count_click','expired_date','password']
    #يمكنك تحرير اغلاق الرابط او فتحة عن طريق قائمة عرض   جدول البيانات 
    list_editable = ['status','count_click']
    #يمكن للادمن البحث بالكود المختصر في لوحة الادمن 
    search_fields = ['shorten_url']
    #لجعل الحقول فقط للقراء 
    readonly_fields = ["shorten_url",'count_views','created_by','created_date',]
    #قبل حفظ البيانات  من لوحة التحكم 
    def save_model(self, request, obj, form, change):
        #هنا اذا كان تعديل على السجل
        if not change:
            # لتحويل الابجكت الي نص لان الحقل ليس له علاقة في جدول اليوزر  str #استخدمنا     
            obj.created_by = str(request.user)
        #هنا اذا كان سجل جديد
        if change:
            # لتحويل الابجكت الي نص لان الحقل ليس له علاقة في جدول اليوزر  str #استخدمنا
            obj.created_by = str(request.user)
        #حفظ البيانات واستدعاء دالة حفظ التي في المودل
        obj.save()

    #وضعنا هذة الميثود كي نتحقق هل هناك اعدادات للتطبيق ام لاء اذا كان لايوجد نمنع اضافة اي سجل  لاختصار الروابط 
    def has_add_permission(self, request, obj=None):
        # هنا نشيك اذا كان لايوجد سجل للاعدادات نجعلها لايمكنه اضافة روابط حتى تكون  الاعدادات جاهزة   معفوس  @xking
        get_setting_app = ConfigShortcutUrl.objects.all().count()
        # اذا كان لايوجد سجل واحد لاعدادات التطبيق نمنع الاضافة  
        if not get_setting_app:
            return False
        else:
            return True

    #هنا نعدل على خصائص السجل على حسب اعدادات التطبيق 
    def get_form(self, request, obj=None, **kwargs):
        i = ConfigShortcutUrl.obj.get_first_object()
        exclude = ()
        if not i.use_limited:
            exclude += ("count_click", )
        if not i.use_expired_date:
            exclude += ("expired_date", )
        if not i.use_password:
            exclude += ("password", )
        self.exclude =  exclude
        form = super(ShortcutUrlAdmin, self).get_form(request, obj, **kwargs)
        return form




