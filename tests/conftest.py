import os
import pytest
from utils.driver_factory import crear_driver


@pytest.fixture
def driver(request):
    driver = crear_driver()
    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        screenshot_path = f"reports/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)