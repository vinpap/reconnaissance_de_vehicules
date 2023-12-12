"""
Tests the 'predict' function.
"""
import torch
import pytest

from model import predict

@pytest.fixture
def model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s')


def test_no_vehicle(model):
    """
    Makes sure the model does not detect a truck on a picture not showing any
    vehicle.
    """
    filepath = "./test_images/no_vehicle.jpg"
    assert predict(model, filepath) == -1


def test_one_car(model):
    """
    Makes sure the model does not detect a truck on a picture showing a car.
    """
    filepath = "./test_images/one_car.jpg"
    assert predict(model, filepath) == -1

def test_one_truck(model):
    """
    Makes sure the model detects a truck on a picture showing one.
    """
    filepath = "./test_images/one_truck.png"
    assert 0 <= predict(model, filepath) <= 1