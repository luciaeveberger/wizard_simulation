import numpy as np

# 'global' variables for game context
NUMBER_OF_CARDS = 100
CARD_MAX = 100
PLAYERS_NAMES = ["Angela", "Theresa", "Emmanuel", "Donald"]
ROUND_COUNT = 10


def set_up_players():
    """
    initializes the dictionary of players
    """
    players = list()
    for player in PLAYERS_NAMES:
        players.append({"name": player, "cards": [], "bet": {"cards_bet": [], "card_history": []},
                        "score": 0, "prev_score": 0, "count_played": 0,
                        "change_in_score": 0, "player_strategy": ""
                        })
    return players


def deal_cards(round_count, players):
    """
    uses np module to select random set of hands by N
    :return: the selected cards & the updated player dictionary
    """
    selected_cards = list()
    for contestant in players:
        selected_hand = np.random.random_integers(low=0, high=CARD_MAX, size=round_count)
        contestant['cards'] = selected_hand
        # compiles all the cards
        selected_cards.extend(selected_hand)
    return selected_cards


def sum_points(betting_members, card_winners):
    for participant in betting_members:
        # keeps a counter of the previous score
        participant['prev_score'] = participant['score']
        bets = participant['bet']['cards_bet']

        participant['count_played'] = len(bets)
        cards = participant['cards']

        count_actual_winners = len(set(card_winners).intersection(set(cards)))
        count_predicted_winners = len(bets)

        # if they guess the exact contents
        if count_predicted_winners == count_actual_winners and bets:
            participant['score'] = participant['score'] + len(bets) + 2

        if count_predicted_winners > count_actual_winners:
            participant['score'] = participant['score'] - abs(count_actual_winners - count_predicted_winners)

        if count_predicted_winners < count_actual_winners:
            participant['score'] = participant['score'] - abs(count_actual_winners - count_predicted_winners)

        # if bet 0 and have 0
        if count_actual_winners == 0 and not bets:
            participant['score'] = participant['score'] + 2

        participant['change_in_score'] = participant['score'] - participant['prev_score']

    return betting_members


def run_rounds(compiled_players, number_of_rounds):
    """
    counts, deals the cards, sets the strategies and sums the points
    """
    for round_ in range(1, number_of_rounds + 1):
        print("** ROUND {0} **".format(round_))
        chosen_cards = deal_cards(round_, compiled_players)

        # players select their betting strategy
        bet_early_aggressive(all_players[0], round_)
        bet_on_distribution(all_players[1], round_)
        bet_early_aggressive(all_players[2], round_)
        bet_historical_pattern(all_players[3])

        # the winning cards are determined
        selected_cards = sorted(chosen_cards)
        winning_cards = (selected_cards[len(selected_cards) - round_:len(selected_cards)])
        print("___WINING CARD(S) {0}___".format(winning_cards))
        sum_points(all_players, winning_cards)

        # the round is reset to the current round
        for participant in all_players:
            print("___Participant {0}___ Bets: {1} ___ Score: {2}"
                  .format(participant['name'], participant['bet']['cards_bet'], participant['score']))

            participant['cards'] = []
            participant['bet']['cards_bet'] = []
    winner = max(all_players, key=lambda x: x['score'])
    print("**** WINNER {0} & STRATEGY {1} ****".format(winner['name'], winner['player_strategy']))


# BETTING STRATEGY METHODS [100-138]
def bet_early_aggressive(player, round_):
    """
    player bets aggressively [ any card > 50] half the game
    player reduces midway [ any card <75]
    """
    for card in player['cards']:
        if card > CARD_MAX/2 and round_ <= ROUND_COUNT/2:
            player['bet']['cards_bet'].append(card)
        if round_ > ROUND_COUNT/2 and card > CARD_MAX - CARD_MAX/4:
            player['bet']['cards_bet'].append(card)
    player["player_strategy"] = "early_aggressive"
    return player


def bet_on_distribution(player, round_):
    """
    bets on distribution of the cards and where they fall
    bets less aggressively at the beginning and more at end
    """
    for card in player['cards']:
        if card > (CARD_MAX - (CARD_MAX/round_)) and round_ <= ROUND_COUNT/2:
            player['bet']['cards_bet'].append(card)
        if card > (CARD_MAX - (round_ * 5)) and round_ > ROUND_COUNT/2:
            player['bet']['cards_bet'].append(card)
    player["player_strategy"] = "distribution_late"
    return player


def bet_historical_pattern(player):
    """
    calculates the max_played of the previous round 
    and then plays that number
    """
    max_played = max(all_players, key=lambda x: x['change_in_score'])
    top_bet = np.argpartition(player['cards'], -max_played['count_played'])[-max_played['count_played']:]
    for card in top_bet:
        player['bet']['cards_bet'].append(card)
    player["player_strategy"] = "historical_winners"
    return player




if __name__ == "__main__":
    all_players = set_up_players()
    run_rounds(all_players, ROUND_COUNT)



