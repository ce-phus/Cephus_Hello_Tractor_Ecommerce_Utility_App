from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]

    def get_rater(self, obj):
        # Safeguard for NoneType
        if obj.rater:
            return obj.rater.username
        return None  # Or return a default value, e.g., "Anonymous"

    def get_agent(self, obj):
        # Safeguard for NoneType
        if obj.agent and obj.agent.user:
            return obj.agent.user.username
        return None  # Or return a default value

