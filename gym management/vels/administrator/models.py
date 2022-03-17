# from datetime import date
# from distutils.command.upload import upload
# from email import message
from django.db import models
# Create your models here.
class Enquirys(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=11)
    message = models.TextField()
    small_message = models.CharField(max_length=20)

    joining_date = models.DateField(blank=True,null=True)
    visit_types = (
        ('Call', 'c'),
        ('Directly', 'd'),
    )
    visit_type = models.CharField(max_length=10,blank=True, choices=visit_types)

    timming = models.TimeField(auto_now_add=True)
    When =models.DateField(auto_now_add=True)
    
    
    def info(self)->str:
        return f"""
    Name :{self.name}
    Number :{self.message}
    Enrolled :{str(self.When)+str(self.timming)}
    Joining date :{str(self.joining_date)}
    Message :{self.message}
    Visit type :{self.visit_type}
    """
    
    def __str__(self) -> str:
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    memberId=models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    joined = models.DateField()
    expiry = models.DateField()
    image       = models.ImageField(default="default/person.png",blank=True,null=True,upload_to='./')
    shift="Morning"
    shift_types = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )
    shift_type = models.CharField(max_length=10,choices=shift_types,default=shift)
    # comming_time =  models.CharField(max_length=500,blank=True,null=True,default="0")

    message = models.TextField(blank=True)
    hold = models.BooleanField(default=False)
    hold_date = models.DateField(blank=True,null=True)
    hold_reason= models.CharField(max_length=100,blank=True)
    dark_color = ""
    colors_types = (
        ('danger', 'danger'),
        ('warning', 'warning'),
        ('success', 'success'),
        ('info', 'info'),
        ('secondary', 'secondary'),
        
        (dark_color, ''),
    )
    color = models.CharField(max_length=30,blank=True, choices=colors_types,default=dark_color) 
    color_message = models.CharField(blank=True, max_length=30,default=" ")
    # color
    def info(self)->str:
        return f"""
    Name :\t{self.name}\t
    Member Id :{self.memberId}
    Number :{self.message}
    joined :{self.joined}
    shift :{self.shift_type}
    Message :{self.message}
    expiry :{self.expiry}
    
    """
        

    def __str__(self) -> str:
        return self.name

def default_values():
    return Member.objects.all()

class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(Member,related_name="+" ,blank=True )  
    # absentees = models.ManyToManyField(Member,related_name="+",blank=False,default=default_values) 
    absentees = models.ManyToManyField(Member,related_name="+",blank=True) 


    def __str__(self) -> str:
            return str(self.date)

class Absentees(models.Model):
    date = models.DateField(auto_now=True)
    member = models.ForeignKey(Member,null=True,blank=True,on_delete=models.CASCADE)
    days_count = models.IntegerField(default=0,blank=True,null=True)
    # Present_count = models.IntegerField(default=0,blank=True,null=True)/

    def __str__(self) -> str:
        out = str(self.member)+" -- "+str(self.days_count)
        return out

class History(models.Model):
    date = models.DateField(auto_now_add=True)
    event  =  models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.date )+ " " +self.event

class Notes(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return self.title

 


























    
