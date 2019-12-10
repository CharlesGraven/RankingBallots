from flask import Flask, render_template, request
from forms import LoginForm
import pymongo
import Ballot_Creation

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.debug = True

client = pymongo.MongoClient("mongodb://cj:riw762Wat@db-shard-00-00-w46cp.mongodb.net:27017,db-shard-00-01-w46cp.mongodb.net:27017,db-shard-00-02-w46cp.mongodb.net:27017/test?ssl=true&replicaSet=DB-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client['test']
mycol = db['tournaments']

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        player_list = str(form.player_list.data).split(' ')

        new_tournament = Ballot_Creation.make_new_ballot(str(form.ballot_name.data), int(form.ranker_amount.data),
                                                         len(player_list), player_list)

        # TODO I'll have to run some checks right here to make sure I'm not throwing trash into the db

        mycol.insert(new_tournament)

        # TODO Run a better webpage and hopefully be able to text or email the results
        return '<h1>The ballot dictionary is {},'.format(new_tournament)
    return render_template('index.html', form=form)

@app.route('/create', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        player_list = str(form.player_list.data).split(' ')

        new_tournament = Ballot_Creation.make_new_ballot(str(form.ballot_name.data), int(form.ranker_amount.data), len(player_list), player_list)

        # TODO I'll have to run some checks right here to make sure I'm not throwing trash into the db

        mycol.insert(new_tournament)

        # TODO Run a better webpage and hopefully be able to text or email the results
        return '<h1>The ballot dictionary is {},'.format(new_tournament)
    return render_template('create.html', title='Sign In', form=form)

@app.route('/<tournament>')
def rank_players(tournament):
    myquery = {"name": tournament}
    queried_tournament = mycol.find_one(myquery)
    if queried_tournament==None:
        return 'this tournament doesnt exist'

    players = Ballot_Creation.show_ranks(queried_tournament)

    return render_template('show_ranks.html', players=players, name = tournament)



@app.route('/<tournament>/<key>', methods=['GET','POST'])
def dropdown(tournament, key):
    myquery = {"name": tournament}
    queried_tournament = mycol.find_one(myquery)

    if request.method == 'POST':

        updated_ranks = []
        for i in range(len(queried_tournament['players'])):
            updated_ranks.append(request.form[str(i)])
            print(request.form[str(i)])
        new_ranks = Ballot_Creation.update_ranks(updated_ranks, queried_tournament)
        queried_tournament['ranks'] = new_ranks
        queried_tournament['keys'].remove(key)
        mycol.update(myquery, queried_tournament)
        return str(new_ranks)
    else:
        if key in queried_tournament['keys']:
            wrong_way = queried_tournament['players']
            players = {v: k for k, v in wrong_way.items()}
            return render_template('rank.html', players=players, name=tournament)
        else:
            return '<h1>This is not a valid link'


if __name__ == "__main__":
    app.run()