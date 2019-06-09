# Generated by Django 2.2.2 on 2019-06-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionalFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('f_type', models.IntegerField(choices=[(0, 'EE'), (1, 'CE'), (2, 'SE')], verbose_name='Functionality type')),
                ('qt_ALR', models.IntegerField()),
                ('qt_DER', models.IntegerField()),
                ('function_points', models.IntegerField()),
                ('counter_name', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('complexity', models.CharField(choices=[('Alta', 'Alta'), ('Media', 'Media'), ('Baixa', 'Baixa')], max_length=50)),
            ],
        ),
    ]
