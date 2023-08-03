from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import contact, MailingListView, MailingDetailView, MailingCreateView, \
    MailingUpdateView, MailingDeleteView, main, MessageCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('contact/', contact, name='contact'),
    path('main/', main, name='main'),
    path('view/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('edit/<int:pk>', MailingUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)