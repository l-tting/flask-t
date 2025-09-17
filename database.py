import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='6979',dbname='myduka_db') 
cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products


#displaying sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales


#insert products
def insert_products(product_values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_values}")
    conn.commit()


def insert_sales(sales_values):
    cur.execute(f"insert into sales(pid,quantity)values{sales_values}")
    conn.commit()


def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock


def add_stock(stock_values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{stock_values}")
    conn.commit()


def available_stock(pid):
    cur.execute(f"select sum(stock_quantity) from stock where pid = {pid}")
    total_stock = cur.fetchone()[0] or 0
    cur.execute(f"select sum(quantity) from sales where pid = {pid}")
    total_sales = cur.fetchone()[0] or 0
    return total_stock - total_sales


def insert_user(user_details):
    cur.execute(f"insert into users(full_name,email,phone_number,password)values{user_details}")
    conn.commit()


def check_user(email):
    cur.execute("select * from users where email = %s",(email,))
    user = cur.fetchone()
    return user












