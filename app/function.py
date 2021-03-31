
  df = pd.read_csv(filepath, parse_dates=['release_date'])

  # dropping the name and artists column
  df = df.drop(['name','artists'])

  # set ID as the index
  df.set_index('id', inplace=True)

  # rearranging similar features to be toegther to improve readability
  df = df[['valence', 'acousticness','danceability', 'energy',
         'instrumentalness', 'liveness', 'loudness',
         'speechiness','tempo']]


  # fixing on loudness and tempo
  pd = pd.read_csv(filepath, parse_dates=['release_date'])

  #stripping artist column of: [   ]' and '
  df['artists'] = df['artists'].str.strip("[]")
  df['artists'] = df['artists'].str.strip("'")
  df['artists'] = df['artists'].str.strip("-")
  df['artists'] = df['artists'].str.lower()
  df['name'] = df['name'].str. lower()
  # str id as index
  df.set_index('id', inplace=True)
  # combined  song:name and artist
  df['name_artist'] = df['name'] + ' - ' + df['artists']

  key = df['name_artist']
  return key

def the_key(filepath):
"""
Tokes in file path for the

"""
  pd = pd.read_csv(filepath, parse_dates=['release_date'])
  #stripping artist column of: [   ]' and '
  df['artists'] = df['artists'].str.strip("[]")
  df['artists'] = df['artists'].str.strip("'")
  df['artists'] = df['artists'].str.strip("-")
  df['artists'] = df['artists'].str.lower()
  df['name'] = df['name'].str. lower()
  # str id as index
  df.set_index('id', inplace=True)
  # combined  song:name and artist
  df['name_artist'] = df['name'] + ' - ' + df['artists']

  key = df['name_artist']
  return key


