
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import SectorApprovedRequest, Request, ApprovedRequest
from django.core.mail import send_mail
from django.conf import settings


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
        # send email as well
        print('approved')
        subject = 'Sheltering Provision For Genocide Survivors'
        message = 'Your request for sheltering provision as a genocide survivor, has been approved on a sector level, Your request have been sent  to MINUBUMWE for further processing. Please contact the sector administration for more information.'
        from_email = 'jadon6dev@gmail.com'
        to_list = [instance.user.email]
        if instance.user.email is not None:
            send_mail(subject, message, from_email, to_list, fail_silently=True)

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
        # send email as well
        print('approved')
        subject = 'Sheltering Provision For Genocide Survivors' 
        message = 'Your request for sheltering provision as a genocide survivor, has been approved At MINUBUMWE, The administration will reach out to you for more information.'
        from_email = 'jadon6dev@gmail.com'
        to_list = [instance.user.email]
        if instance.user.email is not None:
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            

# on request rejected send email to user
@receiver(post_save, sender=Request)
def send_email_to_user(sender, instance, created, **kwargs):
    print('signal')
    if instance.rejected == True and instance.approved == False:
        print('rejected')
        subject = 'Sheltering Provision For Genocide Survivors'
        message = 'Your request for sheltering provision as a genocide survivor, has been rejected on a sector level, You may have provided incomplete documents or the administration have found you do not qualify for This service, Please contact the sector administration for more information.'
        from_email = 'jadon6dev@gmail.com'
        to_list = [instance.user.email]
        print(from_email)
        if instance.user.email is not None:
            send_mail(subject, message, from_email, to_list, fail_silently=True)    

# on SectorApprovedRequest rejected send email to user
@receiver(post_save, sender=SectorApprovedRequest)
def send_email_to_user(sender, instance, created, **kwargs):
    print('signal')
    if instance.rejected == True and instance.approved == False:
        print('rejected')
        subject = 'Sheltering Provision For Genocide Survivors'
        message = 'Your request for sheltering provision as a genocide survivor, has been rejected At MINUBUMWE, You may have provided incomplete documents or the administration have found you do not qualify for This service, Please contact administration for more information.'
        from_email = 'jadon6dev@gmail.com'
        to_list = [instance.user.email]
        print(from_email)
        if instance.user.email is not None:
            send_mail(subject, message, from_email, to_list, fail_silently=True)
