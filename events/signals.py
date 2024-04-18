from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Game, Team, Matchup, Session

@receiver(pre_save, sender=Session)
def pre_save_session(sender, instance, **kwargs):
    print(instance.status)
    if instance.status == 1:
        instance.joinable = True
    else:
        instance.joinable = False

@receiver(post_save, sender=Game)
def post_save_game(sender, created, instance, **kwargs):
    session = instance.session
    session.status = 2
    session.save()
    seq_inc = Game.objects.filter(session=session, creation_type='sequence').count()
    mod = Matchup.objects.filter(player_count=session.player_count).count()
    if mod == 0:
        mod = 1

    if (seq_inc % mod == 0):
        game_i = mod
    else:
        game_i = seq_inc % mod

    if instance.creation_type == 'sequence':
        fixture = Matchup.objects.get(player_count=session.player_count, game_index=game_i)
        roster = session.session_roster.all().order_by('roster')
        team1 = Team.objects.filter(team_players=roster[fixture.team1_player1_index -1].player).filter(team_players=roster[fixture.team1_player2_index -1].player)
        team2 = Team.objects.filter(team_players=roster[fixture.team2_player1_index -1].player).filter(team_players=roster[fixture.team2_player2_index -1].player)

        if not team1.exists():
            new_team = Team.objects.create()
            new_team.team_players.set([roster[fixture.team1_player1_index -1].player,
                                       roster[fixture.team1_player2_index -1].player])
            team1 = new_team
        else:
            team1 = team1.first()

        if not team2.exists():
            new_team2 = Team.objects.create()
            new_team2.team_players.set([roster[fixture.team2_player1_index -1].player,
                                        roster[fixture.team2_player2_index -1].player])
            team2 = new_team2
        else:
            team2 = team2.first()
        instance.team.set([team1, team2])
    else:
        pass