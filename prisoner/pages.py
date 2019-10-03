from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    timeout_seconds = 100


class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    def vars_for_template(self):
        me = self.player
        opponent = me.other_player()
        return dict(
            my_decision=me.decision,
            opponent_decision=opponent.decision,
            same_choice=me.decision == opponent.decision
        )


page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
