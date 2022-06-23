from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import OrganizationSerializer, PeriodSerializer, UserRoleSerializer, \
    MacroProcessSerializer, ProcessSerializer, EventSerializer, EventCategorySerializer, EventNatureSerializer, \
        EventCauseSerializer, EventConsequenceSerializer, ControlSerializer, ActionObjectiveSerializer,\
             ActionPlanSerializer, ActionTypeSerializer, EventCalculatorSerializer, ControlDesignSerializer,\
                ControlOperationSerializer, ResponseSerializer

from .models import Organization, Period, UserRole, MacroProcess, Process, Event, EventCategory, EventNature, \
    EventCause, EventConsequence, Control, ActionObjective, ActionPlan, ActionType, EventCalculator, \
    ControlDesign, ControlOperation, Response


# Create your views here.

class OrganizationListCreateAPIView(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

class OrganizationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)

class PeriodListCreateAPIView(ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = (IsAuthenticated,)

class PeriodRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = (IsAuthenticated,)

class UserRoleListCreateAPIView(ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = (IsAuthenticated,)

class UserRoleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = (IsAuthenticated,)

class MacroProcessListCreateAPIView(ListCreateAPIView):
    queryset = MacroProcess.objects.all()
    serializer_class = MacroProcessSerializer
    permission_classes = (IsAuthenticated,)

class MacroProcessRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MacroProcess.objects.all()
    serializer_class = MacroProcessSerializer
    permission_classes = (IsAuthenticated,)

class ProcessListCreateAPIView(ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = (IsAuthenticated,)

class ProcessRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = (IsAuthenticated,)

class EventListCreateAPIView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)

class EventCategoryListCreateAPIView(ListCreateAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = (IsAuthenticated,)

class EventCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    permission_classes = (IsAuthenticated,)

class EventNatureListCreateAPIView(ListCreateAPIView):
    queryset = EventNature.objects.all()
    serializer_class = EventNatureSerializer
    permission_classes = (IsAuthenticated,)

class EventNatureRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventNature.objects.all()
    serializer_class = EventNatureSerializer
    permission_classes = (IsAuthenticated,)

class EventCauseListCreateAPIView(ListCreateAPIView):
    queryset = EventCause.objects.all()
    serializer_class = EventCauseSerializer
    permission_classes = (IsAuthenticated,)

class EventCauseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventCause.objects.all()
    serializer_class = EventCauseSerializer
    permission_classes = (IsAuthenticated,)

class EventConsequenceListCreateAPIView(ListCreateAPIView):
    queryset = EventConsequence.objects.all()
    serializer_class = EventConsequenceSerializer
    permission_classes = (IsAuthenticated,)

class EventConsequenceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventConsequence.objects.all()
    serializer_class = EventConsequenceSerializer
    permission_classes = (IsAuthenticated,)

class ControlListCreateAPIView(ListCreateAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = (IsAuthenticated,)

class ControlRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = (IsAuthenticated,)

class ActionObjectiveListCreateAPIView(ListCreateAPIView):
    queryset = ActionObjective.objects.all()
    serializer_class = ActionObjectiveSerializer
    permission_classes = (IsAuthenticated,)

class ActionObjectiveRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActionObjective.objects.all()
    serializer_class = ActionObjectiveSerializer
    permission_classes = (IsAuthenticated,)

class ActionPlanListCreateAPIView(ListCreateAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer
    permission_classes = (IsAuthenticated,)

class ActionPlanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer
    permission_classes = (IsAuthenticated,)

class ActionTypeListCreateAPIView(ListCreateAPIView):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    permission_classes = (IsAuthenticated,)

class ActionTypeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeSerializer
    permission_classes = (IsAuthenticated,)

class EventCalculatorListCreateAPIView(ListCreateAPIView):
    queryset = EventCalculator.objects.all()
    serializer_class = EventCalculatorSerializer
    permission_classes = (IsAuthenticated,)

class EventCalculatorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = EventCalculator.objects.all()
    serializer_class = EventCalculatorSerializer
    permission_classes = (IsAuthenticated,)

class ControlDesignListCreateAPIView(ListCreateAPIView):
    queryset = ControlDesign.objects.all()
    serializer_class = ControlDesignSerializer
    permission_classes = (IsAuthenticated,)

class ControlDesignRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ControlDesign.objects.all()
    serializer_class = ControlDesignSerializer
    permission_classes = (IsAuthenticated,)

class ControlOperationListCreateAPIView(ListCreateAPIView):
    queryset = ControlOperation.objects.all()
    serializer_class = ControlOperationSerializer
    permission_classes = (IsAuthenticated,)

class ControlOperationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ControlOperation.objects.all()
    serializer_class = ControlOperationSerializer
    permission_classes = (IsAuthenticated,)

class ResponseListCreateAPIView(ListCreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (IsAuthenticated,)

class ResponseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (IsAuthenticated,)

