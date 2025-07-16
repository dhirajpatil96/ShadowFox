import pandas as pd

df = pd.read_excel("cleaned_IPL_sample_data.xlsx", engine="openpyxl")

df.columns = ['match_no', 'innings', 'team', 'player_name', 'ballcount',
              'position', 'pick', 'throw', 'runs', 'overcount', 'venue', 'stadium']

df['runs'] = pd.to_numeric(df['runs'], errors='coerce').fillna(0)

weights = {
    'CP': 2, 'GT': 3, 'C': 5, 'DC': -4,
    'ST': 5, 'RO': 6, 'MRO': -2, 'DH': 4
}

def compute_score(player_df):
    CP = (player_df['pick'] == 'Y').sum()
    GT = (player_df['throw'] == 'Y').sum()
    C = (player_df['pick'] == 'C').sum()
    DC = (player_df['pick'] == 'DC').sum()
    ST = (player_df['throw'] == 'S').sum()
    RO = (player_df['throw'] == 'RO').sum()
    MRO = (player_df['throw'] == 'MR').sum()
    DH = (player_df['throw'] == 'DH').sum()
    RS = player_df['runs'].sum()
    PS = (CP * weights['CP'] + GT * weights['GT'] + C * weights['C'] +
          DC * weights['DC'] + ST * weights['ST'] + RO * weights['RO'] +
          MRO * weights['MRO'] + DH * weights['DH'] + RS)
    return {
        'Clean Pick': CP, 'Good Throw': GT, 'Catch': C, 'Dropped Catch': DC,
        'Stumping': ST, 'Run Out': RO, 'Missed Run Out': MRO,
        'Direct Hit': DH, 'Runs Saved': RS, 'Performance Score': PS
    }

top_players = df['player_name'].dropna().unique()[:3]

results = {}
for player in top_players:
    pdata = df[df['player_name'] == player]
    results[player] = compute_score(pdata)

output_df = pd.DataFrame(results).T
output_df.index.name = "Player Name"
output_df.to_excel("fielding_performance_scores.xlsx")

print("Fielding performance analysis saved to 'fielding_performance_scores.xlsx'")
