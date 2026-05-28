from django.contrib import admin
from .models import (
    Company,
    SourceUpload,
    RawRecord,
    NormalizedRecord,
    AuditLog
)

admin.site.register(Company)
admin.site.register(SourceUpload)
admin.site.register(RawRecord)
admin.site.register(NormalizedRecord)
admin.site.register(AuditLog)