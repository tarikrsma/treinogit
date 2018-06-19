# -*- coding: utf-8 -*-
{
    'name': "pessoa",

    'summary': """
            Para treino
        """,

    'description': """
        Somente treino
    """,

    'author': "Bradootech",
    'website': "http://www.bradootech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project','hr_expense', 'web_enterprise',
                'purchase', 'mail','web_enterprise','web', 'br_zip',
                'website','website_form','br_base','website_studio'],

    # always loaded
    'data': [
        'data/email_template.xml',
        'data/project_data.xml',
        'data/cron_blocked_activity_grid.xml',
        'security/ir.model.access.csv',
        'security/portal_security.xml',
        'views/planejamento.xml',
        'views/task_activity_views.xml',
        'views/task.xml',
        'views/project.xml',
        'views/hr_employee.xml',
        'views/project_equipment.xml',
        'views/product_product.xml',
        'wizard/project_equipment.xml',
        'wizard/project_task_activity_wizard.xml',
        'wizard/project_task_average_wizard_view.xml',
        'wizard/project_task_alocation_warn.xml',
        'views/project_type.xml',
        'views/color_change.xml',
        'views/agropolos_website_templates.xml',
        'views/res_partner.xml',
        'views/activity_budget.xml',
        'views/activity_pdf.xml',
        'views/res_config_settings.xml',
        'views/logo.xml',
        'views/project_task_alocation_view.xml',
        'views/hr_job.xml',
        'views/hr_expenses.xml',
        'views/hr_employee.xml',
        'report/external_layout.xml',
        'report/report_activity.xml',
        'report/report_task_activity.xml',
        'report/report_task_activity_line.xml',
        'data/project_data.xml',
        'views/agropolos_portal_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",

    ],
}


