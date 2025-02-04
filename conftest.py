import json
import pytest
from datetime import datetime
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = "reports"
    now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    # Créer le dossier reports s'il n'existe pas
    os.makedirs(reports_dir, exist_ok=True)
    # Définir le chemin du rapport HTML
    config.option.htmlpath = os.path.join(reports_dir, f"report_{now}.html")

@pytest.fixture(scope="session",autouse=True)
def set_up_tear_down():
    print("\nSTART")
    yield
    print("\nEND")


@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with  open(json_file_path) as json_file :
        data = json.load(json_file)
    return data