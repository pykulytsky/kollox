import pytest
from todo.models import QuerySetChain
from todo.api.serializers import BaseToDoListSerializer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def chain(project, simple_list):
    return QuerySetChain(project, simple_list)


def test_base_combined_queryset(chain):
    assert chain.count() == 2


def test_combined_queryset_result(chain):
    assert False, chain


def test_combined_queryset_serializing(chain):
    serializer = BaseToDoListSerializer(chain)

    assert False, serializer.data