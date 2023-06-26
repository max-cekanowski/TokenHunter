#!/usr/bin/env python3

import requests as reqs
import json
from dotenv import load_dotenv
import os
import sys, getopt

load_dotenv()

respo = '[{"id":1,"name":"token-checker","revoked":false,"created_at":"2023-06-19T09:42:18.505Z","scopes":["api","read_api","read_user","sudo","admin_mode"],"user_id":1,"last_used_at":"2023-06-19T09:47:38.731Z","active":true,"expires_at":"2023-07-19"},{"id":1,"name":"token-checker","revoked":false,"created_at":"2023-06-19T09:42:18.505Z","scopes":["api","read_api","read_user","sudo","admin_mode"],"user_id":1,"last_used_at":"2023-06-19T09:47:38.731Z","active":true,"expires_at":"2023-07-19"}]'

URL = os.getenv('URL')

headers = {
    "PRIVATE-TOKEN": os.getenv('PRIVATE-TOKEN'),
}

def get_tokens():
    response = reqs.get( URL + '/api/v4/personal_access_tokens', headers=headers)

    print(response.status_code)
    print(response.text)

    return response

def remove_token(id):
    reqs.delete( URL + '/api/v4/personal_access_tokens/' + id , headers=headers)

    return 0

def prettylist() :
    #response = get_tokens()
    parsed = json.loads(respo)
    stop = False
    i = 0
    print('ping')
    while(stop != True):
        print('---------')
        try:
            print('id: ' + str(parsed[i]["id"]))
            print('name: ' + str(parsed[i]["name"]))
            print('revoked: ' + str(parsed[i]["revoked"]))
            print('scopes: ' + str(parsed[i]["scopes"]))
            print('creator id: ' + str(parsed[i]["user_id"]))
            print('active: ' + str(parsed[i]["active"]))
            print('lastly used: ' + str(parsed[i]["last_used_at"]))
            print('creation time: ' + str(parsed[i]["created_at"]))
            print('expiration date: ' + str(parsed[i]["expires_at"]))
            i = i + 1
        except:
            stop = True

def main(argv):
    opts, args = getopt.getopt(argv,"hd:l",["del=","list="])
    for opt, arg in opts:
        if opt == '-h':
            print ('tokenhunter.py [option] (-da to delete all, -d for simple deletion, -l for listing)')
            sys.exit()
        elif opt in ("-d", "--del"):
            remove_token(arg)
        elif opt in ("-l", "--list"):
            prettylist()

if __name__ == '__main__':
    main(sys.argv[1:])