import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv('instagram-gitsindonesia.csv', date_parser='')

data = data.drop('Unnamed: 0', axis=1)

data['Dates'] = pd.to_datetime(data['Dates'])

tipe_infografis_januari = ['Tips', 'Edukatif', 'Edukatif', 'Fun Fact', 'Info Loker', 'Fun Fact', 
    'Pengumuman', 'Edukatif', 'Pengumuman', 'Edukatif', 'Edukatif', 'Edukatif', 'Edukatif', 'Edukatif', 
    'Edukatif', 'Tips', 'Fun Fact', 'Fun Fact', 'Tips', 'Pengumuman', 'Tips', 'Edukatif', 'Edukatif']

tipe_infografis_februari = ['Tips', 'Edukatif', 'Tips', 'Info Loker', 'Info Loker', 'Info Loker',
 'Info Loker', 'Edukatif', 'Edukatif', 'Tips', 'Edukatif', 'Edukatif',
 'Fun Fact', 'Fun Fact', 'Pengumuman', 'Pengumuman', 'Pengumuman', 'Pengumuman',
 'Fun Fact', 'Fun Fact', 'Fun Fact', 'Fun Fact', 'Edukatif', 'Edukatif',
 'Pengumuman', 'Pengumuman']

tipe_infografis_maret = ['Edukatif', 'Pengumuman', 'Pengumuman', 'Pengumuman', 'Pengumuman', 'Tips',
 'Edukatif', 'Edukatif', 'Edukatif', 'Fun Fact', 'Fun Fact', 'Fun Fact',
 'Fun Fact', 'Pengumuman', 'Pengumuman', 'Fun Fact', 'Pengumuman', 'Edukatif',
 'Pengumuman', 'Tips', 'Fun Fact', 'Edukatif', 'Edukatif', 'Tips']

tipe_infografis_april = ['Edukatif', 'Info Loker', 'Fun Fact', 'Fun Fact', 'Info Loker', 'Tips']

tipe_infografis_mei = ['Pengumuman', 'Fun Fact', 'Edukatif', 'Edukatif', 'Edukatif', 'Pengumuman',
 'Info Loker', 'Edukatif', 'Fun Fact', 'Tips', 'Fun Fact', 'Fun Fact',
 'Fun Fact', 'Tips','Tips', 'Fun Fact', 'Fun Fact']

tipe_infografis_juni = ['Fun Fact', 'Edukatif', 'Fun Fact', 'Fun Fact', 'Tips', 'Pengumuman', 'Fun Fact',
    'Pengumuman', 'Fun Fact', 'Tips', 'Fun Fact', 'Fun Fact', 'Tips', 'Edukatif', 'Fun Fact', 'Pengumuman', 
    'Fun Fact', 'Edukatif', 'Tips', 'Tips', 'Pengumuman', 'Pengumuman', 'Tips', 'Tips', 'Pengumuman', 'Tips', 'Tips']

tipeInfografis = tipe_infografis_juni + tipe_infografis_mei + tipe_infografis_april + tipe_infografis_maret + tipe_infografis_februari + tipe_infografis_januari

tipeInfografis = [tipe.title() for tipe in tipeInfografis]
data['Tipe_Infografis'] = tipeInfografis
data['Tipe_Infografis'] = data['Tipe_Infografis'].astype('category')

data['Day'] = data['Dates'].agg(lambda r: datetime.strptime(str(r), '%Y-%m-%d %H:%M:%S').strftime('%A')).astype('category')

list_month = []

for d in data['Dates']:
    list_month.append(d.strftime('%B'))

data['Month'] = list_month

index_missing_like = data[data['Likes'] < 0].index

insert_missing_like = [17, 41, 26, 18, 75, 78, 29, 48, 47, 11]

for i, index in enumerate(index_missing_like):
    data.iloc[index, 1] = insert_missing_like[i]

followers = 4400

def engagement_rate_1(likes, comments):
    """Engagement Rate = ((0.75 * Likes) + Comments) / 100"""
    result = ((0.75 * likes) + comments)
    return result

def engagement_rate_2(likes, comments, followers):
    """Engagement Rate = (Likes + Comments) / Followers * 100"""
    result = (likes + comments) / followers * 100
    return result

data['Engagement_Rate_1'] = engagement_rate_1(data['Likes'], data['Comments'])

data['Engagement_Rate_2'] = engagement_rate_2(data['Likes'], data['Comments'], followers)

data.to_csv('final-instagram-gitsindonesia.csv')