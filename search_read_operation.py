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

    # search read, serach and read request on single request search_read
    partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id', 'name']})
    print(partner_rec)

else:
    print("Authentication failed")
