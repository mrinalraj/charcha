# Generated by Django 3.0.7 on 2020-07-12 09:20

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'permissions',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discussions.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discussions.Role')),
            ],
            options={
                'db_table': 'role_permissions',
            },
        ),
        migrations.RemoveField(
            model_name='grouprole',
            name='permissions',
        ),
        migrations.AlterModelOptions(
            name='groupgchatspace',
            options={'verbose_name': 'Chat Room'},
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(help_text='A larger description that can contain links, charter or any other text to better describe the group', max_length=4096),
        ),
        migrations.AlterField(
            model_name='group',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), help_text='Mailing list address for this group', size=8),
        ),
        migrations.AlterField(
            model_name='group',
            name='gchat_spaces',
            field=models.ManyToManyField(help_text='Associate this group to one or more gchat rooms. This has two purposes - 1) to automatically import members from the gchat room, and 2) to notify the gchat room when a new post is added', through='discussions.GroupGchatSpace', to='discussions.GchatSpace', verbose_name='Google chat rooms associated with this group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Closed'), (2, 'Secret')], help_text="Closed groups can be seen on the listing page and request an invitation, but only members can see the posts. Secret groups don't show up on the listing page."),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(help_text='Members of this group', related_name='mygroups', through='discussions.GroupMember', to=settings.AUTH_USER_MODEL, verbose_name='Members of this group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(help_text='Name of the group', max_length=30),
        ),
        migrations.AlterField(
            model_name='group',
            name='purpose',
            field=models.CharField(help_text='A 1 or 2 sentence explaining the purpose of this group', max_length=200),
        ),
        migrations.AlterField(
            model_name='groupgchatspace',
            name='gchat_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discussions.GchatSpace', verbose_name='Room Name'),
        ),
        migrations.AlterField(
            model_name='groupgchatspace',
            name='notify',
            field=models.BooleanField(default=True, help_text='Notify the chat room whenever a new post is created in this charcha group'),
        ),
        migrations.AlterField(
            model_name='groupgchatspace',
            name='sync_members',
            field=models.BooleanField(default=True, help_text='Automatically sync chat room members with this charcha group'),
        ),
        migrations.DeleteModel(
            name='GroupPermission',
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(related_name='roles', through='discussions.RolePermission', to='discussions.Permission'),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discussions.Role'),
        ),
        migrations.DeleteModel(
            name='GroupRole',
        ),
    ]