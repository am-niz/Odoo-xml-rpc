import xmlrpc.client


url = 'http://localhost:8069'
db = 'product_brand'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

if uid:
    print("Authentication success")
else:
    print("Authentication failed")
