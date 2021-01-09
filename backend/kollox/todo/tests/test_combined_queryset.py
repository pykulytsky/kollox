import pytest

from todo.models import QuerySetChain

pytestmark = [pytest.mark.django_db]


def test_base_combined_queryset(project, simple_list):
    chain = QuerySetChain()