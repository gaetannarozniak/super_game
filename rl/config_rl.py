# reward(my_team) = team_reward(my_team) - sum(team_rewards(other_teams)) + PENALTY

# team_reward = GOLD_REWARD * (delta_gold + sum(delta(character.gold_cost())) + LIFE_REWARD * delta_lives

# We take as a reference that the value of a Miner is 1.0

GOLD_REWARD = 0.01
LIFE_REWARD = 10
PENALTY = -0.1