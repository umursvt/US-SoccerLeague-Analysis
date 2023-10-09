import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot



# Read file
df = pd.read_csv('mls-salaries-2017.csv')
df.copy

# find the sum of empty cells for columns
empty = df.isna().sum()

clubs = df['club'].unique()

club_player_counts=[]




# Calculate player positions and numbers for each club and add them to a DataFrame
for club in clubs:
    positions = df[df['club'] == club]['position']
    total_positions = positions.sum()
    positions_len = len(positions)
    club_player_counts.append({'club':club,'player count':positions_len})
club_player_counts_df = pd.DataFrame(club_player_counts)



trace = go.Bar(x=club_player_counts_df['club'],y=club_player_counts_df['player count'])
layout = go.Layout(
    title='Player Counts for Clubs',
    xaxis=dict(title='Clubs'),
    yaxis=dict(title='Player Count')
)
fig = go.Figure(data=[trace],layout=layout)
iplot(fig)

