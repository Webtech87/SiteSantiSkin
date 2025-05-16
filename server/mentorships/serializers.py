from rest_framework import serializers

from mentorships.models import Mentorship, MentorshipEnrollment


class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ['id', 'title', 'mentor', 'price', 'type', 'group', 'duration']


class PaidMentorshipEnrollmentSerializer(serializers.ModelSerializer):
    mentorship = MentorshipSerializer()
    class Meta:
        model = MentorshipEnrollment
        fields = ['id', 'mentorship', 'enrolled_at', 'finish_date', 'paid']

    def create(self, validated_data):
        return MentorshipEnrollment.objects.create(**validated_data)