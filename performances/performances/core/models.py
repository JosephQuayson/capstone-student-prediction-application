from django.db import models

# Create your models here.

class performancePredict(models.Model):
    CHOICES=[("T", "Together"),
        ("A", 'Apart')]

    REASONS=[
    ("course","Course preference"),
    ("other","Other"),
    ("home","Close to home"),
    ("reputation","School reputation")
    ]

    FAILURES=[("0","No Fail"),
        ("1","Failed once"),
        ("2","Failed Twice"),
        ("3", "Failed Trice")
    ]
    INTERNET=[("yes","yes"),
        ("no","no")
        
    ]
    STUDY_TIME=[
        ("1","2 hours"),
        ("2","From 2 to 5 hours"),
        ("3","From 5 to 10 hours"),
        ("4", "More than 10 hours")
       ]

    FREETIME=[
        ("1","1 hour"),
        ("2","2 hours"),
        ("3","3 hours"),
        ("4","4 hours "),
        ("5","5 hours ")

    ]
    Pstatus=models.CharField(max_length=2, null= True, choices=CHOICES)
    reason=models.CharField(max_length=20, null=True,choices=REASONS)
    studytime=models.CharField(max_length=20, null=True,choices=STUDY_TIME)
    failures=models.CharField(max_length=4,null=True, choices=FAILURES)
    internet=models.CharField(max_length=4,null=True, choices=INTERNET )
    freetime=models.CharField(max_length=4,null=True, choices=FREETIME )
    G1=models.IntegerField()
    G2=models.IntegerField()
    classification=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.classification
