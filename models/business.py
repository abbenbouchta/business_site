# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError




class SaleOrder(models.Model):
    _inherit = 'sale.order'

    business_id = fields.Char(string="N° Dossier", size=256, copy=False,index=True, readonly=False)
    site_id = fields.Text(string="Chantier", required=False)
    period = fields.Char(string="Période",copy=False)
    client_order_ref = fields.Char(string="Customer Reference",related='partner_id.code', store=True, readonly=True, copy=False)



    # @api.onchange('partner_id')
    # def onchange_customer(self):
    #     if self.partner_id.code:
    #         self.client_order_ref = self.partner_id.code


    # @api.multi
    # @api.constrains('business_id','state')
    # def _check_business_id_len(self):
    #     for res in self:
    #         if res.state=='sale' and res.business_id and  len(res.business_id)!=12 :
    #               raise ValidationError(_('Le numéro du dossier doit avoir 12 positions \n. N° dossier saisi %s') % res.business_id)



SaleOrder()

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    business_id = fields.Char(string="N° Dossier", size=256, copy=False, readonly=False)
    site_id = fields.Text(string="Chantier", required=False,copy=False)
    period = fields.Char(string="Période",copy=False)
    code_customer = fields.Char(string="Numéro client")
    ref_attachment = fields.Char(string="Attachement N°")
    nbr_exemplaire = fields.Char(string="Nombre d'exemplaire")
    name = fields.Char(string='Référence', index=True,
        readonly=False, copy=False, help='The name that will be used on account move lines')

    # @api.multi
    # @api.constrains('business_id',)
    # def _check_business_id_len(self):
    #     for res in self:
    #         if res.business_id and len(res.business_id)!=12 :
    #             raise ValidationError(_('Le numéro du dossier doit avoir 12 positions \n. N° dossier saisi %s') % res.business_id)

    @api.model
    def create(self, vals):
        if self._context.get('active_model',False)=='sale.order' :
            sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
            for order in sale_orders :
               vals['business_id']=order.business_id
               vals['site_id']=order.site_id
               vals['period']=order.period
               vals['code_customer']=order.client_order_ref
               vals['name']=""
        return super(AccountInvoice, self.with_context(mail_create_nolog=True)).create(vals)

AccountInvoice()