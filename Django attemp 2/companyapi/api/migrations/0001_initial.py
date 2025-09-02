# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('established', models.DateField()),
                ('type', models.CharField(choices=[('startup', 'Startup'), ('small_business', 'Small Business'), ('enterprise', 'Enterprise')], max_length=50)),
            ],
        ),
    ]
