#!/usr/bin/env python3

"""
TODO:
- nose testing someday
"""

import driver
import sys
import datetime
import copy

class Harness(object):

	def __init__(self, publisher=None):
		"""
		"""
		print(datetime.datetime.now(),' - driver_harness.__init__:')
		print('\targs:',locals())
		self._publisher = publisher
		self.driver_dict = {}
		self.meta_dict = {
			'drivers' : lambda from_,session_id,name,param: self.drivers(from_,session_id,name,param),
			'add_driver' : lambda from_,session_id,name,param: self.add_driver(from_,session_id,name,param),
			'remove_driver' : lambda from_,session_id,name,param: self.remove_driver(from_,session_id,name,param),
			'callbacks' : lambda from_,session_id,name,param: self.callbacks(from_,session_id,name,param),
			'meta_callbacks' : lambda from_,session_id,name, param: self.meta_callbacks(form_,session_id,name,param),
			'set_meta_callback' : lambda from_,session_id,name,param: self.set_meta_callback(from_,session_id,name,param),
			'add_callback' : lambda from_,session_id,name,param: self.add_callback(from_,session_id,name,param),
			'remove_callback' : lambda from_,session_id,name,param: self.remove_callback(from_,session_id,name,param),
			'flow' : lambda from_,session_id,name,param: self.flow(from_,session_id,name,param),
			'clear_queue' : lambda from_,session_id,name,param: self.clear_queue(from_,session_id,name,param),
			'connect' : lambda from_,session_id,name,param: self.connect(from_,session_id,name,param),
			'disconnect' : lambda from_,session_id,name,param: self.disconnect(from_,session_id,name,param),
			'commands' : lambda from_,session_id,name,param: self.commands(form_,session_id,name,param),
			'configs' : lambda from_,session_id,name,param: self.configs(from_,session_id,name,param),
			'set_config' : lambda from_,session_id,name,param: self.set_config(from_,session_id,name,param)
		}


	def set_publisher(self, publisher):
		"""
		"""
		print(datetime.datetime.now(),' - driver_harness.set_publisher:')
		print('\targs:',locals())
		self._publisher = publisher


	def drivers(self, from_, session_id, name, param):
		"""
		name: n/a
		param: n/a
		"""
		print(datetime.datetime.now(),'- driver_harness.drivers:')
		print('\targs:',locals())
		if name is None:
			name = 'None'
		self._publisher.publish(from_,from_,session_id,'driver',name,'drivers',list(self.driver_dict))
		return list(self.driver_dict)


	def add_driver(self, from_, session_id, name, param):
		"""
		name: name of driver to add_driver
		param: driver object
		"""
		print(datetime.datetime.now(),' - driver_harness.add_driver:')
		print('\targs:',locals())
		self.driver_dict[name] = param
		self.drivers(from_,session_id,name,param)


	def remove_driver(self, from_, session_id, name, param):
		"""
		name: name of driver to be driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.remove_driver:')
		print('\targs:',locals())
		del self.driver_dict[name]
		self.drivers(from_,session_id,name,param)



	def callbacks(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.callbacks:')
		print('\targs:',locals())
		return_dict = 
		self._publisher.publish(from_,from_,session_id,'driver',name,'callbacks',self.driver_dict[name].callbacks())
		return copy.deepcopy(self.driver_dict[name].callbacks())


	def meta_callbacks(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.meta_callbacks:')
		print('\targs:',locals())
		return_dict = self.driver_dict[name].meta_callbacks()
		self._publisher.publish(from_,from_,session_id,'driver',name,'meta_callbacks',return_dict)
		return return_dict


	def set_meta_callback(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: { meta-callback-name : meta-callback-object }
		"""
		print(datetime.datetime.now(),' - driver_harness.set_meta_callback:')
		print('\targs:',locals())
		if isinstance(param,dict):
			self.driver_dict.get(name).set_meta_callback(list(param)[0],list(param.values)[0])
		self._publisher.publish(from_,from_,session_id,'driver',name,'meta_callback',self.driver_dict.get(name).meta_callbacks())


	def add_callback(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: { callback obj: [messages list] }
		"""
		print(datetime.datetime.now(),' - driver_harness.add_callback:')
		print('\targs:',locals())
		self.driver_dict[name].add_callback(list(param)[0],list(param.values())[0])
		self._publisher.publish(from_,from_,session_id,'driver',name,'callbacks',self.driver_dict.get(name).callbacks())


	def remove_callback(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: name of callback to remove
		"""
		print(datetime.datetime.now(),' - driver_harness.remove_callback:')
		print('\targs:',locals())
		self.driver_dict[name].remove_callback(param)
		self._publisher.publish(form_,from_,session_id,'driver',name,'callbacks',self.driver_dict.get(name).callbacks())


	def flow(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.flow:')
		print('\targs:',locals())
		self._publisher.publish(from_,from_,session_id,'driver',name,'flow',self.driver_dict.get(name).flow())


	def clear_queue(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.clear_queue:')
		print('\targs:',locals())
		self.driver_dict.get(name).clear_queue()
		self.flow(name,session_id,name,None)


	def connect(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.connect:')
		print('\targs:',locals())
		print('self.driver_dict: ',self.driver_dict)
		print('self.driver_dict[',name,']: ',self.driver_dict[name])
		self.driver_dict[name].connect()	# <--- This should lead to on_connection_made callback


	def disconnect(self, from_, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.disconnect:')
		print('\targs:',locals())
		self.driver_dict.get(name).disconnect()	# <--- This should lead to on_connection_lost callback


	def commands(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.commands:')
		print('\targs:',locals())
		self._publisher.publish(from_,from_,session_id,'driver',name,'commands',self.driver_dict.get(name).commands())
		return self.driver_dict.get(name).commands()


	def meta_commands(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.meta_commands:')
		print('\targs:',locals())
		return_dict = copy.deepcopy(self.meta_dict)
		self._publisher.publish(from_,from_,session_id,'driver',name,'meta_commands',return_dict)
		return return_dict


	def configs(self, from_, session_id, name, param):
		"""
		name: name of driver
		param: n/a
		"""
		print(datetime.datetime.now(),' - driver_harness.configs:')
		print('\targs:',locals())
		return_dict = self.driver_dict.get(name).configs()
		self._publisher.publish(from_,from_,session_id,'driver',name,'configs',return_dict)
		return return_dict


	def set_config(self, from_, session_id, name, param):
		"""
		name: name
		param: { config name : config value }
		"""
		print(datetime.datetime.now(),' - driver_harness.set_config:')
		print('\targs:',locals())
		if isinstance(param,dict):
			self.driver_dict.get(name).set_config(list(param)[0],list(param.values)[0])
		return_dict = self.driver_dict.get(name).configs()
		self._publisher.publish(from_,from_,session_id,'driver',name,'configs',return_dict)
		return return_dict


	def meta_command(self, from_, session_id, data):
		"""

		data should be in the form:

		{
			'name': name,

			'message': value

		}

		where name the name of the driver or None if n/a,

		and value is one of two forms:

		1. string

		2. {command:params}
			params --> {param1:value, ... , paramN:value}


		"""
		print(datetime.datetime.now(),' - driver_harness.meta_command:')
		print('\targs:',locals())
		if isinstance(data, dict):
			name = data['name']
			value = data['message']
			if name in self.driver_dict:
				if isinstance(value, dict):
					command = list(value)[0]
					params = value[command]
					try:
						self.meta_dict[command](from_,session_id,name,params)
					except:
						self._publisher.publish(from_,from_,session_id,'driver',name,'error',sys.exc_info())
						print(datetime.datetime.now(),' - meta_command error: ',sys.exc_info())
				elif isinstance(value, str):
					command = value
					try:
						self.meta_dict[command](from_,session_id,name,None)
					except:
						self._publisher.publish(from_,from_,session_id,'driver',name,'error',sys.exc_info())
						print(datetime.datetime.now(),' - meta_command error: ',sys.exc_info())
			else:
				if isinstance(value, dict):
					command = list(value)[0]
					params = value[command]
					try:
						self.meta_dict[command](from_,session_id,None, params)
					except:
						self._publisher.publish(from_,from_,session_id,'driver',name,'error',sys.exc_info())
						print(datetime.datetime.now(),' - meta_command error, name not in drivers: ',sys.exc_info())
				elif isinstance(value, str):
					command = value
					try:
						self.meta_dict[command](from_,session_id,None,None)
					except:
						self._publisher.publish(from_,from_,session_id,'driver','None','error',sys.exc_info())
						print(datetime.datetime.now(),' - meta_command error, name not in drivers: ',sys.exc_info())


	def send_command(self, from_, session_id, data):
		"""
		data:
		{
			'name': <name-of-driver>
			'message': <string> or { message : {param:values} } <--- the part the driver cares about
		}
		"""
		print('driver_harness.send_command:')
		print('\targs:',locals())
		if isinstance(data, dict):
			name = data['name']
			value = data['message']
			if name in self.driver_dict:
				try:
					self.driver_dict[name].send_command(value)
				except:
					self._publisher.publish(self_,self_,session_id,'driver',name,'error',sys.exc_info()[0])
					print(datetime.datetime.now(),' - send_command error: '+sys.exc_info()[0])
			else:
				self._publisher.publish(self_,self_,session_id,'driver','None','error',sys.exc_info()[0])
				print(datetime.datetime.now(),' - send_command_error, name not in drivers: '+sys.exc_info()[0])















