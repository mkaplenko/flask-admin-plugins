# -*- coding: utf-8 -*-
__author__ = 'mkaplenko'
from flask.ext.sqlalchemy import SQLAlchemy
from flask import current_app, render_template, Markup
from sqlalchemy.ext.declarative import AbstractConcreteBase
from aspo.init import db
from sqlalchemy import func


db = SQLAlchemy(current_app) if 'sqlalchemy' not in current_app.extensions.keys() else current_app.extensions.get('sqlalchemy').db


class BasePluginModel(AbstractConcreteBase, db.Model):
    id = db.Column('id', db.Integer(), primary_key=True)
    name = db.Column('name', db.String(), nullable=False)
    position = db.Column(db.Integer(), default=1)

    def set_increment_position(self):
        max_position_value = db.session.query(func.max(BasePluginModel.position)).one()[0]
        return max_position_value + 1

    @property
    def plugin_type(self):
        return self.__mapper_args__['polymorphic_identity']

    @classmethod
    def init_plugin_choices(cls, form, pool):
        form.plugin_type.choices = [(k, pool.plugins[k].__plugin_name__) for k in pool.plugins]

        print form.plugin_type.choices

    def admin_render(self):
        return Markup(render_template(self.admin_template, form=self.__admin_form__, plugin=self))

    def render(self, last):
        wrapper = 'screens/wrappers/ordinal.html' if not last else 'screens/wrappers/last.html'
        return Markup(render_template(self.frontend_template, plugin=self, wrapper=wrapper))