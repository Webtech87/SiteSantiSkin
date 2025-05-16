from rest_framework import serializers

from mentorships.models import Mentorship, MentorshipEnrollment


class MentorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ['id', 'title', 'mentor', 'price', 'type', 'group', 'duration']


class PaidMentorshipEnrollmentSerializer(serializers.ModelSerializer):
    mentorship = MentorshipSerializer(read_only=True)
    class Meta:
        model = MentorshipEnrollment
        fields = ['id', 'mentorship', 'enrolled_at', 'finish_date', 'paid']

    def create(self, validated_data):
        request = self.context.get('request')
        mentorship_id = self.context.get('view').kwargs.get('pk')  # достаём из URL

        try:
            mentorship = Mentorship.objects.get(pk=mentorship_id)
        except Mentorship.DoesNotExist:
            raise serializers.ValidationError("Mentorship not found.")

        enrollment, created = MentorshipEnrollment.objects.get_or_create(
            student=request.user,
            mentorship=mentorship,
            defaults={'paid': True}
        )

        if not created:
            raise serializers.ValidationError("You are already enrolled in this mentorship.")

        return enrollment