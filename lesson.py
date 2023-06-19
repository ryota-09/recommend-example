import numpy as np
import pandas as pd
import ast

credits_df = pd.read_csv("./data/credits.csv")
movies_df = pd.read_csv("./data/movies.csv")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#print(credits_df.head()) # 頭の五行を表示する
#print(credits_df.tail()) # 後ろの五行を表示する

# titleカラムをidとして結合する。その他のカラムは足される。
movies_df = movies_df.merge(credits_df, on="title")
# 各カラムのデータ型等の情報を取得できる。
# print(movies_df.info())

# 取得したいカラムを配列で指定する。
movies_df = movies_df[["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]]

# 欠損値の合計
movies_df.isnull().sum()

movies_df.dropna(inplace=True)

# オブジェクトを取得する関数
movies_df.iloc[0].genres
# print(movies_df.iloc[0].genres)

# リテラル型をliteral_evalはpythonの構文として評価するために利用する。
def convert(object):
  L = []
  for i in ast.literal_eval(object):
    L.append(i["name"])
    return L

movies_df["genres"] = movies_df["genres"].apply(convert)
movies_df["keywords"] = movies_df["keywords"].apply(convert)

def convert3(obj):
  L = []
  counter = 0
  for i in ast.literal_eval(obj):
    if counter != 3:
      L.append(i["name"])
      counter += 1
    else: 
      break
    return L

movies_df["cast"] = movies_df["cast"].apply(convert3)

def fetch_director(obj):
  L = []
  for i in ast.literal_eval(obj):
    if i["job"] == "Director":
      L.append(i["name"])
  return L

movies_df["crew"] = movies_df["crew"].apply(fetch_director)

movies_df["overview"] = movies_df["overview"].apply(lambda x:x.split())

# trim
movies_df["genres"] = movies_df["genres"].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else x)
movies_df["keywords"] = movies_df["keywords"].apply(lambda x:[i.replace(" ", "") for i in x] if x is not None else x)
movies_df["cast"] = movies_df["cast"].apply(lambda x:[i.replace(" ", "") for i in x] if x is not None else x)
movies_df["crew"] = movies_df["crew"].apply(lambda x:[i.replace(" ", "") for i in x] if x is not None else x)

movies_df["tags"] = movies_df["overview"] + movies_df["genres"] + movies_df["keywords"] + movies_df["cast"] + movies_df["crew"]

new_df = movies_df[["movie_id", "title", "tags"]]

new_df["tags"] = new_df["tags"].apply(lambda x:" ".join(x) if isinstance(x, list) else x)

# 小文字にする
new_df["tags"] = new_df["tags"].apply(lambda x:x.lower() if isinstance(x, str) else x)




print(new_df.head())
