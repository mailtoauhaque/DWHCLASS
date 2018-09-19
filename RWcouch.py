import couchdb


user = "bdme"
password = "class"
url = 'http://' + user + ':' + password + '@127.0.0.1:5984/'
couchserver = couchdb.Server(url)



def createdbincouch(dbname):
    if dbname in couchserver:
        db = couchserver[dbname]
    else:
        db = couchserver.create(dbname)


def writeincouch(data, key, dbname):
    db = couchserver[dbname]
    doc_id, doc_rev = db.save({key: data})
    print doc_id
    print doc_rev


def readfromcouch(dbname):
    db = couchserver[dbname]
    for docid in db.view('_all_docs'):
        i = docid['id']
        data = db[i]
        print data






