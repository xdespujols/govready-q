# Generated by Django 3.2.13 on 2022-05-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0071_system_proposals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicaldeployment',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical deployment', 'verbose_name_plural': 'historical deployments'},
        ),
        migrations.AlterModelOptions(
            name='historicalstatement',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical statement', 'verbose_name_plural': 'historical statements'},
        ),
        migrations.AlterModelOptions(
            name='historicalsystemassessmentresult',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical system assessment result', 'verbose_name_plural': 'historical system assessment results'},
        ),
        migrations.AddField(
            model_name='system',
            name='info',
            field=models.JSONField(blank=True, default=dict, help_text='JSON object representing additional system information'),
        ),
        migrations.AlterField(
            model_name='historicaldeployment',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalsystemassessmentresult',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
