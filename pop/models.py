from base.models import BaseModel
from django.db import models
import uuid


class POP(BaseModel):
    choice_types = (
        ('CRITICAL', 'Critical'),
        ('MAJOR', 'Major'),
        ('MINOR', 'Minor')
    )

    network_choice_types = (
        ('ONLINE', 'On Line'),
        ('OFFLINE', 'Off Line'),
        ('WARNING', 'Warning')
    )

    id = models.UUIDField(db_column='id', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_column='name', max_length=128)
    code = models.CharField(db_column='code', unique=True, max_length=256)
    address = models.TextField(db_column='address', max_length=360)
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    status = models.CharField(max_length=64, db_column='status', choices=choice_types)
    network_status = models.CharField(max_length=64, db_column='network_status', choices=network_choice_types)
    user = models.ForeignKey('account.CustomUser', db_column='user_id', on_delete=models.CASCADE, related_name='user_pops')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'POPs'
        db_table = 'pops'
        ordering = ['-created_at']


class POPDevice(BaseModel):
    choices_types = (
        ('CRITICAL', 'Critical'),
        ('MAJOR', 'Major'),
        ('MINOR', 'Minor')
    )

    id = models.UUIDField(db_column='id',default=uuid.uuid4, editable=False, primary_key=True)
    pop_name = models.ForeignKey(POP , db_column='pop_name', on_delete=models.CASCADE)
    code = models.CharField(db_column='code', unique=True, max_length=256)
    name = models.CharField(db_column='name', max_length=256)
    status = models.CharField(max_length=64, db_column='status', choices=choices_types)
    remark = models.TextField(db_column='remark', max_length=512, null=True, blank=True)
    phy_details = models.JSONField(db_column='phy_details', null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = 'Pop Devices'
        db_table = 'pop_devices'
        ordering = ['-created_at']

        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['status']),
            models.Index(fields=['is_active']),
            models.Index(fields=['created_at']),
        ]


class POPDeviceState(BaseModel):
    choice_types = (
        ('TODAY', 'Today'),
        ('LAST_7_DAYS', 'Last 7 days'),
        ('LAST_30_DAYS', 'Last 30 days'),
        ('THIS_YEAR', 'This Year'),
    )

    id = models.UUIDField(db_column='id', primary_key=True, default=uuid.uuid4, editable=False)
    device_code = models.ForeignKey(POPDevice, db_column='device_code', on_delete=models.CASCADE)
    topic = models.CharField(db_column='topic', max_length=256)
    time_range = models.CharField(max_length=256, db_column='time_range', choices=choice_types)
    data = models.JSONField(db_column='data')

    def __str__(self):
        return f'{self.device_code}'

    class Meta:
        verbose_name_plural = 'Pop Device States'
        db_table = 'pop_device_states'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['is_active'])
        ]

