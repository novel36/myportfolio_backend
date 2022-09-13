# Generated by Django 4.1.1 on 2022-09-13 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_contactme_education_myskill_personalskill_portfolio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name_plural': 'AboutME'},
        ),
        migrations.AlterModelOptions(
            name='contactme',
            options={'verbose_name_plural': 'ContactMe'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='myskill',
            options={'verbose_name_plural': 'MySkills'},
        ),
        migrations.AlterModelOptions(
            name='personalskill',
            options={'verbose_name_plural': 'PersonalSkills'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Portfolio'},
        ),
        migrations.AlterModelOptions(
            name='professionalskill',
            options={'verbose_name_plural': 'ProfessionalSkills'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='socialmedialinks',
            options={'verbose_name_plural': 'SocialmediaLinks'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='tools',
            options={'verbose_name_plural': 'Tools'},
        ),
    ]
