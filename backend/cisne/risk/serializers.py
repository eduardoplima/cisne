from rest_framework.serializers import ModelSerializer
from .models import Organization, Period, UserRole, MacroProcess,\
    Process, Event, EventCause, \
        Control, RiskResponse, EventConsequence, EventNature, ControlOperation,\
            ControlDesign, EventCategory, ActionObjective, ActionPlan, ActionType,\
                EventCalculator

class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class PeriodSerializer(ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

class UserRoleSerializer(ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class MacroProcessSerializer(ModelSerializer):
    class Meta:
        model = MacroProcess
        fields = '__all__'

class ProcessSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventCalculatorSerializer(ModelSerializer):
    class Meta:
        model = EventCalculator
        fields = '__all__'

class EventCategorySerializer(ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'

class EventNatureSerializer(ModelSerializer):
    class Meta:
        model = EventNature
        fields = '__all__'

class EventCauseSerializer(ModelSerializer):
    class Meta:
        model = EventCause
        fields = '__all__'

class EventConsequenceSerializer(ModelSerializer):
    class Meta:
        model = EventConsequence
        fields = '__all__'

class ControlSerializer(ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

class ResponseSerializer(ModelSerializer):
    class Meta:
        model = RiskResponse
        fields = '__all__'

class ControlOperationSerializer(ModelSerializer):
    class Meta:
        model = ControlOperation
        fields = '__all__'

class ControlDesignSerializer(ModelSerializer):
    class Meta:
        model = ControlDesign
        fields = '__all__'

class ActionPlanSerializer(ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = '__all__'

class ActionTypeSerializer(ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'

class ActionObjectiveSerializer(ModelSerializer):
    class Meta:
        model = ActionObjective
        fields = '__all__'

