from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class SearchForm(FlaskForm):
    key_word = StringField('Search Company', validators=[DataRequired(), Length(2, 10)])
    submit = SubmitField('Search')

class AddCompanyForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(1, 100)])
    company_level = StringField('Company Level', validators=[Length(0,3)])
    company_industry = StringField('Company Industry', validators=[DataRequired(), Length(1, 20)])
    company_boss = StringField('Company Boss', validators=[Length(0, 20)])
    boss_phone = StringField('Boss Phone', validators=[Length(0, 20)])
    attn = StringField('ATTN', validators=[DataRequired(), Length(0, 30)])
    attn_phone = StringField('ATTN Phone', validators=[DataRequired(), Length(0, 20)])
    company_address = StringField('Company Address', validators=[DataRequired(), Length(0, 100)])
    remark = StringField('Remark', validators=[Length(0, 200)])
    submit = SubmitField('Submit')

class AddShippingForm(FlaskForm):
    shipping_time = StringField('Shipping Time', validators=[DataRequired(), Length(0, 15)])
    model = StringField('Model', validators=[DataRequired(), Length(0, 20)])
    quantity = StringField('Quantity', validators=[DataRequired(), Length(0, 10)])
    worth = IntegerField('Worth', validators=[DataRequired(), Length(0, 20)])
    weight = StringField('Weight', validators=[DataRequired(), Length(0, 10)])
    shipping_number = StringField('Shipping Number', validators=[Length(0, 20)])
    remark = StringField('Remark', validators=[Length(0, 200)])
    company_id = IntegerField('Company_id', validators=[DataRequired(), Length(0, 10)])
    submit = SubmitField('Submit')





