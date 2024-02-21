# Generated by Django 5.0.2 on 2024-02-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_alter_node_completed_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='complete_on_tasks',
            field=models.BooleanField(
                default=False, help_text='Complete node if all depends_on are completed.'
            ),
        ),
        migrations.AlterField(
            model_name='node',
            name='can_be_completed_by',
            field=models.ManyToManyField(blank=True, to='state.role'),
        ),
        migrations.AlterField(
            model_name='node',
            name='depends_on',
            field=models.ManyToManyField(blank=True, related_name='children', to='state.node'),
        ),
        migrations.AlterField(
            model_name='node',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='parents', to='state.node'),
        ),
    ]
