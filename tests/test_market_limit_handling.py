import unittest

from run_analyzer import resolve_market_limit


class ResolveMarketLimitTests(unittest.TestCase):
    def test_prefers_configured_limit_when_set(self):
        self.assertEqual(resolve_market_limit("forex", configured_limit=25), 25)

    def test_uses_category_default_when_config_is_none(self):
        self.assertEqual(resolve_market_limit("forex", configured_limit=None), 50)

    def test_uses_category_default_when_explicitly_requested(self):
        self.assertEqual(resolve_market_limit("forex", configured_limit=None, use_category_defaults=True), 50)

    def test_fetches_all_markets_when_defaults_disabled(self):
        self.assertIsNone(resolve_market_limit("forex", configured_limit=None, use_category_defaults=False))

    def test_uses_default_cap_for_unknown_categories_with_defaults(self):
        self.assertEqual(resolve_market_limit("mystery", configured_limit=None, use_category_defaults=True), 50)


if __name__ == "__main__":
    unittest.main()
