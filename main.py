from flask import Flask , render_template, request, redirect,url_for,flash,session
from database import get_products, get_sales,insert_products,insert_sales,add_stock,get_stock,available_stock,check_user,insert_user
from flask_bcrypt import Bcrypt
from functools import wraps


#creating a Flask instance
app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'k99wnu8db3b99dndue8'

@app.route('/')
def home():
    return render_template("index.html")


def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


@app.route('/products')
@login_required
def products():
    products = get_products()
    return render_template('products.html',products = products)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name,buying_price,selling_price)
    insert_products(new_product)
    flash("Product added succesfully","success")
    return redirect(url_for('products'))
    


@app.route('/sales')
@login_required
def sales():
    sales =get_sales()
    products = get_products()
    return render_template("sales.html",sales=sales,products =products)


@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    pid = request.form['pid']
    quantity = request.form['quantity'] 
    new_sale = (pid,quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        flash("Insufficient stock",'danger')
        return redirect(url_for('sales'))
    insert_sales(new_sale)
    flash("Sale made successfully","success")
    return redirect(url_for('sales'))



@app.route('/stock')
@login_required
def stock():
    stock = get_stock()
    products = get_products()
    return render_template("stock.html",stock = stock,products=products)


@app.route('/add_stock',methods=['GET',"POST"])
def insert_stock():
    pid = request.form["pid"]
    stock_quantity = request.form["stock"]
    new_stock = (pid,stock_quantity)
    add_stock(new_stock)
    flash("Stock added successfully","success")
    return redirect(url_for('stock'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")



@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['f_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password'] 
        existing_user = check_user(email)

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            insert_user(new_user)
            flash("User registered successfully",'success')
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login","danger")
    return render_template("register.html")




@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user(email)
        if not registered_user:
            flash("user doesn't exist,please register","danger")
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                flash("Logged in","success")
                session["email"] = email
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect,try again","danger")
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect(url_for('login'))


app.run(debug= True)

