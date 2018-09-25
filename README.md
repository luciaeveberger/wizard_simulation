# WIZARD

## Design


## Strategies:

#### 1. Simple Bettor - Early and Aggressive:
This bettor bets on the strength of their hand vs. the order of bids.
At the early stages of the game, they bet aggressively  with a lower threshold  card > [50] at the . As the rounds progress, they up the threshold and bet less aggressively after.
This player may consistently overbid.

#### 2. Distribution Bettor - Passive:
This bettor bets more passively. If their card falls in the highest distribution of 100 with a shifting distribution per size, they will play it. Otherwise, they will not. In effect, they are more concerned with the overall score.
For example,
` n=3  y = card_max - (card_max/round_*4) `
`y = 66 `
At every round, this player bets with the probability of `p=0.25`. This better looks only at the independent probability and aims for the highest probability.
At the beginning, this player will at most gain/lost 1 during the rounds. They will bid on a larger distribution during the second portion of the game.


#### 3. Pattern Bettor
This bettor examines the patterns of the other betters and builds their betting strategy off the others. They will be influenced by the score and build their model on Bayesian probability.