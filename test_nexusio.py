# test_nexusio.py
"""
Tests for NexusIO module.
"""

import unittest
from nexusio import NexusIO

class TestNexusIO(unittest.TestCase):
    """Test cases for NexusIO class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexusIO()
        self.assertIsInstance(instance, NexusIO)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexusIO()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
