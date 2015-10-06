# encoding: utf-8
import json
import os

import pytest

from api.models import FormData


@pytest.fixture
def fixture():
    def load(name):
        fixture = os.path.join(os.path.dirname(__file__), 'fixtures', name)
        with open(fixture) as f:
            return f.read()
    return load


@pytest.fixture
def model_data(user, fixture):
    model_data = {
        'author': user.id,
        'form': {
            'title': 'my form',
            'action': '/action/create',
            'method': 'POST',
            'enctype': 'multipart/form-data',
            'html': '<form></form>',
            'help_text': 'help, HELP!!',
            'css_classes': 'form inline',
            'elements_css_classes': 'form-control',
            'elements': json.loads(fixture('simple_form.json'))['form']['elements'],
        }
    }
    return model_data


@pytest.fixture
def model(model_data, user):
    model_data['form']['author'] = user
    return FormData.objects.create(**model_data['form'])


@pytest.fixture
def form_data(fixture, user):
    form_data = json.loads(fixture('simple_form.json'))
    form_data['author'] = user.id
    return json.dumps(form_data)


@pytest.fixture
def sample_dict():
    data = {
        '1': 'string',
        '2': [1, 2, 3, 4, 5],
        '3': {
            '1': 'string',
            '2': [1, 2, 3, 4, 5],
        }
    }
    return data


@pytest.fixture
def login(client, user):
    """Return the User instance after logging the user in."""
    assert client.login(user=user.username, password=user.password)
    return user
