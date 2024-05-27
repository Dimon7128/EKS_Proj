import pytest

@pytest.fixture
def config():
    return {"setting1": "value1", "setting2": "value2"}

def test_config_values(config):
    assert config["setting1"] == "value1"
    assert config["setting2"] == "value2"
