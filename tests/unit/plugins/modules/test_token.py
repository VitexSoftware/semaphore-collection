# -*- coding: utf-8 -*-
# https://docs.ansible.com/ansible/latest/community/collection_contributors/collection_unit_tests.html


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from datetime import timedelta
from decimal import Decimal

import pytest

from plugins.modules.token import (
    convert_to_supported,
)

# We use the @pytest.mark.parametrize decorator to parametrize the function
# https://docs.pytest.org/en/latest/how-to/parametrize.html
# Simply put, the first element of each tuple will be passed to
# the test_convert_to_supported function as the test_input argument
# and the second element of each tuple will be passed as
# the expected argument.
# In the function's body, we use the assert statement to check
# if the convert_to_supported function given the test_input,
# returns what we expect.
@pytest.mark.parametrize('test_input, expected', [
    (timedelta(0, 43200), '12:00:00'),
    (Decimal('1.01'), 1.01),
    ('string', 'string'),
    (None, None),
    (1, 1),
])
