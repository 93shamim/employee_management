# Generated by Django 5.1.1 on 2024-09-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_empid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Team Lead', 'Team Lead'), ('Developer', 'Developer'), ('Tester', 'Tester'), ('HR', 'HR')], max_length=50),
        ),
    ]
