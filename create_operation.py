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

    vals = {
        'name': 'nizam',
        'email': 'nizamudheenmj@gmail.com'
    }
    # # creating new record on 'res.parnter' model
    created_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
    print("created--------->", created_id)

else:
    print("Authentication failed")
