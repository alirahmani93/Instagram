# Generated by Django 3.2.7 on 2021-09-24 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insta.log')),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'man'), ('f', 'female'), ('o', 'other')], max_length=1, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/Profile/%s')),
                ('is_active', models.BooleanField(default=False)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('protected_profile', models.BooleanField(default=False)),
                ('fg', models.ManyToManyField(default=None, related_name='fg', to=settings.AUTH_USER_MODEL)),
                ('fw', models.ManyToManyField(default=None, related_name='fw', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('insta.log',),
        ),
        migrations.CreateModel(
            name='Post_testtttt',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insta.log')),
                ('caption', models.TextField(blank=True, max_length=300, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/Profile/%s')),
                ('comment_is_active', models.BooleanField(default=True)),
                ('is_archaive', models.BooleanField(default=False)),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('post_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('insta.log',),
        ),
        migrations.CreateModel(
            name='FollowPendingRequests',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insta.log')),
                ('follow_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_receiver', to=settings.AUTH_USER_MODEL)),
                ('follow_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_sender', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('insta.log',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='insta.log')),
                ('body', models.CharField(max_length=1000)),
                ('target_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='insta.post_testtttt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='insta.profile')),
            ],
            bases=('insta.log',),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['user'], name='insta_profi_user_id_054e45_idx'),
        ),
        migrations.AddIndex(
            model_name='post_testtttt',
            index=models.Index(fields=['caption'], name='insta_post__caption_73ecf4_idx'),
        ),
    ]
