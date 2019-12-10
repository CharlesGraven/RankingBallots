import random
import string
import numpy

def randomString(stringLength=12):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def create_random_keys(amount_of_keys):
    keys = []
    i = 0
    for i in range(amount_of_keys):
        keys.append(randomString())
    return keys

def create_player_dict(players):
    dict = {}
    for i in range(len(players)):
        dict[str(i)] = players[i]
    return dict

def make_new_ballot(name, amount_of_entries,amount_of_players , player_list):
    keys = create_random_keys(amount_of_entries)
    player_dict = create_player_dict(player_list)
    ranks = [0]*amount_of_players;
    document = {
        "player_count":amount_of_players,
        "name":name,
        "keys":keys,
        "players":player_dict,
        "ranks":ranks,
    }
    return document

def has_key(document, key):
    if any(key in s for s in document['keys']):
        #yes the key is in the document
        document['keys'].remove(key)
        return True
    return False

#similar to the above
#def delete_key(document, key)

#updateRanks goes into the tournaments dictionary
#and sets the players ranks based off of what the
#user enters
#Ballot_entry is the results of the ballot that a user filled out
def update_ranks(ballot_entry, dictionary):
    players = dictionary['players']
    original_player_ranks = dictionary['ranks']

    #[player_ranked_1, player_ranked_2, player_ranked_3]
    for index, player in players.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)

        for i in range(len(ballot_entry)):
            if ballot_entry[i] == player:
                original_player_ranks[int(index)] += i
    return original_player_ranks



def show_ranks(dictionary):
    ranks = dictionary['ranks']
    sorted_ranks = sorted(range(len(ranks)), key=ranks.__getitem__)
    players = []
    for i in range(len(ranks)):
        players.append(dictionary['players'][str(sorted_ranks[i])])
        print(i+1," : " + dictionary['players'][str(sorted_ranks[i])])

    return players

