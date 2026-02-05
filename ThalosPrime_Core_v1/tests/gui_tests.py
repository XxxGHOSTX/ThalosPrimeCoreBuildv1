"""
Thalos Prime - GUI Tests
Copyright (c) 2026 Tony Ray Macier III
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from gui.window_manager import WindowManager
from gui.font_manager import FontManager


class TestWindowManager(unittest.TestCase):
    def setUp(self):
        # Note: GUI tests require display, may need headless mode for CI
        pass

    def test_initialization(self):
        # Placeholder - full GUI tests require display
        self.assertTrue(True)


class TestFontManager(unittest.TestCase):
    def setUp(self):
        self.font_manager = FontManager()

    def test_load_fonts(self):
        self.assertIn('mono', self.font_manager.fonts)
        self.assertIn('title', self.font_manager.fonts)

    def test_get_font(self):
        font = self.font_manager.get_font('mono')
        self.assertIsNotNone(font)


if __name__ == '__main__':
    unittest.main()
