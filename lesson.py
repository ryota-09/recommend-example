import numpy as np
import pandas as pd

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


