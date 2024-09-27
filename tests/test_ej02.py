#!/usr/bin/env python3

import pytest
from src.ej02_def import importe

def test_nombre():
    assert importe(33, 3) == 99