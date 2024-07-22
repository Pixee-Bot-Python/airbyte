# Copyright (c) 2023 Airbyte, Inc., all rights reserved.

import string

import pytest
import secrets


@pytest.fixture
def random_string():
    return "".join(secrets.SystemRandom().choices(string.ascii_uppercase + string.digits, k=10))
