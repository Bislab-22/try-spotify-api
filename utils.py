import numpy as np

# 特徴量の平均値を出力する関数
def get_average_feature(info):
    feature_type_list = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    average_feature=[]
    for i in feature_type_list:
        average_feature.append(np.average(info[i]))

    average_feature = np.array(average_feature)

    return average_feature