#!/usr/bin/env python3

from unittest.mock import patch
from src.ej04_def import conversion

def test_conversion():
    with patch('builtins.input', return_value="33.8"):
        assert conversion() == 1.0
        
    with patch('builtins.input', return_value="-33.8"):
        assert conversion() == -1.0