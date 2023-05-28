from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField()
    passwd = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.passwd}"


class SignIn(models.Model):
    name = models.CharField(max_length=30)
    passwd = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.passwd}"

class First(models.Model):
    wall_width = models.CharField(max_length=40)
    room_width = models.CharField(max_length=40)
    room_length = models.CharField(max_length=40)
    room_height = models.CharField(max_length=40)
    toilet_x_сoordinate = models.CharField(max_length=40)
    toilet_y_сoordinate = models.CharField(max_length=40)
    toilet_z_сoordinate = models.CharField(max_length=40)
    shell_x_coordinate = models.CharField(max_length=40)
    shell_y_coordinate = models.CharField(max_length=40)
    shell_z_coordinate = models.CharField(max_length=40)


class Second(models.Model):
    wall_width = models.CharField(max_length=40)
    first_room_width = models.CharField(max_length=40)
    first_room_length = models.CharField(max_length=40)
    first_room_height = models.CharField(max_length=40)
    toilet_x_сoordinate = models.CharField(max_length=40)
    toilet_y_сoordinate = models.CharField(max_length=40)
    toilet_z_сoordinate = models.CharField(max_length=40)
    first_shell_x_coordinate = models.CharField(max_length=40)
    first_shell_y_coordinate = models.CharField(max_length=40)
    first_shell_z_coordinate = models.CharField(max_length=40)
    second_room_width = models.CharField(max_length=40)
    second_room_length = models.CharField(max_length=40)
    second_room_height = models.CharField(max_length=40)
    second_shell_x_coordinate = models.CharField(max_length=40)
    second_shell_y_coordinate = models.CharField(max_length=40)
    second_shell_z_coordinate = models.CharField(max_length=40)
    bath_x_сoordinate = models.CharField(max_length=40)
    bath_y_сoordinate = models.CharField(max_length=40)
    bath_z_сoordinate = models.CharField(max_length=40)

class third(models.Model):
    wall_width = models.CharField(max_length=40)
    room_width = models.CharField(max_length=40)
    room_length = models.CharField(max_length=40)
    room_height = models.CharField(max_length=40)
    toilet_x_сoordinate = models.CharField(max_length=40)
    toilet_y_сoordinate = models.CharField(max_length=40)
    toilet_z_сoordinate = models.CharField(max_length=40)
    shell_x_coordinate = models.CharField(max_length=40)
    shell_y_coordinate = models.CharField(max_length=40)
    shell_z_coordinate = models.CharField(max_length=40)
    bath_x_сoordinate = models.CharField(max_length=40)
    bath_y_сoordinate = models.CharField(max_length=40)
    bath_z_сoordinate = models.CharField(max_length=40)
    x_room_curvature_coordinate = models.CharField(max_length=40)
    y_room_curvature_coordinate = models.CharField(max_length=40)
    













