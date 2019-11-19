import xadmin
from xadmin import views


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True  # 引导控制菜单


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)


from app01.models import Book


class BookAdminModel:
    # 控制列表展示的字段 设置默认展示字段
    list_display = ['title', 'price', 'pub_date', 'publish', 'authors']
    # 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
    search_fields = ['id', 'title', 'price']
    # 可以进行过滤操作的列，对于分类、性别、状态
    list_filter = ['id', 'title', 'price', 'publish']
    # 排序，默认升序
    ordering = ['-price']
    # 展示详情信息的字段
    show_detail_fields = ['title']
    # 设置允许直接在展示页编辑的字段
    list_editable = ['price']
    # 设置列表页的刷新频率
    refresh_times = [3, 6, 30, 60]
    # 控制列表页导出数据的可选格式，设置None来禁用数据导出功能
    list_export = ['xls', 'csv', 'json']
    # 控制是否显示书签功能，False表示关闭
    show_bookmarks = True
    # 显示图表数据
    data_charts = {
        'price_total': {
            'title': '书籍单价曲线图',
            'x-field': 'id',
            'y-field': 'price',
            'order': ('id',),
        },
        # 可以有多个图表
        # 'price_total2': {
        #     'title': '书籍单价曲线图2',
        #     'x-field': 'id',
        #     'y-field': 'price',
        #     'order': ('id',),
        # }
    }
    # 控制菜单的图标（图标的设置可以参考boostrap的图标css名称）
    model_icon = 'fa fa-gift'
    # 设置编辑页中只读字段
    readonly_fields = ['title']
    # 设置在编辑页隐藏的字段
    exclude = ['pub_date']

xadmin.site.register(Book, BookAdminModel)