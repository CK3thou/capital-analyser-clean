import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("app_module", ROOT / "app.py")
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


def test_auto_refresh_provisions_removed():
    assert not hasattr(app_module, "AUTO_REFRESH_ENABLED")
    assert not hasattr(app_module, "AUTO_REFRESH_INTERVAL_HOURS")
