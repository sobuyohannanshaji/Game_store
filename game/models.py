from django.db import models


class Userone(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    gender_choices=(('male','male'),('female','female'),)
    gender=models.CharField(max_length=10,choices=gender_choices)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    avatar=models.ImageField(upload_to='upload/user/images',default=True)

    def __str__(self):
        return self.name



class game_details(models.Model):
    game_name=models.CharField(max_length=100)
    game_video1=models.FileField(upload_to='upload/game/videos')
    game_video2=models.FileField(upload_to='upload/game/videos')
    game_avatar=models.ImageField(upload_to='upload/game/images')
    game_images=models.ImageField(upload_to='upload/game/images')
    game_choice=(('free','free'),('paid','paid'),)
    game_type=models.CharField(max_length=4,choices=game_choice,default=False)
    game_amt=models.CharField(max_length=100)
    game_file =models.FileField(upload_to='upload/game/file',default=True)



    def __str__(self):
        return self.game_name

class Payment_details(models.Model):
    email = models.ForeignKey(Userone,on_delete=models.CASCADE,null=True)
    game_name = models.ForeignKey(game_details, on_delete=models.CASCADE, null=True)
    card_holder_name=models.CharField(max_length=100)
    card_number=models.IntegerField()
    card_cvc=models.IntegerField()
    card_year=models.CharField(max_length=100)


    def __str__(self):
        return self.card_holder_name

class Account(models.Model):
    bal=models.CharField(null=True,max_length=100)
    email = models.ForeignKey(Userone,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.bal


class adminpage(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.user_name




class feedback(models.Model):
    name = models.ForeignKey(Userone, on_delete=models.CASCADE, null=True)
    feedbacks = models.CharField(max_length=100)
    reply= models.CharField(max_length=100)

    def __str__(self):
        return self.feedbacks

class review(models.Model):
    name = models.ForeignKey(Userone, on_delete=models.CASCADE, null=True)
    game_name = models.ForeignKey(game_details, on_delete=models.CASCADE, null=True)
    review = models.CharField(max_length=100)
    reply_review = models.CharField(max_length=100,default=0)


    def __str__(self):
        return self.review

class ApplyForm(models.Model):
    file=models.FileField(upload_to='upload/game/file')