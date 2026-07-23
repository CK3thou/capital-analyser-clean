import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("app_module", ROOT / "app.py")
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)


def test_should_refresh_when_interval_elapsed():
    app_module.init_db()
    app_module.set_last_fetch_time("2024-01-01T00:00:00")

    now = app_module.datetime(2024, 1, 1, 1, 0, 0)
    should_refresh = app_module.should_refresh_data(now=now, interval_hours=1)

    assert should_refresh is True
