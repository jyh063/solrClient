from flask import Flask,request,jsonify,abort

from solrclient import SolrClient
from models.product import Product


app = Flask(__name__)




@app.before_first_request
def initialize_database():
    SolrClient.initialize()


# '''
# index for test server connection
# '''
@app.route('/')
def index():
    return "search index page"


# '''
# get all documents as json list, default 10 results by solr query
# below are same
# '''
@app.route('/search/api/test/products',methods=['GET'])
def get_products_list():
    res = SolrClient.search(query='*:*')
    return jsonify({'products':res})

# '''
# search by specific name
# '''
@app.route('/search/api/test/products/name/<name>',methods=['GET'])
def search_by_name(name):
    res = SolrClient.search(query="name_s:%s" % name)
    return jsonify({'name_res':res})


# '''
# search by specific single ingredient
# '''
@app.route('/search/api/test/products/ingredient/<ingredient>',methods=['GET'])
def search_by_ingredient(ingredient):
    res = SolrClient.search(query="ingredients_ss:%s" % ingredient)
    return jsonify({'ingredient_res':res})


# '''
# search by specific brand
# '''
@app.route('/search/api/test/products/brand/<brand>',methods=['GET'])
def search_by_brand(brand):
    res = SolrClient.search(query="brand_s:%s" % brand)
    return jsonify({'brand_res':res})


# @app.route('/search/api/test/products/<query>',methods=['GET'])


# '''
# create a new index on solr receiving post method only and json file only
# '''
@app.route('/search/api/test/products',methods=['POST'])
def create_product():
    if not request.json or not 'productId_s' in request.json:
        abort(400)
    product = _create_product_from_json(request.json)
    SolrClient.add([product])

    return jsonify({'Create Product':product})

# '''
# update a document given new object already created completely
# receive json only
# '''
@app.route('/search/api/test/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    if not request.json or not 'productId_s' in request.json:
        abort(400)

    product_old = SolrClient.search(query="productId_s:%s" % product_id)
    if not product_old:
        abort(404)
    SolrClient.delete(query="productId_s:%s" % product_id)
    product_new = _create_product_from_json(request.json)
    SolrClient.add([product_new])
    return jsonify({'Old Product': product_old,'Updated Product':product_new})

# '''
# helper function creating product from request json file, receive json only
# '''
def _create_product_from_json(jsonobj):
    name_s = jsonobj.get('name_s')
    brand_s = jsonobj.get('brand_s')
    imgUrl_s = jsonobj.get('imgUrl_s')
    ingredients_ss = jsonobj.get('ingredients_ss')
    productId_s = jsonobj.get('productId_s')
    product = Product(name_s=name_s, brand_s=brand_s,
                      imgUrl_s=imgUrl_s, ingredients_ss=ingredients_ss,
                      productId_s=productId_s).json()
    return product


# '''
# Delete a product given id
# '''
@app.route('/search/api/test/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = SolrClient.search(query="productId_s:%s" % product_id)
    if len(products) == 0:
        abort(404)
    SolrClient.delete(query=product_id)
    return jsonify({'result': [True,products]})



if __name__ == '__main__':
    app.run(port=5001,debug=True)
