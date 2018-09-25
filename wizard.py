import numpy as np


def set_up_players(players_names):
    all_players = list()
    for player in PLAYERS_NAMES:
        all_players.append({"name": player, "cards": [], "bet": {"cards_bet": [], "card_history":[]},
                            "score": 0, "betting_strategy": ""})
    return all_players


def run_rounds(compiled_players, number_of_rounds):
    selected_cards = list()
    # runs the rounds from 1 - 10
    for round_ in range(1, 10):
        print("** ROUND {0} **".format(round_))
        # distributes the cards from 1 - 100 with the size round
        for contestant in compiled_players:
            selected_hand = np.random.random_integers(low=0, high=CARD_MAX, size=round_)
            contestant['cards'] = selected_hand
            selected_cards.extend(selected_hand)
        # players select their betting strategy
        simple_bettor_1 = bet_early_aggressive(all_players[0], round_)
        simple_bettor_2 = bet_early_aggressive(all_players[1], round_)
        distribution_bettor = bet_on_distribution(all_players[2], round_)
        conditional_better = bet_conditional_logic(all_players[3], round_)
        # sorts the cards and determines the winners
        selected_cards = sorted(selected_cards)
        winning_cards = (selected_cards[len(selected_cards) - round_:len(selected_cards)])
        # the winning cards are determined
        print("___WINING CARD(S) {0}___".format(winning_cards))
        print("SIMPLE_BETTERS" + str(simple_bettor_1))
        print("SIMPLE_BETTERS" + str(simple_bettor_2))
        print("DISTRIBUTION" + str(distribution_bettor))
        print("CONDITIONAL_BETTER" + str(conditional_better))

        # the point are scored
        sum_points(all_players, winning_cards)
        # the round is reset to the current round
        for participant in all_players:
            print(participant)
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
        if card > (CARD_MAX - (CARD_MAX/round_)):
            player['bet']['cards_bet'].append(card)
    return player


def bet_conditional_logic(player, round_):
    # P(E | F) = P(E∩F)P(F)
    if round_ % 4:
        for card in player['cards']:
            player['bet']['cards_bet'].append(card)
    return player


def sum_points(betting_members, card_winners):
    for participant in betting_members:
        bets = participant['bet']['cards_bet']
        non_betting = set(participant['cards']) - set(bets)
        print(non_betting)
        print(card_winners)
        correct_bets = set(card_winners).intersection(participant['bet']['cards_bet'])
        missing_bets = set(card_winners).intersection(non_betting)

        print("CORRECT_BET" + str(len(correct_bets)))
        print("INCORRECT_BET" + str(len(missing_bets)))
        # if they placed a correct bet(s)
        if correct_bets:
            participant['score'] = participant['score'] + len(correct_bets) + 2
        # # if they placed a bet & they were not correct
        if missing_bets:
            participant['score'] = participant['score'] - len(missing_bets)

    return betting_members



NUMBER_OF_CARDS = 100
CARD_MAX = 100
PLAYERS_NAMES = ["Angela", "Theresa", "Emmanuel", "Donald"]
ROUND_COUNT = 10
all_players = set_up_players(PLAYERS_NAMES)
run_rounds(all_players, ROUND_COUNT)


