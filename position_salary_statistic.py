import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot

df = pd.read_csv('mls-salaries-2017.csv')
df.copy


df['position'] = df['position'].replace('M/F', 'M-F')
df['position'] = df['position'].replace('F/M', 'F-M')
positions = df['position'].unique()

total_salary_list =[]
for pos in positions:
    total_salary = df[df['position'] == pos]['base_salary'].sum()
    total_salary_list.append(total_salary)

pos_salary_df = pd.DataFrame({'pos':positions,'salary':total_salary_list})
pos_salary_df = pos_salary_df.sort_values(by='salary',ascending=False)
print(pos_salary_df)


# BAR CHART
bar = go.Bar(x=pos_salary_df['pos'],y=pos_salary_df['salary'])
layout = go.Layout(
    title='Total Salary of positions',
    xaxis=dict(title='Positions'),
    yaxis=dict(title='Total Salary')
)
fig = go.Figure(data=[bar],layout=layout)
iplot(fig)

# PIE CHART

pie =go.Pie(labels=pos_salary_df['pos'],values=pos_salary_df['salary'])
pie_layout = go.Layout(title='TOTAL SALARY FOR POSITIONS')
fig = go.Figure(data=[pie],layout=pie_layout)
iplot(fig)



