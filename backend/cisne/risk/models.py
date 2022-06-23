from sys import implementation
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization_updated_by')
    users = models.ManyToManyField(User, related_name='organization_users')
    active = models.BooleanField(default=True)
    sector_of = models.ForeignKey('self', on_delete=models.CASCADE, related_name='organization_sector_of', null=True, blank=True)

    def on_create(self):
        Period.objects.create(order=1, organization=self, created_by=self.created_by)

class Period(models.Model):
    order = models.IntegerField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='period_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='period_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='period_organization')

class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_updated_by', null=True, blank=True)
    
class MacroProcess(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='macroprocess_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='macroprocess_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='macroprocess_organization')
    active = models.BooleanField(default=True)

class Process(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='process_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='process_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='process_organization')
    macroprocess = models.ForeignKey(MacroProcess, on_delete=models.CASCADE, related_name='process_macroprocess')
    active = models.BooleanField(default=True)
    approval_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='process_approval_responsible')
    analysis_responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='process_analysis_responsible')

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='event_organization')
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='event_process')
    active = models.BooleanField(default=True)
    inherent_risk = models.ForeignKey('EventCalculator', on_delete=models.CASCADE, related_name='inherent_risk')
    residual_risk = models.ForeignKey('EventCalculator', on_delete=models.CASCADE, related_name='residual_risk')

class EventCategory(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_category_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_category_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='eventcategory_organization')
    active = models.BooleanField(default=True)
    event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventcategory')

class EventNature(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventnature_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventnature_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='eventnature_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventnature')

class EventCalculator(models.Model):
    id = models.AutoField(primary_key=True)
    likelihood = models.IntegerField()
    impact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventcalculator_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventcalculator_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='eventcalculator_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventcalculator')
    active = models.BooleanField(default=True)

class EventCause(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventcause_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventcause_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='eventcause_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventcause')
    active = models.BooleanField(default=True)

class EventConsequence(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventconsequence_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventconsequence_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='eventconsequence_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventconsequence')
    active = models.BooleanField(default=True)

class Control(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='control_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='control_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='control_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventcontrol')
    active = models.BooleanField(default=True)

class Response(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='response_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='response_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='response_organization')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='eventresponse')

class ControlDesign(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='controldesign_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='controldesign_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='controldesign_organization')
    risk_control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='controldesign')
    active = models.BooleanField(default=True)

class ControlOperation(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='controloperation_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='controloperation_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='controloperation_organization')
    risk_control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='controloperation')
    active = models.BooleanField(default=True)

class ActionType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actiontype_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actiontype_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='actiontype_organization')

class ActionObjective(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actionobjective_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actionobjective_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='actionobjective_organization')

class ActionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    implementation_description = models.TextField()
    intervening_actors = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actionplan_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actionplan_updated_by', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='actionplan_organization')
    responsible_sector = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='actionplan_responsible_sector')
    responsible_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actionplan_responsible_user')
    responsible_sector_description = models.TextField(null=True, blank=True)
    responsible_user_description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
