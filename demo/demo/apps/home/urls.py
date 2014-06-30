from django.conf.urls import patterns, include, url

urlpatterns = patterns('demo.apps.home.views',
    url(r'^$', 'index',name="Principal"),
    #url(r'^about/$', 'about',name="About"),
    url(r'^productos/$', 'productos',name="Productos"),    
    url(r'^form/$', 'contacto',name="Contacto"),    
)
