import pysolr

class SolrClient(object):
    URL = 'http://localhost:8983/solr/skinTest/'
    SOLR = None

    @staticmethod  # decorator
    def initialize():  # no self
        SolrClient.SOLR = pysolr.Solr(SolrClient.URL,timeout=10)  # access class/static variable

    @staticmethod  #adds list of json to solr
    def add(data):
        SolrClient.SOLR.add(data)



    @staticmethod  #search from solr query is
    def search(query,**kwargs):  # query:solr query string **kwargs field search dict
        results = SolrClient.SOLR.search(q=query,**kwargs)
        return [r for r in results]

    @staticmethod #delete items
    def delete(id=None,query=None):
        SolrClient.SOLR.delete(id=id,q=query)

    @staticmethod  # replace fields of certain single document
    def update_replace(data, fields):
        # "data" is updateed json from the original data
        # receive a "fields" list of fields needed to be change
        replace_dic = {}
        for k in fields:
            replace_dic[k] = 'set'
        SolrClient.SOLR.add([data], fieldUpdates=replace_dic)

    @staticmethod  # append values to specific fileds in specific document
    def update_add(data, addDictionary):
        # "data" is orginal data you want to expend fields to
        # receive a "fields" list of fields needed to be change
        add_dic = {}
        for k,v in addDictionary:
            add_dic[k] = {'add':v}
        SolrClient.SOLR.add([data], fieldUpdates=add_dic)


