from django.db import models

class MainTab(models.Model):
    label = models.CharField(max_length=100)  

    def __str__(self):
        return self.label

class SubTab(models.Model):
    main_tab = models.ForeignKey(MainTab, related_name='sub_tabs', on_delete=models.CASCADE)  
    label = models.CharField(max_length=100) 
    content = models.TextField() 

    def __str__(self):
        return self.label