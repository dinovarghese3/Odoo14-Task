# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.safe_eval import datetime


class VehicleRental(models.Model):
    _name = 'vehicle.rental'
    _description = "Vehicle for rental"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle',
                                 domain=[('state_id', '=', 3)])
    name = fields.Char(string='Name',
                       related='vehicle_id.name',
                       store=True)
    brand_id = fields.Many2one(string='Brand',
                               related='vehicle_id.brand_id', store=True)
    registration_date = fields.Date('Registration Date ', required=False,
                                    help='Date the vehicle has Register',
                                    readonly=True,
                                    related='vehicle_id.registration_date')
    model = fields.Char(string='Model')
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id)

    rent = fields.Monetary(string='Rent', track_visibility='onchange')
    state = fields.Selection(
        [('available', 'Available'), ('not_available', 'Not available'),
         ('sold', 'Sold')],
        string='State', default='available', track_visibility='onchange')
    all_request_ids = fields.One2many('vehicle.request', 'vehicle_id',
                                      string='All Requests',
                                      domain=lambda self: [
                                          ('state', '!=', 'draft')])
    rent_charges_ids = fields.One2many('rent.charges', 'vehicle_id')

    def all_rental_requests(self):
        """ Function for Smart button to return the car requests"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Requests',
            'view_mode': 'tree,form',
            'res_model': 'vehicle.request',
            'domain': [('vehicle_id', '=', self.name)],
            'context': "{'create': False}",
        }

    @api.onchange('registration_date')
    def _onchange_registration_date(self):
        """ Calculating Year from registration date """
        # print('contry', self.env.user.company_id.id)
        # print(self.registration_date)
        if self.registration_date:
            self.model = str((datetime.datetime.strptime(
                str(self.registration_date), "%Y-%m-%d")).year)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Vehicle is already exists!'),

    ]


class RentCharges(models.Model):
    _name = 'rent.charges'
    _description = 'Amount calculation based on date'
    _rec_name = 'time'
    vehicle_id = fields.Many2one('vehicle.rental', string="vehicle")

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id)
    amount = fields.Monetary(string='Amount')
    time = fields.Selection([('hour', 'Hour'), ('day', 'Day'), ('week', 'Week'),
                             ('month', 'Month')], string="Time", default='day')

    @api.constrains('time')
    def _constrains_time(self):
        #  checking the time is repeated
        for rec in self.vehicle_id.rent_charges_ids - self:
            # print(rec.time)
            if rec.time == self.time:
                print(self.time, rec.time)
                raise ValidationError(" Cannot select same type " + self.time)
        # for rec in self.filtered(
        #         lambda l: l.vehicle_id.rent_charges_ids - self and (
        #                 l.time == self.time)):
        #     raise ValidationError(" Cannot select same type ")


class RegisterDate(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Adding new field registration date to fleet module'
    registration_date = fields.Date('Registration Date ', required=False,
                                    help='Date when the vehicle has been '
                                         'Register')
