from django.contrib import admin
from. models import CustomUser, createparentss, createstaffs, datas,TeacherExtra,StudentExtra,upload_image

# Register your models here.
admin.site.register(datas)
admin.site.register(createstaffs)
admin.site.register(createparentss)
admin.site.register(CustomUser)
admin.site.register(TeacherExtra)
admin.site.register(StudentExtra)
admin.site.register(upload_image)


