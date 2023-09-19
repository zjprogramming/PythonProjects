import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))
print(ad_clicks.groupby('utm_source').user_id.count().reset_index())
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True]/ (clicks_pivot[True] + clicks_pivot[False])

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())
print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
  columns = 'experimental_group',
  index = 'is_click',
  values = 'user_id'
).reset_index())
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(a_clicks)
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True]/ (a_clicks_pivot[True] + a_clicks_pivot[False])

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True]/ (b_clicks_pivot[True] + b_clicks_pivot[False])
print(a_clicks_pivot)
print(b_clicks_pivot)