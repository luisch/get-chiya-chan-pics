#!/usr/bin/env python
import json
import urllib.request

print("Hello! Chiya-chan!")

userName=''
passWord=''
baseURL='https://danbooru.donmai.us'

# 認証
auth = urllib.request.HTTPPasswordMgrWithDefaultRealm()
auth.add_password(None,baseURL,userName,passWord)
auth_handler = urllib.request.HTTPBasicAuthHandler(auth)

# 接続
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener( opener )

# タグからランダムで一つポストを取得する
try:
	result = json.loads( opener.open(baseURL+'/posts.json?tags=ujimatsu_chiya&limit=1&random=1').read().decode('utf-8') )
	id = result[0]['id']
	print( id )
except IOError as e:
	print( e )


