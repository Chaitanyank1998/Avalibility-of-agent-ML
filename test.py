# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:09:33 2020

@author: Chaitanya Kholapure
"""

from app import app
import unittest

class agent(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
