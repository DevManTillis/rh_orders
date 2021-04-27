#!/usr/bin/env python3
import psycopg2
import sys
import boto3
import os

ENDPOINT="database-1-instance-1.c0iillcvsqfx.us-west-2.rds.amazonaws.com"
PORT="5432"
USR="RDSCreds"
REGION="us-west-2"
DBNAME="database-1"

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='RDSCreds')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=token)
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))                
                