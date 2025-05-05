from rest_framework import serializers
from api.models import Member, Plan


class MemberSerializer(serializers.ModelSerializer):
    active_plan = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = '__all__'
        
    def get_active_plan(self, obj):
        active_plan = obj.plan.filter(is_activate=True).first()
        if active_plan is not None:
            return active_plan.plan_type, active_plan.id
        else:
            return None


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
