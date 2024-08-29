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

    # search method, it will returns id's of records
    partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['email', '=', 'nizamudheenmj@gmail.com']]])

    # Delete the existing record
    models.execute_kw(db, uid, password, 'res.partner', 'unlink', [partners])

else:
    print("Authentication failed")
