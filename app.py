from flask import Flask, render_template, url_for, redirect, flash, request
from form.forms import LoginForm, SearchForm, AddCompanyForm, AddShippingForm
from database import insert_company, insert_shipping_info, session, get_fields, get_contents
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, LoginManager, login_user, login_required
import config


app = Flask(__name__)
bootstrap = Bootstrap(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'
login_manager.init_app(app)

app.secret_key = 'secret string'

class User(UserMixin):
    pass


@login_manager.user_loader
def load_user(username):
    curr_user = User()
    return curr_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form['password']
        if user_auth(username, password):
            curr_user = User()
            curr_user.id = username
            login_user(curr_user)

            return redirect(url_for('index'))
        flash('Wrong username or password!')



    return render_template('login.html', form=form)


@app.route('/')
def index():
    form = SearchForm()
    table = 'company'
    company_fields = get_fields(table)
    company_contents = get_contents(table)
    return render_template('index.html', form=form, fields=fields, contents=contents)

@app.route('/show_shipping_info/<int:company_id>')
def show_shipping_info(company_id):
    table = 'shipping_info'
    shipping_fields = get_slave_fields(table)
    shipping_contents = get_slave_contents(table, company_id)
    return render_template('show_shipping_info.html', fields=fields, contents=contents)


@login_required
@app.route('/add_company', methods=['GET', 'POST'])
def add_company():
    form = AddCompanyForm()
    if request.method == "POST":    
        data={
        'company_name': form.company_name.data,
        'company_level': form.company_level.data,
        'company_industry' : form.company_industry.data,
        'company_boss' : form.company_boss.data,
        'boss_phone' : form.boss_phone.data,
        'ATTN' : form.attn.data,
        'ATTN_phone' : form.attn_phone.data,
        'company_address' : form.company_address.data,
        'remark' : form.remark.data
        }

        insert_company(**data)
        flash("You added a company.")
        return redirect(url_for('index'))

   

    return render_template('add_company.html', form=form)

@login_required
@app.route('/add_shipping_info', methods=["GET", "POST"])
def add_shipping_info():
    form = AddShippingForm()
    if request.method == "POST":
        data={
                'company_id': form.company_id.data,
                'shipping_time': form.shipping_time.data,
                'model': form.model.data,
                'quantity': form.quantity.data,
                'worth': form.worth.data,
                'weight': form.weight.data,
                'shipping_number': form.shipping_number.data,
                }
        try:

            insert_shipping_info(**data)
            flash('You added a shipping info.')
            return redirect(url_for('index'))


        except Exception as e:
            redirect(url_for('add_shipping_info'))
            session.rollback()
        flash('You added a shipping info.')
        return redirect(url_for('index'))

    return render_template('add_shipping_info.html', form=form)



        

        

def user_auth(username, password):
    if username == config.username and password == config.password:
        return True
    else:
        return False
