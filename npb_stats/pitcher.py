from django.http.response import HttpResponse
from django.shortcuts import render
import numpy
import pandas as pd
#import matplotlib.pylab as plt

def pitcherSearch(isFarm, teamChoice, pitcherTargetChoice, pitcherDataChoice, number, request):
    #urlをリスト形式で取得
    df_all = []
    years = range(19,9,-1)
    urls = []

    #URLを入力：2019年だけ命名規則が違う
    for year in years:
        if(year==19):
            urls.append('http://baseball-data.com/stats'+isFarm+'/pitcher-'+teamChoice+'/era-'+pitcherTargetChoice+'.html')
        else:
            urls.append('http://baseball-data.com/'+ "{0:02d}".format(year)+'/stats'+isFarm+'/pitcher-'+teamChoice+'/era-'+pitcherTargetChoice+'.html')

    #データをURLから取得
    for url in urls:
    #    print('取得URL：'+url)
        df = pd.io.html.read_html(url)
        df = df[0]
        df_all.append(df)

    #選手IDの作成
    tmp_list = []
    dic = {}
    for i in range(len(df_all)):
        tmp_list.append(df_all[i]['選手名'])
    name_list = pd.concat(tmp_list).drop_duplicates().reset_index(drop=True)["選手名"].values.tolist()
    for i,name in enumerate(name_list):
        dic[name] = i

    #選手IDの付与
    for i in range(len(df_all)):
        df_all[i].columns = df_all[i].columns.droplevel()
        df_all[i]['ID'] = -1
        for j in range(len(df_all[i])):
            df_all[i].loc[j,'ID'] = dic[df_all[i].loc[j,'選手名']]
        df_all[i].index = df_all[i]['ID']
        df_all[i] = df_all[i].drop('ID',axis=1)

    #index被りを除去
    for i in range(len(df_all)):
        doubled_index = []
        count = df_all[i].index.value_counts()
        for j in count.index:
            if(count.loc[j]>1):
                doubled_index.append(j)
        df_all[i] = df_all[i].drop(doubled_index)

    #カラム名に年を付ける
    for i in range(len(df_all)):
        df_name = df_all[i].columns + "20" + "{0:02d}".format(years[i])
        df_all[i].columns = df_name

    df_m = pd.concat(df_all,axis=1)

    #結果作成
    data_col = ['選手名2019']
    for col in df_m.columns:
        if pitcherDataChoice in col:
            data_col.append(col)
    df_m = df_m.sort_values(pitcherDataChoice+'2019',ascending=False)
    df_m = df_m[data_col]
    result = df_m.head(int(number)).to_html()
    return result
