import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import book.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_review.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  
    "websocket": URLRouter(book.routing.websocket_urlpatterns)
    
})