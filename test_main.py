import pytest
from main import format_user

@pytest.fixture
def example_people():
    return [
        {"name": {"title": "Dr", "first": "Uga", "last": "Dumpis"}, "nat": "LV"},
        {"name": {"title": "Mrs", "first": "Jānis", "last": "Liepnieks"}, "nat": "LV"}, 
        {"name": {"title": "Dr", "first": "Maeva", "last": "Fabre"}, "nat": "CH"}, 
        {"name": {"title": "Mr", "first": "Jevgeni", "last": "Sobcek"}, "nat": "RUS"},
        {"name": {"title": "Mr", "first": "Arvo", "last": "Eekali"}, "nat": "EST"}
        ]


def test_format_table(example_people):
  result = format_user(example_people[0], "country")
  assert result == "LV"
  result = format_user(example_people[3], "short")
  assert result == "Mr Jevgeni"
  result = format_user(example_people[4], "greeting")
  assert result == "Mr Arvo Eekali"
  result = format_user(example_people[1], "table")
  assert result == "Mrs | Jānis | Liepnieks | LV"
  
  # Pārbaudi vai short formāts atbilst formatējumam "Title Last", izvade "Mr Jevgeni"
  # Pārbaudi vai greeting formāts atbilst formatējumam "Title First Last", izvade "Mr Arvo Eekali"
  # Pārbaudi vai table formāts atbilst formatējumam "First | Last | Title | Nat", izvade "Mrs | Jānis | Liepnieks | LV"
  

  
pytest.main(["-v"])