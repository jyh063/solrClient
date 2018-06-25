


class Product(object):

    def __init__(self,name_s,brand_s,imgUrl_s,ingredients_ss,productId_s):
        self.name_s = name_s
        self.brand_s = brand_s
        self.imgUrl_s = imgUrl_s
        self.ingredients_ss = ingredients_ss
        self.productId_s = productId_s

    # def add_to_solr(self):
    #     pass
    #
    # def add_to_dynamodb(self):
    #     pass

    def json(self):
        return {
            "name_s":self.name_s,
            "brand_s":self.brand_s,
            "imgUrl_s":self.imgUrl_s,
            "ingredients_ss":self.ingredients_ss,
            "productId_s":self.productId_s
        }

    # @classmethod
    # def search_from_solr(cls,_id):
    #     pass
    #
    # def search_from_dynamodb(self):
    #     pass


