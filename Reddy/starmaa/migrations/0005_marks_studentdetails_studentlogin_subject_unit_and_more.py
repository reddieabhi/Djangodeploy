# Generated by Django 4.2.4 on 2023-12-01 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("starmaa", "0004_people_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marks", models.IntegerField(default=25)),
            ],
        ),
        migrations.CreateModel(
            name="StudentDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("st_name", models.CharField(max_length=100)),
                ("st_birth_year", models.IntegerField(default=2001)),
                (
                    "st_birth_place",
                    models.CharField(default="Hyderabad", max_length=100),
                ),
                ("st_parent_name", models.CharField(max_length=100)),
                ("st_standard", models.IntegerField(default=9)),
            ],
        ),
        migrations.CreateModel(
            name="StudentLogin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("student_id", models.CharField(max_length=100, unique=True)),
                ("login_id", models.IntegerField(unique=True)),
                ("login_password", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "unit_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("unit_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="People",
        ),
        migrations.AddField(
            model_name="studentdetails",
            name="student_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_details",
                to="starmaa.studentlogin",
            ),
        ),
        migrations.AddField(
            model_name="marks",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="marks",
                to="starmaa.studentlogin",
            ),
        ),
        migrations.AddField(
            model_name="marks",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="marks",
                to="starmaa.subject",
            ),
        ),
        migrations.AddField(
            model_name="marks",
            name="unit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="marks",
                to="starmaa.unit",
            ),
        ),
    ]