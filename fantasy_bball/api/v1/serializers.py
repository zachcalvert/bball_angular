from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField

from leagues.models import League, Team
from players.models import Player


class LeagueSerializer(ModelSerializer):
	teams = ReadOnlyField(source='get_teams')

	class Meta:
		model = League
		fields = ('id', 'name', 'manager', 'is_public', 'teams')


class TeamSerializer(ModelSerializer):
	players = ReadOnlyField(source='get_players')

	class Meta:
		model = Team
		fields = ('id', 'name', 'record', 'league', 'owner', 'players')


class PlayerList(ModelSerializer):
	fgpct = SerializerMethodField('fgpctpg')
	ftpct = SerializerMethodField('ftpctpg')
	pts = SerializerMethodField('ppg')
	threesm = SerializerMethodField('threespg')
	rebs = SerializerMethodField('rpg')
	asts = SerializerMethodField('apg')
	stls = SerializerMethodField('spg')
	blks = SerializerMethodField('bpg')
	tos = SerializerMethodField('topg')

	def fgpctpg(self, obj):
			if obj.stats != {}:
				return obj.stats['averages'].get('fgpct')
			else:
				return 0.0

	def ftpctpg(self, obj):
			if obj.stats != {}:
				return obj.stats['averages'].get('ftpct')
			else:
				return 0.0

	def ppg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('pts')
		else:
			return 0.0

	def threespg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('threesm')
		else:
			return 0.0

	def rpg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('rebs')
		else:
			return 0.0

	def apg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('asts')
		else:
			return 0.0

	def spg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('stls')
		else:
			return 0.0

	def bpg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('blks')
		else:
			return 0.0

	def topg(self, obj):
		if obj.stats != {}:
			return obj.stats['averages'].get('tos')
		else:
			return 0.0

	class Meta:
		model = Player
		fields = ('id', 'short_name', 'recent_form', 'fgpct', 'ftpct', 'pts', 'threesm', 'rebs', 'asts', 'stls', 'blks', 'tos')


class PlayerDetail(ModelSerializer):

	class Meta:
		model = Player
		fields = ('id', 'name', 'image_url', 'position', 'nba_team', 'notes', 'stats', 'recent_games')

		