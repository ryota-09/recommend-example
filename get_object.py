import boto3
import pandas as pd
from io import StringIO
import os

from dotenv import load_dotenv

load_dotenv()

# バケット名,オブジェクト名
BUCKET_NAME = os.environ['BUCKET_NAME']
OBJECT_KEY_NAME_CREDITS = os.environ["OBJECT_KEY_NAME_CREDITS"]
OBJECT_KEY_NAME_MOVIES = os.environ['OBJECT_KEY_NAME_MOVIES']

IAM_ACCESS_KEY = os.environ['IAM_ACCESS_KEY']
IAM_SECRET_KEY = os.environ['IAM_SECRET_KEY']

s3 = boto3.resource('s3')

def get_credits_csv_file():
    # オブジェクト取得
    s3 = boto3.client("s3",
                  aws_access_key_id     = IAM_ACCESS_KEY,
                  aws_secret_access_key = IAM_SECRET_KEY)
    csv_file      = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY_NAME_CREDITS)
    csv_file_body = csv_file["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(csv_file_body))
    
    return  df

def get_movies_csv_file():
    # オブジェクト取得
    s3 = boto3.client("s3",
                  aws_access_key_id     = IAM_ACCESS_KEY,
                  aws_secret_access_key = IAM_SECRET_KEY)
    csv_file      = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY_NAME_MOVIES)
    csv_file_body = csv_file["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(csv_file_body))
    
    return  df





