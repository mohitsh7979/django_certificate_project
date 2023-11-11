from django.db import models
from django.contrib.auth.models import User

class Certification(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in hours")
    # price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    completion_date = models.DateField()
    # status = models.CharField(max_length=20, choices=[("in_progress", "In Progress"), ("completed", "Completed"), ("failed", "Failed")])

class CertificateRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("approved", "Approved"), ("denied", "Denied")], default="pending")
    issuing_date = models.DateField(null=True,blank=True)
    issuing_authority = models.CharField(max_length=100)

    def __str__(self):
        return self.certification.title
 


  
