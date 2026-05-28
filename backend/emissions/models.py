from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SourceUpload(models.Model):
    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('FAILED', 'Failed'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    file_name = models.CharField(max_length=255)
    uploaded_by = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.source_type} - {self.file_name}"


class RawRecord(models.Model):
    PARSE_STATUS = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    source_upload = models.ForeignKey(SourceUpload, on_delete=models.CASCADE)
    raw_data = models.JSONField()
    row_number = models.IntegerField()
    parse_status = models.CharField(max_length=20, choices=PARSE_STATUS)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Row {self.row_number}"


class NormalizedRecord(models.Model):
    STATUS_CHOICES = [
        ('PENDING_REVIEW', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_upload = models.ForeignKey(SourceUpload, on_delete=models.CASCADE)

    scope = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)

    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    normalized_quantity = models.FloatField()
    normalized_unit = models.CharField(max_length=50)

    period_start = models.DateField()
    period_end = models.DateField()

    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    suspicious_flag = models.BooleanField(default=False)

    approved_by = models.CharField(max_length=255, blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)

    locked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category} - {self.activity_type}"


class AuditLog(models.Model):
    normalized_record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=255)

    old_value = models.JSONField(blank=True, null=True)
    new_value = models.JSONField(blank=True, null=True)

    changed_by = models.CharField(max_length=255)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action