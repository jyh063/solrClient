from models.product import Product
from solrclient import SolrClient

SolrClient.initialize()
# print(SolrClient.search(query="*:*"))
# print(SolrClient.search(query="brand_s:Acne.org"))
# print(SolrClient.search(query="Acne.org"))

# print(SolrClient.search(query="PEG-80 Sorbitan Laurate"))
# print(SolrClient.search(query="ingredients_ss:PEG-80 Sorbitan Laurate"))
# p1 = Product('nameA','brandA','a.jpg',['ingA','ingAA'],1).json()

# p2 = Product('nameB',"brandB",'a.jpg','ingB',2).json()
# p3 = Product('nameC','brandA','A.jpg',['ingAA'],3).json()
# p4 = Product('nameD','branda','a.jpg',['ingD'],4).json()
# test for update_replace
#
# """
# print(p1)
# SolrClient.add([p1])
# oriData = SolrClient.search(query='a.jpg')[0]
# print('original doc', oriData)
# oriData['brand_s'] = 'brandA_new'
# oriData['name_s'] = 'nameA_new'
# SolrClient.update_replace(oriData,['brand_s','name_s'])
# newData = SolrClient.search(query='a.jpg')[0]
# print('new data', newData)
# """test for update_add
# """
# print(p2)
# print(p3)
# print(p4)
# SolrClient.add([p1,p2,p3,p4])
# print(len(SolrClient.search(query='a.jpg')))
# SolrClient.delete(query="A.jpg")
# print(len(SolrClient.search('a.jpg')))

