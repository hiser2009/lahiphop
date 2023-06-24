import pytest
from flask import template_rendered
from event import event

@pytest.fixture
def captured_templates(app):
    templates = []

    def capture(sender, template, context, **extra):
        templates.append(template)

    template_rendered.connect(capture, app)

    try:
        yield templates
    finally:
        template_rendered.disconnect(capture, app)

def test_index_route(client, captured_templates):
    response = client.get('/')
    assert response.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == 'index.html'
    assert 'events' in context
    assert 'pst_formatted' in context


