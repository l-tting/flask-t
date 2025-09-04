import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='6979',dbname='myduka_db') 

cur = conn.cursor()
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products = get_products()
print(type(products))


#displaying sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = get_sales()
print(sales)


#insert products
def insert_products(product_values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_values}")
    conn.commit()


products1= ('juice',150,170)
products2 = ('flour',140,180)

insert_products(products1)
insert_products(products2)


def insert_sales():
    cur.execute("insert into sales(pid,quantity)values(2,30)")
    conn.commit()

# insert_sales()




