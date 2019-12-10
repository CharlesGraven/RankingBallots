
import pysmash
from pysmash.brackets import _filter_set_response
from pysmash.exceptions import ValidationError

smash = pysmash.SmashGG()

token = 'aab988cd7849411e00a887597fb816f1'


#print(smash.tournament_show_players('blast-off-6', 'melee-singles'))

#for player in players_in_tournament:
#    print(player['tag']+' was seeded ' + str(player['seed']) +' and placed '+ str(player['final_placement']))

def create_tournament(tournament_name, event):
    tourny_dictionary = {'id':tournament_name + '_' + event}

    try:
        players_in_tournament = smash.tournament_show_players(tournament_name, event)
    except:
        return print('Tournament or Event Does not exist')

    for player in players_in_tournament:
        tourny_dictionary[player['tag']]= player['seed']

    return tourny_dictionary

def get_user_dictionary():

    return
def compute_results(user_bracket, completed_bracket):
    total_difference = 0
    for i in user_bracket:
        difference = abs(user_bracket[i] - completed_bracet[i])
        total_difference+=difference
        # user_bracket = [2,3,1] completed_bracket = [1,2,3]
    return total_difference
