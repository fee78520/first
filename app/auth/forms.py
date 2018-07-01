#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住密码')
    submit = SubmitField(u'登录')

class RegistrationForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64), Email()])
    username = StringField(u'用户名', validators=[Required(), Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                 u'用户名必须由字母数、字数、下划线或 . 组成')])
    password = PasswordField(u'密码', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须一致')
    ])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError(u'该邮箱已被注册。')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'该用户名已被使用')

class ChangePasswordForm(Form):
    old_password = PasswordField(u'现在使用的密码', validators=[Required()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须一致')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'确定修改')

class PasswordResetRequestForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField(u'重设密码')

class PasswordResetForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'两次密码必须一致')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'确定重设')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')

class ChangeEmailForm(Form):
    email = StringField(u'新邮箱', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField(u'修改邮箱地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该邮箱已被注册')