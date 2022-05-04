from importlib.resources import path
import pprint
import os
from tqdm import tqdm
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
from utils import get_average_feature

# APIの認証
with open('api_key.txt') as f:
    id, key = f.read().splitlines()
client_credentails_maneger = spotipy.oauth2.SpotifyClientCredentials(
    id, key)
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentails_maneger)
source = os.path.join("source", "regional-jp-daily-latest.csv")
top_jp_song = pd.read_csv(source, header=1)

# 列を表示
print(top_jp_song.columns)
# 要素を表示
print(top_jp_song.head(10))

song_info = pd.DataFrame()
for url in tqdm(top_jp_song["URL"]):
    df = pd.DataFrame.from_dict(spotify.audio_features(url))
    song_info = pd.concat([song_info, df])

# indexの振り直し
song_info = song_info.reset_index(drop=True)
print(song_info.head(10))
print(song_info.dtypes)

# 特徴量の平均値を取得(次元ごと)
average_feature = get_average_feature(song_info)
print(average_feature)

# アーティスト別に曲を取得する
name = 'zutomayo'
result = spotify.search(q="artist:" + name, type="artist")
pprint.pprint(result['artists'])

url = "https://api.spotify.com/v1/artists/38WbKH6oKAZskBhqDFA8Uj"

df = pd.DataFrame.from_dict(spotify.audio_features(url))
print(df)
