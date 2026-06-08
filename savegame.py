import json

def save_game(score):

    data = {
        "score": score
    }

    with open("savegame.json","w") as file:

        json.dump(data,file)


def load_game():

    try:

        with open("savegame.json","r") as file:

            return json.load(file)

    except:

        return {"score":0}
