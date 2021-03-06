from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0002_auto_20190406_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='algorithm',
            field=models.CharField(choices=[('RS256', 'RSA with SHA-2 256'), ('HS256', 'HMAC with SHA-2 256')], default='RS256', max_length=5),
        ),
        migrations.AlterField(
            model_name='application',
            name='authorization_grant_type',
            field=models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials'), ('openid-hybrid', 'OpenID connect hybrid')], max_length=32),
        ),
    ]
