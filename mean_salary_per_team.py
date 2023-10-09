import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot
# Read file
df = pd.read_csv('mls-salaries-2017.csv')
df.copy




# player counts of each team

clubs = df['club'].unique()

mean_salary_list = []

# Mean salary for each team 
for club in clubs:
    total_salary = df[df['club']==club]['base_salary'].sum()
    mean_salary_list.append(total_salary.mean())


mean_salary_df = pd.DataFrame({
    'club':clubs,
    'mean_salary':mean_salary_list
    })

total_salary_all_clubs = mean_salary_df['mean_salary'].sum()
mean_salary_df['Mean Salary (%)'] = (mean_salary_df['mean_salary']/total_salary_all_clubs) * 100



fig = go.Figure(data=[go.Pie(labels=mean_salary_df['club'], values=mean_salary_df['Mean Salary (%)'])])
fig.update_layout(title='Top 10 MLS Takımlarının Ortalama Maaş Dağılımı (%)')
iplot(fig)




