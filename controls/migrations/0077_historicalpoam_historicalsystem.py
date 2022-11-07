# Generated by Django 3.2.14 on 2022-07-18 19:23

import auto_prefetch
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controls', '0076_system_import_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSystem',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('fisma_id', models.CharField(blank=True, help_text='The FISMA Id of the system', max_length=40, null=True)),
                ('info', models.JSONField(blank=True, default=dict, help_text='JSON object representing additional system information')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('import_record', auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The Import Record which created this System.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.importrecord')),
                ('root_element', auto_prefetch.ForeignKey(blank=True, db_constraint=False, help_text='The Element that is this System. Element must be type [Application, General Support System]', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.element')),
            ],
            options={
                'verbose_name': 'historical system',
                'verbose_name_plural': 'historical systems',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPoam',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('poam_id', models.IntegerField(blank=True, help_text='The sequential ID for the information system.', null=True)),
                ('controls', models.CharField(blank=True, help_text='Comma delimited list of security controls affected by the weakness identified.', max_length=254, null=True)),
                ('weakness_name', models.CharField(blank=True, help_text='Name for the identified weakness that provides a general idea of the weakness.', max_length=254, null=True)),
                ('weakness_detection_source', models.CharField(blank=True, help_text=' Name of organization, vulnerability scanner, or other entity that first identified the weakness.', max_length=180, null=True)),
                ('weakness_source_identifier', models.CharField(blank=True, help_text='ID or reference provided by the detection source identifying the weakness.', max_length=180, null=True)),
                ('remediation_plan', models.TextField(blank=True, help_text='A high-level summary of the actions required to remediate the plan.', null=True)),
                ('scheduled_completion_date', models.DateTimeField(blank=True, db_index=True, help_text='Planned completion date of all milestones.', null=True)),
                ('milestones', models.TextField(blank=True, help_text='One or more milestones that identify specific actions to correct the weakness with an associated completion date.', null=True)),
                ('milestone_changes', models.TextField(blank=True, help_text='List of changes to milestones.', null=True)),
                ('risk_rating_original', models.CharField(blank=True, help_text='The initial risk rating of the weakness.', max_length=50, null=True)),
                ('risk_rating_adjusted', models.CharField(blank=True, help_text='The current or modified risk rating of the weakness.', max_length=50, null=True)),
                ('poam_group', models.CharField(blank=True, help_text='A name to collect related POA&Ms together.', max_length=50, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('statement', models.ForeignKey(blank=True, db_constraint=False, help_text='The Poam details for this statement. Statement must be type Poam.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='controls.statement')),
            ],
            options={
                'verbose_name': 'historical poam',
                'verbose_name_plural': 'historical poams',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
