from django.db import models

class member_data(models.Model):
    member_name = models.CharField(max_length=100, default='ناشناس')
    member_sedigh = models.IntegerField(max_length=100, default='عمومی')

    def __str__(self):
        return self.member_name

class PresenceRecord(models.Model):
    member = models.ForeignKey(member_data, on_delete=models.CASCADE)
    present = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
class form_info(models.Model):
    form_date = models.CharField()
    form_type = models.CharField(null = False)    
    def __str__(self):
        return self.form_type
class admin_data(models.Model):
    admin_name = models.CharField(null=False)
    latest_login = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.admin_name          