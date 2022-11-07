from django.contrib import admin

from .models import Claim, ClaimAmount, ClaimApprover, Department, Position, Staff, User

admin.site.register(Claim)
admin.site.register(ClaimAmount)
admin.site.register(ClaimApprover)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(User)
