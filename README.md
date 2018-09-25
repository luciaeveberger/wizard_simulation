# WIZARD

## Strategies:

After assessing the game, I devised the following strategies. The bettors below bet on a combination of:
1. the strength of the individual card(s): raw card value
2. the order/size (N) of the round
3. the distribution of cards for (N)
4. the patterns of others betting and history

Mentioned also are the potential downside of their strategy. * None of these strategies are optimal!

#### 1. Simple Bettor - Early and Aggressive:
This bettor bets on the strength of their hand and the order of bids.
At the early stages of the game, they bet aggressively  with a lower threshold  `card > [50]` . As the rounds progress, they up the threshold and bet less aggressively after.
This player may consistently overbid.

#### 2. Distribution Bettor - Passive:
This bettor bets more passively. If their card falls in the highest distribution of 100 with a shifting distribution per size, they will play it. Otherwise, they will not. In effect, they are more concerned with the overall score.
For example,
` n=3  y = card_max - (card_max/round_*4) `
`y = 66 `
At every round, this player bets with the probability of `p=0.25`. This better looks only at the independent probability and aims for the highest probability.
At the beginning, this player will at most gain/lost 1 during the rounds. They will bid on a larger distribution during the second portion of the game.


#### 3. Pattern Bettor
This bettor examines the patterns of the other betters and builds their betting strategy off the original bets and wins of the other players.
They will be influenced by the score and build their model on Bayesian probability.