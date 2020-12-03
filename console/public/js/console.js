$(function() {
	frappe.realtime.on('log', (data) => data.forEach(element => console.log(element)));
	frappe.realtime.on('table', (data) => data.forEach(element => console.table(element)));
	frappe.realtime.on('warn', (data) => data.forEach(element => console.warn(element)));
	frappe.realtime.on('error', (data) => data.forEach(element => console.error(element)));
	frappe.realtime.on('info', (data) => data.forEach(element => console.info(element)));
	frappe.realtime.on('group', (data) => data.forEach(element => console.group(element)));
	frappe.realtime.on('groupEnd', (data) => console.groupEnd());
	frappe.realtime.on('time', (data) => data.forEach(element => console.time(element)));
	frappe.realtime.on('timeEnd', (data) => console.timeEnd());
	frappe.realtime.on('debug', (data) => data.forEach(element => console.debug(element)));
	frappe.realtime.on('trace', (data) => data.forEach(element => console.trace(element)));
	frappe.realtime.on('count', (data) => data.forEach(element => console.count(element)));
});