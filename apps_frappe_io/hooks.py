# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "apps_frappe_io"
app_title = "Frappe Apps"
app_publisher = "Frappé Technologies"
app_description = "Apps built using Frappé Framework"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/apps_frappe_io/css/apps_frappe_io.css"
# app_include_js = "/assets/apps_frappe_io/js/apps_frappe_io.js"

# include js, css files in header of web template
# web_include_css = "/assets/apps_frappe_io/css/apps_frappe_io.css"
# web_include_js = "/assets/apps_frappe_io/js/apps_frappe_io.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "/"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

website_context = {
	"brand_html": "<img class='navbar-icon' src='/assets/frappe_theme/img/frappe-icon.svg' />Frappé Apps",
	# "top_bar_items": [
	# 	{"label": "About", "url":"https://frappe.io", "right":1}
	# ],
	"hide_login": 1,
	"include_search": 1,
	"hero": {
		"/": "templates/includes/hero.html"
	},
	"favicon": "/assets/frappe_theme/img/frappe-favicon.png",

}

website_route_rules = [
	{"from_route": "/", "to_route": "Frappe App"},
]

# automatically create page for each record of this doctype
website_generators = ["Frappe App"]

# Installation
# ------------

# before_install = "apps_frappe_io.install.before_install"
# after_install = "apps_frappe_io.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "apps_frappe_io.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"apps_frappe_io.tasks.all"
# 	],
# 	"daily": [
# 		"apps_frappe_io.tasks.daily"
# 	],
# 	"hourly": [
# 		"apps_frappe_io.tasks.hourly"
# 	],
# 	"weekly": [
# 		"apps_frappe_io.tasks.weekly"
# 	]
# 	"monthly": [
# 		"apps_frappe_io.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "apps_frappe_io.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "apps_frappe_io.event.get_events"
# }

