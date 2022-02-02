# psae-partner-training-jan-2022

# REST-ful API 1

Odoo does not feature a restful API. You have a client that would like to 
interface odoo with his already-existing app. Due to their lack of knowledge of odoo functions, they 
do not want to use the XML-RPC system odoo has. 

Help them by creating the following routes:

1) GET /myApi/v1/product?name=<names seperated by commas>&ids=<ids seperated by commas>
returns an array of product.template records if their names are in "name" or their ids in "ids"

2) PUT /myApi/v1/product
payload:
```json
{
  "ids": [id1, id2, ...],
  "data": {
    "attribute1": "bla"
    ...
  }
}
```
  
passes 'data' to the write method of records with id ∈ "ids"

3) POST /myApi/v1/product
payload: 
```json
{
  "data": [{
    "attribute1": "bla"
    ...
  }]
}
```

passes 'data' to the create method of product.template

4) DELETE /myApi/v1/product
payload: 
```json
{
  "ids": [id1, id2, ...]
}
```

attepts to call "unlink" on product.template recrods with id ∈ "ids". If a product is not deletable, 
archive it.




##### (optional)

If you wanted to continue developing /myApi/v1/ to make it support the entirety of models in the 
database, it would take you a lot of work.

Create /myApi/v2/ in a way such as it works on every possible mode


Hint: Use dynamic routes /myApi/v2/<model>
