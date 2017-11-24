# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.tiles.maps.testing import COLLECTIVE_TILES_MAPS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.tiles.maps is properly installed."""

    layer = COLLECTIVE_TILES_MAPS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.tiles.maps is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.tiles.maps'))

    def test_browserlayer(self):
        """Test that ICollectiveTilesMapsLayer is registered."""
        from collective.tiles.maps.interfaces import (
            ICollectiveTilesMapsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveTilesMapsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_TILES_MAPS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.tiles.maps'])

    def test_product_uninstalled(self):
        """Test if collective.tiles.maps is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.tiles.maps'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveTilesMapsLayer is removed."""
        from collective.tiles.maps.interfaces import \
            ICollectiveTilesMapsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveTilesMapsLayer,
           utils.registered_layers())
