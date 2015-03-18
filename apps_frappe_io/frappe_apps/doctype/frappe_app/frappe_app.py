# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappé Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class FrappeApp(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/frappe_app.html",
		page_title_field = "app_name"
	)

def get_list_context(context=None):
	list_context = frappe._dict(
		page_title = _("Frappé Apps"),
		template = "templates/includes/app_list.html",
		row_template = "templates/includes/app_row.html",
		hide_filters = True,
	)

	return list_context

