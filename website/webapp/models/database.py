from mongokit import Document, Connection
from bson import objectid
#from twisted.words.protocols.jabber.jid import prep

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_NAME = 'dev'

connection = Connection(MONGODB_HOST, MONGODB_PORT)


def populateDoc(document, vals):
    '''populate the fields of a document with vals. Precondition: vals in the same order as fields'''
    #unique = 'username'
    #if 'name' in vals:
    #    unique = 'name'
    #existing = document.find_one({unique : vals[unique]})
    #if existing is None:
    doc = document()
    for each in vals:
        doc[each] = vals[each]
    doc.save()

@connection.register
class Tag(Document):
    __collection__ = 'tags'
    __database__ = 'dev'
    structure = {
	'name' : basestring,
	'desc' : basestring,
    }
    use_dot_notation = True
    required_fields = ['name']

@connection.register
class Ingredient(Document):
    __collection__ = 'ingredients'
    __database__ = 'dev'
    structure = {
	'name' : basestring,
	'desc' : basestring,
	'tags' : [objectid.ObjectId],
	'nutrition' : {
            'cal' : int,
            'fatsat' : int,
            'fatpoly' : int,
            'fatmono' : int,
            'chol' : int,
	    'sodium' : int,
            'pot' : int,
            'carbof' : int,
            'carbos' : int,
            'iron' : int,
            'mag' : int,
            'va' : int,
            'vb6' : int,
            'vb12' : int,
	    'vc' : int,
            'vd' : int
            },
	'alter' : [objectid.ObjectId]
    }
    required_fields = ['name']
    use_dot_notation = True

@connection.register
class Meal(Document):
    __collection__ = 'meals'
    __database__ = 'dev'
    structure = {
        'name': basestring,
        'desc': basestring,
        'ingredients': [objectid.ObjectId],
        'amounts':[int],
        'tags': [objectid.ObjectId],
        'instructions' : basestring,
        'alter' : [objectid.ObjectId],
        'image' : [basestring],
        'likedby' : int,
        'time' : { 'total': int,
                   'prep' : int,
                   'cook' : int 
            }
    }
    required_fields = ['name', 'ingredients']
    use_dot_notation = True
    default_values = {
        'likedby' : 0
        }

@connection.register
class User(Document):
    __collection__ = 'users'
    __database__ = 'dev'
    structure = {
        'username': basestring,
        'password': basestring,
        'display': basestring,
        'email': basestring,
        'favourites' : [objectid.ObjectId],
        'ingloves' : [objectid.ObjectId],
        'inghates' : [objectid.ObjectId],
        'tags' : [objectid.ObjectId]
    }
    required_fields = ['username', 'password', 'email','display']
    use_dot_notation = True
    default_values = {
        'tags' : [],
        'ingloves' : [],
        'inghates' : [],
        'favourites' : []
        }
