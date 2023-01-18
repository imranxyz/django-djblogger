import pytest 

pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_string_return(self, post_factory):
        title = post_factory(title='test-post-title')
        assert title.__str__() == 'test-post-title'