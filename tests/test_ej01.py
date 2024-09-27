#!/usr/bin/env python3

import pytest
from src.ej01_def import nombre

def test_nombre():
    assert nombre("Diego") == "Diego"