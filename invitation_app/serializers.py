from rest_framework import serializers
from .models import Invitation


class InvitationSerializer(serializers.ModelSerializer):
    """
    It's return serialize to invitation model fields
    """
    seconds = serializers.IntegerField(source='invitation_create_time_diff_from_now')
    creator_email = serializers.EmailField(source='creator.email')
    creator_full_name = serializers.CharField(source='creator.get_full_name')

    class Meta:
        model = Invitation
        fields = ['id', 'created_time', 'seconds', 'email', 'used', 'creator_email','creator_full_name' ]


class InvitationCreateSerializer(serializers.ModelSerializer):
    """
    it's purpose to create the invitation record.
    """
    class Meta:
        model = Invitation
        fields = ['email',]


class InvitationPatchSerializer(serializers.ModelSerializer):
    """
    It's purpose for partial update the invitation record.
    """
    class Meta:
        model = Invitation
        fields = ['email', 'used']

