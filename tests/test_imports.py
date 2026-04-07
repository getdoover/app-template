"""
Basic tests for an application.

This ensures all modules are importable and that the config is valid.
"""

def test_import_app():
    from app_template.application import SampleApplication
    assert SampleApplication
    assert SampleApplication.config_cls is not None
    assert SampleApplication.tags_cls is not None
    assert SampleApplication.ui_cls is not None

def test_config():
    from app_template.app_config import SampleConfig
    schema = SampleConfig.to_schema()
    assert isinstance(schema, dict)
    assert len(schema["properties"]) > 0

def test_tags():
    from app_template.app_tags import SampleTags
    assert SampleTags

def test_ui():
    from app_template.app_ui import SampleUI
    assert SampleUI

def test_state():
    from app_template.app_state import SampleState
    assert SampleState
