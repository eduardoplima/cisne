from django.contrib import admin
from django.urls import path

from .views import OrganizationListCreateAPIView, OrganizationRetrieveUpdateDestroyAPIView,\
PeriodListCreateAPIView, PeriodRetrieveUpdateDestroyAPIView, ControlOperationListCreateAPIView,\
UserRoleListCreateAPIView, UserRoleRetrieveUpdateDestroyAPIView, MacroProcessListCreateAPIView,\
MacroProcessRetrieveUpdateDestroyAPIView, ProcessListCreateAPIView, ProcessRetrieveUpdateDestroyAPIView,\
EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView,\
EventCauseListCreateAPIView, EventNatureListCreateAPIView, ControlListCreateAPIView, \
EventCategoryListCreateAPIView, ResponseListCreateAPIView, ActionPlanListCreateAPIView, ActionTypeListCreateAPIView,\
EventCalculatorListCreateAPIView, EventConsequenceListCreateAPIView, ControlDesignListCreateAPIView,\
ActionObjectiveListCreateAPIView, EventCauseRetrieveUpdateDestroyAPIView,\
EventNatureRetrieveUpdateDestroyAPIView, ControlRetrieveUpdateDestroyAPIView,\
EventCategoryRetrieveUpdateDestroyAPIView, ResponseRetrieveUpdateDestroyAPIView,\
ActionPlanRetrieveUpdateDestroyAPIView, ActionTypeRetrieveUpdateDestroyAPIView,\
EventCalculatorRetrieveUpdateDestroyAPIView, EventConsequenceRetrieveUpdateDestroyAPIView,\
ControlDesignRetrieveUpdateDestroyAPIView, ActionObjectiveRetrieveUpdateDestroyAPIView,\
ControlOperationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organization/', OrganizationListCreateAPIView.as_view()),
    path('organization/<int:pk>/', OrganizationRetrieveUpdateDestroyAPIView.as_view()),
    path('period/', PeriodListCreateAPIView.as_view()),
    path('period/<int:pk>/', PeriodRetrieveUpdateDestroyAPIView.as_view()),
    path('userrole/', UserRoleListCreateAPIView.as_view()),
    path('userrole/<int:pk>/', UserRoleRetrieveUpdateDestroyAPIView.as_view()),
    path('macroprocess/', MacroProcessListCreateAPIView.as_view()),
    path('macroprocess/<int:pk>/', MacroProcessRetrieveUpdateDestroyAPIView.as_view()),
    path('process/', ProcessListCreateAPIView.as_view()),
    path('process/<int:pk>/', ProcessRetrieveUpdateDestroyAPIView.as_view()),
    path('event/', EventListCreateAPIView.as_view()),
    path('event/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view()),
    path('eventcause/', EventCauseListCreateAPIView.as_view()),
    path('eventcause/<int:pk>/', EventCauseRetrieveUpdateDestroyAPIView.as_view()),
    path('eventnature/', EventNatureListCreateAPIView.as_view()),
    path('eventnature/<int:pk>/', EventNatureRetrieveUpdateDestroyAPIView.as_view()),
    path('control/', ControlListCreateAPIView.as_view()),
    path('control/<int:pk>/', ControlRetrieveUpdateDestroyAPIView.as_view()),
    path('eventcategory/', EventCategoryListCreateAPIView.as_view()),
    path('eventcategory/<int:pk>/', EventCategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('response/', ResponseListCreateAPIView.as_view()),
    path('response/<int:pk>/', ResponseRetrieveUpdateDestroyAPIView.as_view()),
    path('actionplan/', ActionPlanListCreateAPIView.as_view()),
    path('actionplan/<int:pk>/', ActionPlanRetrieveUpdateDestroyAPIView.as_view()),
    path('actiontype/', ActionTypeListCreateAPIView.as_view()),
    path('actiontype/<int:pk>/', ActionTypeRetrieveUpdateDestroyAPIView.as_view()),
    path('eventcalculator/', EventCalculatorListCreateAPIView.as_view()),
    path('eventcalculator/<int:pk>/', EventCalculatorRetrieveUpdateDestroyAPIView.as_view()),
    path('eventconsequence/', EventConsequenceListCreateAPIView.as_view()),
    path('eventconsequence/<int:pk>/', EventConsequenceRetrieveUpdateDestroyAPIView.as_view()),
    path('controldesign/', ControlDesignListCreateAPIView.as_view()),
    path('controldesign/<int:pk>/', ControlDesignRetrieveUpdateDestroyAPIView.as_view()),
    path('actionobjective/', ActionObjectiveListCreateAPIView.as_view()),
    path('actionobjective/<int:pk>/', ActionObjectiveRetrieveUpdateDestroyAPIView.as_view()),
    path('controloperation/', ControlOperationListCreateAPIView.as_view()),
    path('controloperation/<int:pk>/', ControlOperationRetrieveUpdateDestroyAPIView.as_view())
]
