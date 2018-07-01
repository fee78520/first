#-*- coding:utf-8 -*-
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField, FileField
from wtforms.validators import DataRequired, Length, Email, Regexp, Required
from ..models import Role, User
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField


class NameForm(Form):
    name = StringField(u'你的名字是什么?', validators=[Required(), Length(1, 64)])
    submit = SubmitField(u'提交')


class EditProfileForm(Form):
    name = StringField(u'真实姓名', validators=[Length(0,64)])
    location = StringField(u'地址', validators=[Length(0,64)])
    about_me = TextAreaField(u'关于我')
    image = FileField(u'头像')
    submit = SubmitField(u'提交')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1.64), Email()])
    username = StringField('Uaernam', validators=[Required(), Length(1.64), Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$', 0,
                                                                                   u'用户名必须由字母数、字数、下划线或 . 组成')])
    confirmed = BooleanField('Comfirmed')
    role = SelectField('Role', coerce=int)
    name = StringField(u'真实姓名', validators=[Length(1,64)])
    location = StringField(u'地址', validators=[Length(1,64)])
    about_me = TextAreaField(u'关于我')
    submit = SubmitField(u'提交')
    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError(u'该用户名已被使用！')


class PostForm(Form):
    body = TextAreaField(u'正文', validators=[DataRequired(u'内容不能为空！')])
    # body_html = TextAreaField("What's on your mind?", validators=[Required()])
    # body = PageDownField(u"文章", validators=[Required()])
    submit = SubmitField(u'提交')


class CommentForm(FlaskForm):
    body = StringField(u'写评论', validators=[DataRequired()])
    submit = SubmitField(u'提交')





