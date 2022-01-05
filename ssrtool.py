import requests
def getSetting():
	print ("getting setting ...")
	headers={
	"User-Agent"	:	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
	"Accept"	:	"application/json, text/javascript, */*; q=0.01",
	"Accept-Language"	:	"en-US,en;q=0.5",
	"Referer"	:	"https://www.ssrtool.com/tool/free_ssr",
	"X-Requested-With"	:	"XMLHttpRequest",
	"DNT"	:	"1",
	"Connection"	:	"keep-alive",
	"Cookie"	:	"JSESSIONID=04FB6221C237B5CCC199F6E9862A4E86",
	"TE"	:	"Trailers",
	}

	r=requests.get("https://www.ssrtool.com/tool/api/free_ssr?page=1&limit=10",headers=headers)

	config={
		'server':None,
		'server_port':None,
		'password':None,	
	}
	for con in r.json()['data']:
		if con['method']=="aes-256-cfb":
			config={
			'server':con['server'],
			'server_port':int(con['server_port']),
			'password':con['password'].encode('ascii'),	
			}
			break

	shell="sslocal.exe -s {} -p {} -k {}  -l 1081".format(config['server'],config['server_port'],config['password'])
	print (shell)
	
	return config
	
getSetting()