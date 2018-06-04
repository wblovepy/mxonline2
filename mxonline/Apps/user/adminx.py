import xadmin
from .models import  EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    # 基础主题
    enable_themes = True  # 不能写错，写错了也不报错，themes，不是thems
    use_bootswatch = True # 不加这一句或者写错了就只有一个主题

class GlobleSettings(object): # 全局管理
    site_title = '慕学OL'  #title不能写成tittle  , 左上角图标
    site_footer = 'WanBin_Django'  # 页面中间页脚
    menu_style = 'accordion'  # 左边导航栏收起来

""" 不能像admin继承admin.ModelAdmin, 而是直接继承object"""
class EmailVerifyRecordAdmin(object):
    """list_display是在admin中显示详细信息的字段，专用名字"""
    list_display = ['code', 'email', 'send_type','send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type','send_time']

class BannerAdmin(object):
    list_display = ['tittle', 'image', 'url', 'index','add_time']
    search_fields = ['tittle', 'image', 'url', 'index']
    list_filter = ['tittle', 'image', 'url', 'index','add_time']

xadmin.site.register( EmailVerifyRecord,  EmailVerifyRecordAdmin)
xadmin.site.register( Banner,  BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobleSettings)