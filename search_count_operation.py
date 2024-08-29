import xmlrpc.client


url = 'http://localhost:8069'
db = 'product_brand'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

#authentication
uid = common.authenticate(db, username, password, {})

if uid:
    print("Authentication success")

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url)) 

    # parnter count
    partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
    print(partners_count)

else:
    print("Authentication failed")
