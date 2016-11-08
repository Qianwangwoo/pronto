﻿# coding: utf-8
from __future__ import absolute_import

### DEPS
import unittest
import io
import sys
import six
import yaml
import os.path as op
import warnings
import textwrap

from .test_ontology import TestProntoOntology
from .              import utils


# Make sure we're using the local pronto library
sys.path.insert(0, op.dirname(op.dirname(op.abspath(__file__))))
import pronto


### TESTS
class TestProntoOboFoundry(TestProntoOntology):

    @classmethod
    @utils.ciskip
    def register_tests(cls):
        """Register tests for each ontology of the obofoundry"""

        foundry_url = "http://www.obofoundry.org/registry/ontologies.yml"
        foundry_rq = six.moves.urllib.request.urlopen(foundry_url)
        foundry_yaml = yaml.load(foundry_rq)

        # products = ( o['products'] for o in foundry_yaml['ontologies'] if 'products' in o )
        # for product in products:
        #     cls.add_test(product)

        for o in foundry_yaml['ontologies']:
            if 'products' in o:
                for product in o['products']:
                    cls.add_test(product)

    @classmethod
    def add_test(cls, product):
        """Add test for each product found in the obofoundry yaml file"""

                             #CRASH       #INF. WAIT
        #if product["id"] in ("chebi.obo", "dideo.owl"):
        #    return

        url, name = product["ontology_purl"], product["id"]

        def _foundry_noimports(self):
            onto = pronto.Ontology(url, False)
            self.check_ontology(onto)

        def _foundry_imports(self):
            onto = pronto.Ontology(url)
            self.check_ontology(onto)

        setattr(cls, "test_{}_foundry_noimports".format(name), _foundry_noimports)
        setattr(cls, "test_{}_foundry_imports".format(name),   _foundry_imports)

    # @classmethod
    # def setUpClass(cls):
    #     cls.register_tests()

# ### SETUP
# def setUpModule():
#     TestProntoOboFoundry.register_tests()

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    TestProntoOboFoundry.register_tests()
    suite.addTests(loader.loadTestsFromTestCase(TestProntoOboFoundry))
    return suite

