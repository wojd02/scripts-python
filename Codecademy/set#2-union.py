#UNINDO SETS .union()
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}
for key, song in song_data.items():
    set_song_data = set(song)
    set_user_tag_data = set(user_tag_data[key])
    new_song_data[key] = set_song_data.union(set_user_tag_data)

#print(new_song_data)

#INTERSEÇÃO DE SETS .intersection or &
song_data_2 = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs_2 = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

tags_int = set(user_recent_songs_2['Retro Words']).intersection(set(user_recent_songs_2['Lowkey Space']))

recommended_songs = {}
for song, tag in song_data_2.items():
  for tag_int in tag:
    if tag_int in tags_int:
      if song not in user_recent_songs_2:
        recommended_songs[song] = tag
print(recommended_songs)