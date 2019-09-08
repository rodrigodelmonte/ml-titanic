import pytest
from model import Model


@pytest.fixture(scope='session')
def model():
    '''Create a config to Model Class'''

    clf = Model()
    yield clf
