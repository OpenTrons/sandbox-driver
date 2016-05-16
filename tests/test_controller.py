#!/usr/bin/env python3

# https://medium.com/@theHQ/using-mock-and-trial-to-create-unit-tests-for-crossbar-applications-867e5b941cf2#.aru3coz3i
# http://python-mock.sourceforge.net/
# https://github.com/python/asyncio/blob/master/tests/test_base_events.py

import asyncio
import socket
import unittest
from unittest import mock

from controller.controller import Controller


class ControllerTest(unittest.TestCase):

	def get_free_address(self):
		sock = socket.socket()
		sock.bind(('127.0.0.1', 0))
		address = sock.getsockname()
		sock.close()
		return address
		

	def setUp(self):
		self.loop = asyncio.new_event_loop()
		# asyncio.set_event_loop(None)

		# self.addr = self.get_free_address()

		# self.server = self.loop.run_until_complete(
		# 	asyncio.start_server(
		# 		self.handle_client_callback,
		# 		host=self.addr[0],
		# 		port=self.addr[1],
		# 		loop=self.loop
		# 	)
		# )
		self.controller = Controller()

	def test_handshake_with_valid_msg(self):
		input_message = {'start_session' : ""}

		self.controller.publish = mock.Mock()

		self.controller._handshake(input_message)

		sessions = self.controller._sessions

		self.assertEqual(1, len(sessions.items()))
		
		session_id, sessions_obj = sessions.items()[0]

		self.assertTrue(isinstance(sessions_obj, Session))

	# def test_handshake_with_invalid_msg(self):
	# 	input_message = 'start_sessionFooBar'

	# 	self.controller.handshake(input_message)

	# 	self.assertEqual(1, length(sessions.items()))
		
	# 	session_id, sessions_obj = sessions.items()[0]

	# 	self.assertTrue(isinstance(sessions_obj, Session))
		


	def test_connect(self):
		pass


	def test_publish(self):
		pass


	def test_handshake_start_session(self):
		pass


	def test_handshake_close_session(self):
		pass




if __name__ == '__main__':
    unittest.main()
