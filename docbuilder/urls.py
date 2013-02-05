from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('doc.views',
    url(r'article/(?P<fileref>[\w.-]+)$', 'docbuilder',
        {'template': 'template/article.tex'}),
    url(r'report/(?P<fileref>[\w.-]+)$', 'docbuilder',
        {'template': 'template/report.tex'}),
    url(r'slide/(?P<fileref>[\w.-]+)$', 'docbuilder',
        {'template': 'template/slide.tex', 'beamer': True}),
)
