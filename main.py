import random

regions = ["South", "West", "East", "Midwest"]

def predict_winner(seed_high, seed_low):
    s_h = seed_high['seed']
    s_l = seed_low['seed']
    # the higher seed (lower number seed) will have more weight than the lower seed, if they are the same seed it is a 50/50
    prob_high_wins = s_l / (s_h + s_l) if s_h != s_l else 0.5
    return seed_high if random.random() < prob_high_wins else seed_low

def simulate_round(matchups, round_name):
    # Simulates a round of the tournament.
    next_round = []
    results = []
    for i, (seed1, seed2) in enumerate(matchups):
        winner = predict_winner(seed1, seed2)
        next_round.append(winner)
        results.append(f"({seed1['seed']}) {seed1['region']} vs ({seed2['seed']}) {seed2['region']} -> Winner: ({winner['seed']}) {winner['region']}")
    print(f"\n{round_name} Results:")
    print("\n".join(results))
    return next_round

def generate_matchups(teams):
    # Generates matchups from the list of advancing teams.
    return [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]

def simulate_tournament():
    # Simulates the entire March Madness tournament.

    # Define initial bracket (order seeds based on 1st round matchup)
    seeds_init = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
    
    # Simulate each round for each region
    seeds = []
    for region in regions:
        # create the teams by region
        seeds += [{ 'seed': s, 'region': region } for s in seeds_init]

    # simulate rounds of tournament
    round_of_32 = simulate_round(generate_matchups(seeds), "Round of 64")
    sweet_16 = simulate_round(generate_matchups(round_of_32), "Round of 32")
    elite_8 = simulate_round(generate_matchups(sweet_16), "Sweet 16")
    final_4 = simulate_round(generate_matchups(elite_8), "Elite 8")
    
    championship = simulate_round(generate_matchups(final_4), "Final 4")
    champion = simulate_round(generate_matchups(championship), "Championship")[0]
    
    print(f"\nChampion: ({champion['seed']}) {champion['region']}")

# Run the tournament simulation
simulate_tournament()
