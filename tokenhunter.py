#!/usr/bin/env python3

import requests as reqs
import json
from dotenv import load_dotenv
import os
import sys, getopt

load_dotenv()

whitelist = json.loads(os.getenv('WHITELIST'))

URL = os.getenv('URL')

headers = {
    "PRIVATE-TOKEN": os.getenv('PRIVATE-TOKEN'),
}

def test():
    if (whitelist.count("tokenhunter") != 0):
        print('whitelisted token name:' + ' ignored')
    else:
        print('removed token id: ')

def get_tokens():
    response = reqs.get( URL + '/api/v4/personal_access_tokens', headers=headers)
    return response.text

def remove_token(id):
    reqs.delete( URL + '/api/v4/personal_access_tokens/' + id , headers=headers)

    return 0

def prettylist() :
    response = get_tokens()
    parsed = json.loads(response)
    stop = False
    i = 0

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

def deleteAll() :
    response = get_tokens()
    parsed = json.loads(response)
    stop = False
    i = 0

    while(stop != True):
        print('---------')
        try:
            if (whitelist.count(str(parsed[i]["name"])) != 0):
                print('whitelisted token named: ' + str(parsed[i]["name"])  + ' ignored')
            else:
                remove_token(parsed[i]["id"])
                print('removed token named: ' + str(parsed[i]["name"]))
            i = i + 1
        except:
            stop = True

# def dryrun() :
#     response = get_tokens()
#     parsed = json.loads(response)
#     stop = False
#     i = 0

#     while(stop != True):
#         print('---------')
#         try:
#             if (whitelist.count(str(parsed[i]["name"])) != 0):
#                 print('whitelisted token named: ' + str(parsed[i]["name"])  + ' ignored')
#             else:
#                 print('will remove token named: ' + str(parsed[i]["name"]))
#             i = i + 1
#         except:
#             stop = True

def main(argv):
    opts, args = getopt.getopt(argv,"hd:lat",["del=","list=", "all=", "test="])
    for opt, arg in opts:
        if opt == '-h':
            print ('tokenhunter.py [option] (-a to delete all, -d for simple deletion, -l for listing)')
            sys.exit()
        elif opt in ("-d", "--del"):
            remove_token(arg)
        elif opt in ("-l", "--list"):
            prettylist()
        elif opt in ("-a", "--all"):
            deleteAll()
        elif opt in ("-t", "--test"):
            test()
if __name__ == '__main__':
    main(sys.argv[1:])