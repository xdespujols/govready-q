# Generated by Django 3.2.14 on 2022-08-14 18:18

from django.db import migrations, models
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0069_alter_project_import_record'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('name', models.CharField(blank=True, help_text='Descriptive name', max_length=100, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unique identifier')),
                ('description', models.CharField(blank=True, help_text='Brief description', max_length=250, null=True)),
                ('recipe', models.TextField(blank=True, help_text='Workflow instructions', null=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='workflowrecipe', to='siteapp.Tag')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
