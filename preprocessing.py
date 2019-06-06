import pandas as pd
import numpy as np
from tabulate import tabulate

from sklearn.preprocessing import minmax_scale

pd.set_option('display.max_columns',15)
import sklearn.preprocessing as sk

def preprocesProcedura(file):
    data = pd.read_csv(file, sep="\t", header=None)
    data.columns = ['id', 'stimulusId', 'consistency', 'picture_sound_pos_neg', 'sound_number', 'picture_number','choose_type', 'not_processed_answer', 'answer_time', 'stimulus_time']
    answer=''
    # data.dropna()
    data = (data[['id', 'consistency', 'picture_sound_pos_neg', 'sound_number', 'picture_number', 'choose_type','not_processed_answer']].copy())
    data = data[data['consistency'] == 'inc']
    data = data[data['choose_type'] == 'emospace1']
    data = (data[['id', 'picture_sound_pos_neg', 'sound_number', 'picture_number', 'not_processed_answer']].copy())

    answer=data['not_processed_answer']
    answer_valence=[]
    answer_arousal=[]

    for i in answer:
        a=i[1:]
        a=a[:-1]
        a=a.split(', ',1)

        answer_valence.append(float(a[0]))
        answer_arousal.append(float(a[1]))


    answer_valance_scaled = minmax_scale(answer_valence, feature_range=(1,9))
    answer_arousal_scaled = minmax_scale(answer_arousal, feature_range=(1,9))

    data['answer_valence']=answer_valance_scaled
    data['answer_valence']=data['answer_valence'].astype("float")
    data['answer_arousal']=answer_arousal_scaled
    data['answer_arousal']=data['answer_arousal'].astype("float")

    pictures_data = preprocesPictures()
    sounds_data = preprocesSounds()


    # print(pictures_data)
    # print(pictures_data.dtypes)


    data = data.merge(sounds_data, on='sound_number')
    data = data.merge(pictures_data, on='picture_number')

    # data['picture_sound_pos_neg'] = data['picture_sound_pos_neg'].apply(lambda x : str(convert_to_pos_neg(x)))
    is_picture_pos = []
    is_sound_pos = []



    for i in data['picture_sound_pos_neg']:
        if i == "p+s-":
            is_picture_pos.append(1)
            is_sound_pos.append(0)
        else:
            is_picture_pos.append(0)
            is_sound_pos.append(1)

    data['is_picture_positive'] = is_picture_pos
    data['is_sound_positive'] = is_sound_pos

    data = (data[['id', 'sound_number', 'sound_valence_mean', 'sound_arousal_mean', 'is_sound_positive', 'is_sound_obscene',
                  'picture_number', 'picture_arousal_mean', 'picture_valence_mean', 'is_picture_positive', 'is_picture_obscene',
                  'not_processed_answer', 'answer_valence', 'answer_arousal']].copy())

    # print("PO JOINIE")
    print(tabulate(data, headers='keys', tablefmt='psql'))
    print(data.dtypes)

    return data


def preprocesPictures():
    data=pd.read_csv('IAPS.csv',sep=';')
    data = (data[['Description', 'IAPS', 'ValenceMean', 'ArousalMean']].copy())
    data.columns = ['is_picture_obscene', 'picture_number', 'picture_valence_mean', 'picture_arousal_mean']
    data['picture_number'] = data['picture_number'].apply(lambda x : x.replace(',', ''))
    data['picture_number'] = data['picture_number'].apply(lambda x : int(x))
    data['picture_valence_mean'] = data['picture_valence_mean'].apply(lambda x : x.replace(',', '.'))
    data['picture_arousal_mean'] = data['picture_arousal_mean'].apply(lambda x : x.replace(',', '.'))
    data['picture_valence_mean'] = data['picture_valence_mean'].apply(lambda x : float(x))
    data['picture_arousal_mean'] = data['picture_arousal_mean'].apply(lambda x : float(x))
    data['is_picture_obscene'] = data['is_picture_obscene'].apply(lambda  x : is_obscene(x))
    data['is_picture_obscene'] = data['is_picture_obscene'].astype("int")
    return data


def preprocesSounds():
    data = pd.read_csv('IADS2.csv', sep=';')
    data = (data[['Sound', 'Number', 'ValenceMean', 'ArousalMean']].copy())
    data.columns = ['is_sound_obscene', 'sound_number', 'sound_valence_mean', 'sound_arousal_mean']
    data['is_sound_obscene'] = data['is_sound_obscene'].apply(lambda  x : is_obscene(x))
    data['is_sound_obscene'] = data['is_sound_obscene'].astype("int")
    return data

def is_obscene(description):
    if description[:6] == 'Erotic' or description[0:4] == 'Nude':
        return '1'
    else:
        return '0'

def convert_to_pos_neg(pXsX):
    if pXsX == "p-s+":
        to_return = [-1,1]
        return to_return
    elif pXsX == "p+s-":
        to_return = [1,-1]
        return to_return
    else:
        return {0,2}


# print("PICTURES")
# preprocesPictures()
# print("SOUDS")
# preprocesSounds()

preprocesProcedura('procedura/1107_2019_Apr_19_0712.txt').head()
