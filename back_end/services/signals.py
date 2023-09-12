
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SectorApprovedRequest, Request, ApprovedRequest

@receiver(post_save, sender=Request)
def create_sector_approved_request(sender, instance, created, **kwargs):
    print('signal')
    if instance.approved == True:
        SectorApprovedRequest.objects.create(
            sector=instance.sector,
            user=instance.user,
            genocide_survivor_certificate=instance.genocide_survivor_certificate,
            social_status_class=instance.social_status_class,
            deprived_certificate=instance.deprived_certificate,
            message=instance.message,
            approved=False
        )

@receiver(post_save, sender=SectorApprovedRequest)
def create_approved_request(sender, instance, created, **kwargs):
    print('signal')
    if instance.approved == True:
        ApprovedRequest.objects.create(
            sector=instance.sector,
            user=instance.user,
            genocide_survivor_certificate=instance.genocide_survivor_certificate,
            social_status_class=instance.social_status_class,
            deprived_certificate=instance.deprived_certificate,
            message=instance.message,
        )