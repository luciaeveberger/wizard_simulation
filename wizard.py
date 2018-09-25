import numpy as np
# basic rules
number_of_cards = 100
card_max = 100
players = ["Angela", "Theresa", "Emmanuel", "Donald"]


def set_up_players(players_names):
    all_players = list()
    for player in players:
        all_players.append({"name": player, "cards": [], "bet": {"cards_bet": [], "card_history":[]},
                            "score": 0, "betting_strategy": ""})
    return all_players


def run_rounds(compiled_players, number_of_rounds):
    selected_cards = list()
    # runs the rounds from 1 - 10
    for round_ in range(1, 7):
        print("** ROUND {0} **".format(round_))

        # distributes the cards from 1 - 100 with the size round
        for contestant in compiled_players:
            selected_hand = np.random.random_integers(low=0, high=card_max, size=round_)
            contestant['cards'] = selected_hand
            selected_cards.extend(selected_hand)

        # players select their betting strategy
        simple_bettor_1 = bet_early_aggressive(all_players[0], round_)
        simple_bettor_2 = bet_early_aggressive(all_players[1], round_)
        distribution_bettor = bet_on_distribution(all_players[2], round_)

        # sorts the cards and determines the winners
        selected_cards = sorted(selected_cards)
        winning_cards = (selected_cards[len(selected_cards) - round_:len(selected_cards)])

        # the winning cards are determined
        print("___WINING CARD(S) {0}___".format(winning_cards))
        print("SIMPLE_BETTERS" + str(simple_bettor_1))
        print("SIMPLE_BETTERS" + str(simple_bettor_2))
        print("DISTRIBUTION" + str(distribution_bettor))

        # the point are scored
        sum_points(all_players, winning_cards)

        # the round is reset to the current round
        for participant in all_players:
            participant['cards'] = []
            participant['bet']['cards_bet'] = []
        selected_cards = []


def bet_early_aggressive(player, round_):
    for card in player['cards']:
        if card > 50 and round_ <= 5:
            player['bet']['cards_bet'].append(card)
        if round_ > 5 and card > 75:
            player['bet']['cards_bet'].append(card)
    return player


def bet_on_distribution(player, round_):
    for card in player['cards']:
        # expand this out a bit
        if card > (card_max - (card_max/round_)) and round_ <=5:
            player['bet']['cards_bet'].append(card)
    return player


def bet_conditional_logic(all_players, round_):
    # Montecarlo betting style
    # bet on previous outcome

    # P(E | F) = P(E∩F)P(F)
    return


def sum_points(betting_members, card_winners):

    for participant in betting_members:

        correct_bets = set(card_winners).intersection(participant['bet']['cards_bet'])
        # if they placed a correct bet(s)
        if correct_bets:
            participant['score'] = participant['score'] + len(correct_bets) + 2

        # # if they placed a bet & they were not correct
        if participant['bet']['cards_bet'] and not correct_bets:
            participant['score'] = participant['score'] - len(participant['bet']['cards_bet'])
        #
        # if not participant['bet']['cards_bet'] and not correct_bets:
        #     participant['score'] = participant['score'] + 1
        #
        # # if they did not place a bet and
        # if not participant['bet']['cards_bet'] and participant['cards'].any() in card_winners:
        #     participant['score'] = participant['score'] - 1

    return betting_members


round_count = 10
all_players = set_up_players(players)
run_rounds(all_players, round_count)


