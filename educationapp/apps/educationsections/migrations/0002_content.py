# Generated by Django 3.0.5 on 2020-04-25 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educationsections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('url', models.CharField(max_length=200, verbose_name='ссылка')),
                ('author', models.CharField(max_length=200, verbose_name='автор')),
                ('description', models.TextField(verbose_name='описание')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='educationsections.Section')),
            ],
        ),
    ]