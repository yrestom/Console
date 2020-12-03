# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
__version__ = '1.0.0'


# def console(*data):
# 	frappe.publish_realtime('console', data, user=frappe.session.user)

def console(*data):
	return Console(msg=data)

class Console():
	def __init__(self, msg="null"):
		self.msg = msg
	
	def log(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('log', msg, user=frappe.session.user)
	
	def warn(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('warn', msg, user=frappe.session.user)

	def table(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('table', msg, user=frappe.session.user)

	def error(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('error', msg, user=frappe.session.user)

	def info(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('info', msg, user=frappe.session.user)

	def group(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('group', msg, user=frappe.session.user)
	
	def groupEnd(self, *msg):
		frappe.publish_realtime('groupEnd', msg, user=frappe.session.user)

	def time(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('time', msg, user=frappe.session.user)
	
	def timeEnd(self, *msg):
		frappe.publish_realtime('timeEnd', msg, user=frappe.session.user)

	def debug(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('debug', msg, user=frappe.session.user)
	
	def trace(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('trace', msg, user=frappe.session.user)

	def count(self, *msg):
		if not msg:
			msg = self.msg
		frappe.publish_realtime('count', msg, user=frappe.session.user)