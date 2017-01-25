# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    business_id = fields.Char(string="N° Dossier", size=12, copy=False,index=True, readonly=True,states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})

    @api.multi
    @api.constrains('business_id',)
    def _check_business_id_len(self):
        for res in self:
            if len(res.business_id)!=12 :
                  raise ValidationError(_('Le numéro du dossier doit avoir 12 positions \n. N° dossier saisi %s') % res.business_id)



SaleOrder()

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    business_id = fields.Char(string="N° Dossier", size=12, copy=False,readonly=True,states={'draft': [('readonly', False)]})

    @api.multi
    @api.constrains('business_id',)
    def _check_business_id_len(self):
        for res in self:
            if len(res.business_id)!=12 :
                raise ValidationError(_('Le numéro du dossier doit avoir 12 positions \n. N° dossier saisi %s') % res.business_id)

    def create(self, vals):
        if self._context.get('open_invoices',False) :
            sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
            for order in sale_orders :
               print "business_id",order.business_id
               vals['business_id']=order.business_id
        return  super(AccountInvoice, self.with_context(mail_create_nolog=True)).create(vals)

AccountInvoice()