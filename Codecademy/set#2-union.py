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
#print(recommended_songs)

#DIFERENÇA DE SETS .difference() or -
song_data_3 = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

tag_diff = set(user_liked_song['Back To Art']).difference(user_disliked_song['Retro Words'])
print(tag_diff)

recommended_songs_3 = {}
for song, tag in song_data_3.items():
  for one_tag in tag:
    if one_tag in tag_diff:
      if song not in user_disliked_song and song not in user_liked_song:
        recommended_songs_3[song] = tag
print(recommended_songs_3)

#DIFERENÇA SIMETRICA .symmetric_difference or ^
user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_song = set()
friend_song = set()

for song, tags in user_song_history.items():
  user_song.update(tags)
for song, tags in friend_song_history.items():
  friend_song.update(tags)

unique_tags = set(user_song.symmetric_difference(friend_song))
print(unique_tags)