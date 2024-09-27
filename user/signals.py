# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CartItem,Cart

# @receiver(post_save,sender=CartItem)
# def handle_cart_item(sender,instance,created,**kwargs):
#     if created:
#         user=instance.user
#         if not Cart.objects.filter(user=user).exists():
#             Cart.objects.create(user=user)
        