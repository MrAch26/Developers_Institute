from flask import Flask, render_template, render_template_string, url_for
import json
import database

app = Flask(__name__)
# database.create_database() already created 


@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/products")
def products_page():
    data = database.load_database()


    return render_template('products.html', products=data)

@app.route("/products/<product_id>")
def products_details(product_id):
    
    final_product = None

    data = database.load_database()

    for product in data:
        if product['ProductId'] == product_id:
             final_product = product
    
    # print (final_product['ProductId'])
    

    template_file = open('templates/products_details.html', 'r').read()
    return render_template_string(template_file, product=final_product)



def main():
    app.run(debug=True)
    


if __name__ == '__main__':
    main()
    
