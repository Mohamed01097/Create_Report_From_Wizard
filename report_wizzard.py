from odoo import fields, models, api


class Wizard(models.TransientModel):
    _name = 'school.wizard'

    start_date = fields.Date(string="Start Date")
    name = fields.Char(string="Name")

    def generate_pdf_report(self):
        contract_running_emps = self.env['hr.contract'].search_read([
            ('date_start', '<=', self.start_date),
            ('state', '=', 'open'),
        ])

        data = {
            'form': self.read()[0],
            'contract_running_emps': contract_running_emps
        }
        return self.env.ref('school.hr_emp_contract_report').report_action(self, data=data)



