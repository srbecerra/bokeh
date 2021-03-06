#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2017, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest ; pytest

from bokeh.util.api import INTERNAL, PUBLIC ; INTERNAL, PUBLIC
from bokeh.util.testing import verify_api ; verify_api

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports
import bokeh.io.notebook as binb

# Module under test
import bokeh.io as bi

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL = (
    'curdoc',
    'export_png',
    'export_svgs',
    'install_notebook_hook',
    'push_notebook',
    'output_file',
    'output_notebook',
    'save',
    'show',
)

#-----------------------------------------------------------------------------
# Public API
#-----------------------------------------------------------------------------

def test_jupyter_notebook_hook_installed():
    assert list(binb._HOOKS) == ["jupyter"]
    assert binb._HOOKS["jupyter"]['load'] == binb.load_notebook
    assert binb._HOOKS["jupyter"]['doc']  == binb.show_doc
    assert binb._HOOKS["jupyter"]['app']  == binb.show_app

def test___all__():
    assert bi.__all__ == ALL

@pytest.mark.parametrize('name', ALL)
def test_contents(name):
    assert hasattr(bi, name)
