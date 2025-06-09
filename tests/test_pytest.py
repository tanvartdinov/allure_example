# pip install pytest


import pytest
from main import factorial, summarize
from phonebook import PhoneBook


def test_summarize_1():
    assert summarize(5, 7) == 12


@pytest.mark.xfail
def test_summarize_2():
    assert summarize(0, 7) == 7


@pytest.mark.skipif(True, reason='Боевой сервер')
def test_summarize_3():
    assert summarize(0, 7) == 7


@pytest.mark.parametrize(
    'a,b,expected',
    (
            (5, 7, 12),
            (5, -7, -2),
            (-5, 7, 2),
    )
)
def test_summarize_with_params(a, b, expected):
    assert summarize(a, b) == expected


@pytest.fixture
def get_summarize_data():
    # что-то делаем до теста
    yield 5, 7, 12
    # что-то делаем после теста


def test_summarize_with_fixture(get_summarize_data):
    a, b, expected = get_summarize_data
    assert summarize(a, b) == expected


@pytest.fixture(params=(
        (5, 7, 12),
        (5, -7, -2),
        (-5, 7, 2),
))
def get_summarize_data2(request):
    return request.param

def test_summarize_with_fixture2(get_summarize_data2):
    a, b, expected = get_summarize_data2
    assert summarize(a, b) == expected




class TestPhoneBook:
    def setup_method(self):
        self.phonebook = PhoneBook()
        self.phonebook.add_contact('Мама', 124124124)
        self.phonebook.add_contact('папа', 999999999)
        self.phonebook.add_contact('братан', 345345623)
        self.phonebook.add_contact('Васек', 457373434)
        self.phonebook.add_contact('ПАПА', 888888888)

    def teardown_method(self):
        del self.phonebook

    def test_create_empty_book(self):
        phonebook = PhoneBook()
        assert len(phonebook.get_all_contacts()) == 0

    def test_add_contact(self):
        assert len(self.phonebook.get_all_contacts()) == 4

    def test_find_contact_success(self):
        assert self.phonebook.find_contact('Папа') == 888888888

    def test_find_contact_failed(self):
        assert self.phonebook.find_contact('Жора') is None