from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    established = models.DateField()
    type = models.CharField(
        max_length=50,
        choices=[
            ("startup", "Startup"),
            ("small_business", "Small Business"),
            ("enterprise", "Enterprise"),
        ],
    )

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(
        Company, related_name="employees", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    position = models.CharField(
        max_length=100,
        choices=[
            ("manager", "Manager"),
            ("developer", "Developer"),
            ("designer", "Designer"),
        ],
    )
    date_hired = models.DateField()

    def __str__(self) -> str:
        return self.name