import unittest

from run_analyzer import resolve_market_limit


class ResolveMarketLimitTests(unittest.TestCase):
    def test_prefers_configured_limit_when_set(self):
        self.assertEqual(resolve_market_limit("forex", configured_limit=25), 25)

    def test_returns_none_when_config_is_none(self):
        self.assertIsNone(resolve_market_limit("forex", configured_limit=None))

    def test_uses_category_default_only_when_requested(self):
        self.assertEqual(resolve_market_limit("forex", configured_limit=None, use_category_defaults=True), 30)

    def test_uses_default_cap_for_unknown_categories_when_requested(self):
        self.assertEqual(resolve_market_limit("mystery", configured_limit=None, use_category_defaults=True), 100)


if __name__ == "__main__":
    unittest.main()
