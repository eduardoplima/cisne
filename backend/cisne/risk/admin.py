from django.contrib import admin

# Register your models here.
from .models import MacroProcess, Process, Event, EventCategory,\
EventNature, EventCause, EventConsequence, Control, ActionObjective,\
ActionPlan, ActionType, EventCalculator, ControlDesign, ControlOperation, RiskResponse, UserRole\
, Organization, Period

admin.site.register(Organization)
admin.site.register(Period)
admin.site.register(UserRole)
admin.site.register(MacroProcess)
admin.site.register(Process)
admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventNature)
admin.site.register(EventCause)
admin.site.register(EventConsequence)
admin.site.register(Control)
admin.site.register(ActionObjective)
admin.site.register(ActionPlan)
admin.site.register(ActionType)
admin.site.register(EventCalculator)
admin.site.register(ControlDesign)
admin.site.register(ControlOperation)
admin.site.register(RiskResponse)