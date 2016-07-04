from django.utils.translation import ugettext_lazy as _


CONFIG = {
    'SEARCH_URL': '/admin/accounts/user/',
    'MENU': (
        'sites',
        {'label': _('accounts'), 'icon': 'icon-user',
         'models': ('accounts.user',
                    {'label': '员工', 'icon': 'icon-book', 'url': '/admin/accounts/user/?aaaaaa=1', 'blank': False},
                    'auth.group',
                    {'label': 'weibo', 'model': 'accounts.WBUid'})},
#         {'app': 'cash', 'label': _('cash'), 'icon': 'icon-signal'},
#         '-',
#         {'app': 'orders', 'label': _('orders'), 'icon': 'icon-signal'},
#         {'app': 'transactions', 'label': _('transactions'), 'icon': 'icon-heart'},
#         '-',
#         {'app': 'assets', 'label': _('assets'), 'icon': 'icon-file'},
#         {'app': 'projects', 'label': _('projects'), 'icon': 'icon-star'},
#         {'app': 'products', 'label': _('products'), 'icon': 'icon-shopping-cart'},
#         {'app': 'coupons', 'label': _('coupons'), 'icon': 'icon-tags'},
#         {'app': 'organizations', 'label': _('organizations'), 'icon': 'icon-signal'},
#         '-',
#         {'app': 'files', 'label': _('files'), 'icon': 'icon-file'},
#         {'label': _('content'), 'icon': 'icon-bookmark', 'models': ('articles.article', 'videos.video')},
#         {'app': 'cards', 'label': _('cards'), 'icon': 'icon-signal'},
#         {'app': 'specials', 'label': _('specials'), 'icon': 'icon-signal'},
#         {'app': 'featured', 'label': _('featured'), 'icon': 'icon-signal'},
#         {'app': 'tags', 'label': _('tags'), 'icon': 'icon-hashtag'},
#         '-',
#         {'app': 'notifications', 'label': _('notifications'), 'icon': 'icon-heart'},
#         {'app': 'site', 'label': _('site'), 'icon': 'icon-heart'},
#         {'app': 'ips', 'label': 'IPs', 'icon': 'icon-signal'},
#         '-',
#         {'app': 'comments', 'label': _('comments'), 'icon': 'icon-comment'},
#         {'app': 'likes', 'label': _('likes'), 'icon': 'icon-heart'},
        {'app': 'questions', 'label': _('questions'), 'icon': 'icon-star'},
        '-',
#         {'app': 'popping', 'icon': 'icon-signal'},
#         '-',
#         {'app': 'x', 'icon': 'icon-signal'},
#         {'app': 'x_fabao', 'icon': 'icon-signal'},
#         '-',
#         {'app': 'marketing', 'icon': 'icon-signal'},
#         '-',
#         {'label': 'Settings', 'icon': 'icon-cog', 'models': ('auth.group',)},
        {'label': 'Documentation', 'icon': 'icon-book', 'url': '/developer/', 'blank': True},
#         {'label': 'API', 'icon': 'icon-wrench', 'url': '/api/v1/', 'blank': True},
#         {'label': 'AWS', 'icon': 'icon-hdd', 'url': 'http://console.amazonaws.cn', 'blank': True},
#         {'label': 'DNS', 'icon': 'icon-hdd', 'url': 'http://netcn.console.aliyun.com/core/domain/list', 'blank': True},
#         '-',
#         {'label': 'Redis', 'icon': 'icon-tasks', 'url': '/admin/redisboard/redisserver/'}
    )
}