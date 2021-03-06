# -*- coding: utf-8 -*-
# Copyright (c) 2020, Aerele Technologies Private Limited and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Project(Document):
	def validate(self):
		if not self.site_serial:
			self.site_serial = ''.join(self.project_name.split())


	def after_insert(self):
		present_sites = frappe.get_list('Sites', filters={'real_estate_project': self.project_name})
		if self.enable_blocks == 1:
			for block in self.block_record:				 
				if len(present_sites) == 0:
					for site_no in range(1, block.number_of_sites + 1):
						site = frappe.new_doc('Sites')
						site.real_estate_project = self.project_name
						site.block_name = block.block_name
						site.site_name = block.block_name+'-'+str(site_no)
						site.status = 'Open'
						site.save()
		else:
			if len(present_sites) == 0:
					for site_no in range(1, self.number_of_sites + 1):
						site = frappe.new_doc('Sites')
						site.real_estate_project = self.project_name
						site.site_name = 'Site -'+str(site_no)
						site.status = 'Open'
						site.save()


