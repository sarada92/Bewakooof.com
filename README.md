# Bewakooof.com

E-commerce space for buy or sell wearable items. Visit the [website]()

## User

**Signup**

```curl
POST /api/user/
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188860239-2e2a91b7-ce3f-429f-b462-31f6729cbf85.png">

**Login**

```curl
POST /api/user/
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188861698-b21bb145-26d7-4536-af87-5a38a039a9f4.png">

**Get_Token**

```curl
POST /api/user/gettoken/
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188862067-2e124612-3b4a-475f-ba2c-edfd45be68f9.png">

**Get User Details**

```curl
GET /api/user/
Authorization: Bearer {access_token}
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188862818-3ffb8fea-e0e7-41ae-ad3b-5d7d1fe3db3c.png">

**Logout**

```curl
GET /api/user/logout/{user_uuid}/
```

<img width="1367" alt="image" src="https://user-images.githubusercontent.com/38226564/188863484-1cc09576-b34f-478b-9818-df30d32e36ce.png">

## Category

**Add Category**

```curl
POST /api/category/
Authorization: Bearer {access_token}
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188864152-755be26e-66c6-4838-b30b-c0b7001559b3.png">

**Get Category Details**

```curl
GET /api/category/
```

<img width="1365" alt="image" src="https://user-images.githubusercontent.com/38226564/188864921-5a1e70d0-ac09-4d92-ae68-ac33a7932f66.png">

**Delete Category**

```curl
DELETE /api/category/{category_id}/
Authorization: Bearer {access_token}
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188865468-9c98f331-b193-4786-8bf9-03b5f9657d43.png">

## Product

**Add Product**

```curl
POST /api/product/
Authorization: Bearer {access_token}

category: category_id
merchant: merchant_id (user_uuid)
image: file, product image
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188866847-ed2196f8-1954-49f5-9f3a-8e10f61cf534.png">

**List Products**

```curl
GET /api/product/
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188868176-7851afda-23ed-487e-bb17-2a6221ddc6b4.png">

## Order

**Add to cart**

```curl
POST /api/order/add/{user_uuid}/
Authorization: Bearer {access_token}

product: product_id
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188868557-0871b81b-2eb4-49ab-b976-f7a874873a34.png">

**Available Product quantity**

```curl
GET /api/product/2/
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/38226564/188869457-ebaae476-cba7-4727-a9e0-6606a5b6cd7f.png">

```text
Note:
* Total amount is the product of (quantity ordered * price per item)
* Product quantity availability updated automatically based on total number of order
```
