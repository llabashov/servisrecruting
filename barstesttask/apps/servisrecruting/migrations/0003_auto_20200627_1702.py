# Generated by Django 3.0.6 on 2020-06-27 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servisrecruting', '0002_auto_20200521_0910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recrut',
            options={'verbose_name': 'Рекрут', 'verbose_name_plural': 'Рекруты'},
        ),
        migrations.AddField(
            model_name='recrut',
            name='recrut',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='servisrecruting.Planet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sith',
            name='planet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='servisrecruting.Planet'),
            preserve_default=False,
        ),
    ]