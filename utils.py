from tqdm import tqdm
import pandas as pd


def get_urls2feature(spotify, urls):

    song_feature = pd.DataFrame()
    for url in tqdm(urls):
        df = pd.DataFrame.from_dict(spotify.audio_features(url))
        song_feature = pd.concat([song_feature, df])
    # インデックスの割り当てとNANデータの消去
    song_feature = song_feature.reset_index(drop=True)
    song_feature = song_feature.dropna(how="all")
    song_feature = song_feature.dropna(how="all", axis=1)

    if not(song_feature.empty):
        # 不要な属性を削除
        drop_list = ["mode", "type", "id", "uri", "key", "track_href",
                     "analysis_url", "duration_ms", "time_signature"]
        song_feature = song_feature.drop(drop_list, axis=1)

        # データの成形
        # これだと取得したデータに依存しているため不適切
        # 十分な量とジャンルの楽曲があれば良いが現実的ではない
        # 正規化する場合は一般的な楽曲の最大値と最小値と平均値を調査した方がよさそう

        # song_feature = (song_feature - song_feature.min()) / \
        #     (song_feature.max() - song_feature.min())

        return song_feature
    else:
        print("not found")


if __name__ == '__main__':
    pass
