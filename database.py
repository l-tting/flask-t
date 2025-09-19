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

def sales_per_day():
    cur.execute("""
    select date(sales.created_at) as date, sum(products.selling_price * sales.quantity) as
    total_sales from products inner join sales on sales.pid = products.id group by(date);
    """)
    daily_sales = cur.fetchall()
    return daily_sales


def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum((products.selling_price - products.buying_price)* sales.quantity) as 
        profit from sales join products on products.id = sales.pid group by(date);
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        select products.name as p_name, sum(sales.quantity * products.selling_price) as total_sales
        from products join sales on products.id = sales.pid group by(p_name);
    """)
    product_sales = cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
    select products.name as p_name ,sum((products.selling_price - products.buying_price) * sales.quantity) as profit from
    sales join products on sales.pid = products.id group by(p_name);
    """)
    product_profit = cur.fetchall()
    return product_profit



test1 = sales_per_day()

print(test1)

# print(test1)


# product_names = []
# sales = []
# for i in test1:
#     product_names.append(i[0])
#     sales.append(i[1])
# print(product_names)
# print(sales)








