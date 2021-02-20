from HW12.product_for_retry import Product
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    t = Product.product()
    prod_str1 = t.to_xml()
    print(prod_str1)
    prod = ET.fromstring(prod_str1)
    data = {}
    for child in prod:
        data[child.tag] = child.text
    print(data)
