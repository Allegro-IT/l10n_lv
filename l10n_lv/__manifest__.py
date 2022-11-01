# -*- encoding: utf-8 -*-
##############################################################################
#
#    Part of Odoo.
#    Copyright (C) 2022 Allegro IT (<https://allegro.lv/>)
#                       E-mail: <info@allegro.lv>
#                       Address: <Vienibas gatve 109 LV-1058 Riga Latvia>
#                       Phone: +371 67289467
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Latvia - Accounting",
    "version": "1.1",
    "category": "Localization",
    "summary": "Accounting configuration for Latvia",
    "description": """
Adds Chart of accounts, Chart of taxes, Fiscal positions, Banks and Partner titles.
""",
    "author": "Allegro IT",
    "website": "https://allegro.lv",
    "license": "LGPL-3",
    "images": [],
    "depends": [
        "account"
        "l10n_multilang",
    ],
    "data": [

        # Chart of Accounts
        "data/account_chart_template_data.xml",
        "data/account_account_tag_data.xml",
        "data/account.account.template.csv",
        "data/account.group.template.csv",

        #      "data/account_account_type_data.xml",
        #      "data/account_group_template_data.xml",
        #      "data/account_account_template_data.xml",

        # Taxes
        "data/account_tax_group_data.xml",
        "data/account_tax_report_data.xml",
        "data/account_tax_template_data.xml",
        "data/account_fiscal_position_template_data.xml",
        "data/account_account_template_post_data.xml",

        # Views and others
        "views/res_partner_view.xml"
        "data/update_data.xml",
        "data/res_company_data.xml",
        "data/res_partner_title_data.xml",
        "data/res.bank.csv",
        "data/account_payment_terms_data.xml",

    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "qweb": [],
}
