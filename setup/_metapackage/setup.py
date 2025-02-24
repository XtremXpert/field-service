import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-field-service",
    description="Meta package for oca-field-service Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_territory',
        'odoo14-addon-fieldservice',
        'odoo14-addon-fieldservice_account',
        'odoo14-addon-fieldservice_account_analytic',
        'odoo14-addon-fieldservice_account_payment',
        'odoo14-addon-fieldservice_activity',
        'odoo14-addon-fieldservice_agreement',
        'odoo14-addon-fieldservice_calendar',
        'odoo14-addon-fieldservice_crm',
        'odoo14-addon-fieldservice_delivery',
        'odoo14-addon-fieldservice_distribution',
        'odoo14-addon-fieldservice_equipment_stock',
        'odoo14-addon-fieldservice_isp_account',
        'odoo14-addon-fieldservice_isp_flow',
        'odoo14-addon-fieldservice_maintenance',
        'odoo14-addon-fieldservice_partner_multi_relation',
        'odoo14-addon-fieldservice_project',
        'odoo14-addon-fieldservice_purchase',
        'odoo14-addon-fieldservice_recurring',
        'odoo14-addon-fieldservice_repair',
        'odoo14-addon-fieldservice_route',
        'odoo14-addon-fieldservice_sale',
        'odoo14-addon-fieldservice_sale_recurring',
        'odoo14-addon-fieldservice_sale_stock',
        'odoo14-addon-fieldservice_size',
        'odoo14-addon-fieldservice_skill',
        'odoo14-addon-fieldservice_stage_server_action',
        'odoo14-addon-fieldservice_stock',
        'odoo14-addon-fieldservice_substatus',
        'odoo14-addon-fieldservice_timeline',
        'odoo14-addon-fieldservice_vehicle',
        'odoo14-addon-fieldservice_vehicle_stock',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
