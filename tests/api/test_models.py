# encoding: utf-8
import json

from api.models import FormData


def test_convert_to_dict(sample_dict):
    data = json.dumps(sample_dict)
    converted_data = FormData.convert_to_dict(data)
    assert type(converted_data) == dict
    data = {k: json.dumps(v) for k, v in sample_dict.items()}
    converted_data = FormData.convert_to_dict(data)
    assert type(converted_data) == dict


def test_convert_values_to_string(sample_dict):
    converted_data = FormData.convert_values_to_string(sample_dict)
    assert all(type(v) == str for _, v in converted_data.items())