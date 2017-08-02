#!/usr/bin/env python
import json
import urllib.request
import os.path

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

try:
	# タグからランダムで一つポストを取得する
	result = json.loads( opener.open(baseURL+'/posts.json?tags=ujimatsu_chiya&limit=1&random=1').read().decode('utf-8') )
	id = result[0]['id']
	print( id )
	
	# 取れた画像をダウンロード
	result = json.loads( opener.open(baseURL+'/posts/'+str(id)+'.json').read().decode('utf-8') )
	target_url = result['file_url']
	save_name = os.path.basename(target_url)
	
	# 重複ファイルチェック付き
	if os.path.isfile(save_name):
		print( save_name + ' already exists.' )
	else:
		print('=> ' + save_name )
		urllib.request.urlretrieve( baseURL+target_url, os.path.basename(target_url) )
	
except IOError as e:
	print(e)

