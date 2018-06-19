# -*- coding: utf-8 -*-

from odoo import fields


class Pessoa(models.Model):
    _inherit = "pessoa.pessoa"

    name = fields.string('nome')
    lastname = fields.string('Sobrenome')
    age = fields.number('Idade')
    weitgh = fields.float('Peso')
    height = fields.float('Altura')

