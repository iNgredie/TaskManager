from rest_framework import serializers

from tmapp.models import UserTask


class UserTaskSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = UserTask
        fields = '__all__'
        read_only_fields = ('history',)

    def get_history(self, obj):
        h = obj.history.all().values(
            'title',
            'description',
            'status',
            'deadline',
            'create_at',
        )[1:]
        return h
