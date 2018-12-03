from rest_framework import serializers
from .models import Team, Game


class TeamSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = {'id', 'team_name', 'teacher', 'game', 'is_verify'}


class GameSerializer(serializers.Serializer):
    class Meta:
        model = Game
        fields = {'id', 'headline', 'describe', 'game_type', 'game_time', 'start_enter_time', 'end_enter_time',
                  'location', 'actor', 'require_pay', 'pay_money', 'img_thumbnail', 'img_show', 'create_time'
                  }
