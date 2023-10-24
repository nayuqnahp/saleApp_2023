def load_categories():
    return [{
        "id": 1,
        "name": "mobile"
    }, {
        "id": 2,
        "name": "tablet"
    }]


def load_products(kw=None):
    products = [{
        "id": 1,
        "name": "iPhone 15",
        "price": 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2023/09/13/iphone-15-pro-natural-titanium-pure-back-iphone-15-pro-natural-titanium-pure-front-2up-screen-usen.png"
    }, {
        "id": 2,
        "name": "iPhone 14 pro max",
        "price": 20000000,
        "image": "https://shopdunk.com/images/thumbs/0007808_iphone-14-pro-max-128gb.png"
    }, {
        "id": 3,
        "name": "iPhone 14",
        "price": 20000000,
        "image": "https://cdn.hoanghamobile.com/i/preview/Uploads/2022/09/08/2222.png"
    }, {
        "id": 4,
        "name": "iPhone 13 pro",
        "price": 20000000,
        "image": "https://hoangkimmobile.com/wp-content/uploads/2021/10/iphone-13-pro-max-blue-select.png"
    }, {
        "id": 5,
        "name": "iPhone 12 pro max",
        "price": 20000000,
        "image": "https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/d/o/download_2__1_6.png"
    }, {
        "id": 6,
        "name": "iPhone 11",
        "price": 20000000,
        "image": "https://cdn2.cellphones.com.vn/x/media/catalog/product/i/p/iphone-11-pro-max-gold-select-2019_1_3.png"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
