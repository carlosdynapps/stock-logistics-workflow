# Copyright 2016 AvanzOsc (http://www.avanzosc.es)
# Copyright 2024 Adriana Saiz <adriana.saiz@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    allow_locked = fields.Boolean(string="Allow Locked Lots/Serial Numbers")
