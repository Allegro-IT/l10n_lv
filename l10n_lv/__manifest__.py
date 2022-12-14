
{
    'name': "Latvia - Accounting",
    'version': '16.0.0.5',
    'description': """
        Chart of Accounts (COA) Template for Latvia's Accounting.

        This module also includes:

        * Tax groups.
        * Most common Latvian Taxes.
        * Fiscal positions.
        * Account Tags.
        * Latvian and Lithuanian banks list.
        co-author is Chick.Farm (visit for more information https://www.myacc.cloud)
    """,
    'license': 'LGPL-3',
    'author': "Allegto IT, Chick.Farm",
    'website': "https://allegro.lv",
    'category': 'Accounting/Localizations/Account Charts',
    'depends': [
        'l10n_multilang',
    ],
    'data': [
# Data for Trial balance and profit/loss report
        'data/account_account_tag_data.xml',

# Information about accounting plan
        'data/account_chart_template_data.xml',
# Accounting plan
        'data/account.account.template.csv',
        'data/account.group.template.csv',
#Jornal data
        'data/account_chart_template_setup_data.xml',
        'data/res_bank_data_lv.xml',
        'data/res_bank_data_lt.xml',
        'data/account_tax_group_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_fiscal_position_template_data.xml',
# Try Loading COA for Current Company
        'data/account_chart_template_load.xml',
    ],

    'post_init_hook': 'load_translations',
    'installable': True,
}
