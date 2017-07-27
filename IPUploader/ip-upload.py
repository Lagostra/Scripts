import dropbox
import urllib.request

ipv4 = urllib.request.urlopen('http://v4.ipv6-test.com/api/myip.php').read()
ipv6 = urllib.request.urlopen('http://v6.ipv6-test.com/api/myip.php').read()

with open('access_token.txt') as file:
	access_token = file.read()

dbx = dropbox.Dropbox(access_token)
dbx.files_upload(ipv4, '/ipv4.txt', dropbox.files.WriteMode.overwrite)
dbx.files_upload(ipv6, '/ipv6.txt', dropbox.files.WriteMode.overwrite)