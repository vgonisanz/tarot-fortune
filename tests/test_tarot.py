#!/usr/bin/env python

"""Tests for `tarot_fortune` package."""

import tarot_fortune

def test_package_publishes_version_info():
    """Tests that the `tarot_fortune` publishes the current version"""

    assert hasattr(tarot_fortune, '__version__')
