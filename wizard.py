import numpy as np


def set_up_players(players_names):
    players = list()
    for player in PLAYERS_NAMES:
        players.append({"name": player, "cards": [], "bet": {"cards_bet": [], "card_history": []},
                        "score": 0, "prev_score": 0, "count_played": 0, "count_of_cards_bet":0})
    return players


def run_rounds(compiled_players, number_of_rounds):
    selected_cards = list()
    for round_ in range(1, number_of_rounds + 1):
        print("** ROUND {0} **".format(round_))

        # distributes the cards from 1 - 100 with the size round
        for contestant in compiled_players:
            selected_hand = np.random.random_integers(low=0, high=CARD_MAX, size=round_)
            contestant['cards'] = selected_hand
            selected_cards.extend(selected_hand)

        # players select their betting strategy
        bet_early_aggressive(all_players[0], round_)
        bet_on_distribution(all_players[1], round_)
        bet_early_aggressive(all_players[2], round_)
        bet_conditional_logic(all_players[3], round_)

        selected_cards = sorted(selected_cards)
        winning_cards = (selected_cards[len(selected_cards) - round_:len(selected_cards)])

        # the winning cards are determined
        print("___WINING CARD(S) {0}___".format(winning_cards))
        # the point are scored
        sum_points(all_players, winning_cards)
        # the round is reset to the current round
        for participant in all_players:
            print("___Participant {0}___ Bets: {1} ___ Score: {2}"
                  .format(participant['name'], participant['bet']['cards_bet'], participant['score']))

            participant['cards'] = []
            participant['bet']['cards_bet'] = []
        selected_cards = []
    winner = max(all_players, key=lambda x: x['score'])
    print("**** WINNER {0} ****".format(winner['name']))


def bet_early_aggressive(player, round_):
    for card in player['cards']:
        if card > 50 and round_ <= 5:
            player['bet']['cards_bet'].append(card)
        if round_ > 5 and card > 75:
            player['bet']['cards_bet'].append(card)
    return player


def bet_on_distribution(player, round_):
    for card in player['cards']:
        if card > (CARD_MAX - (CARD_MAX/round_)) and round_ <= 5 :
            player['bet']['cards_bet'].append(card)
        if card > (CARD_MAX - (round_ * 5)) and round_ > 5:
            player['bet']['cards_bet'].append(card)
    return player


def bet_conditional_logic(player, round_):
    # Looks at the past winner => highest change in score with score positive
    max_played = max(all_players, key=lambda x: x['count_of_cards_bet'])
    betting_top = np.argpartition(player['cards'], -max_played['count_played'])[-max_played['count_played']:]
    for card in betting_top:
        player['bet']['cards_bet'].append(card)
    return player


def sum_points(betting_members, card_winners):
    for participant in betting_members:
        # keeps a counter of the previous score
        participant['prev_score'] = participant['score']
        bets = participant['bet']['cards_bet']
        participant['count_played'] = len(bets)
        cards = participant['cards']

        containing_cards = len(set(card_winners).intersection(set(cards)))
        count_of_bets = len(bets)

        # if they guess the exact contents
        if count_of_bets == containing_cards and bets:
            participant['score'] = participant['score'] + len(bets) + 2

        if count_of_bets > containing_cards:
            participant['score'] = participant['score'] - abs(containing_cards - count_of_bets)

        if count_of_bets < containing_cards:
            participant['score'] = participant['score'] - abs(containing_cards - count_of_bets)

        # if bet 0 and have 0
        if containing_cards == 0 and not bets:
            participant['score'] = participant['score'] + 2

        participant['count_of_cards_bet'] = participant['score'] - participant['prev_score']

    return betting_members


NUMBER_OF_CARDS = 100
CARD_MAX = 100
PLAYERS_NAMES = ["Angela", "Theresa", "Emmanuel", "Donald"]
ROUND_COUNT = 10
all_players = set_up_players(PLAYERS_NAMES)
run_rounds(all_players, ROUND_COUNT)


