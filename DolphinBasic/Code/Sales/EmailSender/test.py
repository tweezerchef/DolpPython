import pytest


def create_email(name):
    # Remove special characters and convert to lowercase
    name = name.replace(" ", "_").replace("'", "").replace("-", "").lower()
    # Create the email address
    return f"{name}@mycompany.com"


class TestCreateEmail:
    def test_create_email_happy_path(self):
        assert create_email("John Doe") == "john_doe@mycompany.com"

    def test_create_email_special_characters(self):
        assert create_email("O'Reilly-Conor") == "oreilly_conor@mycompany.com"

    def test_create_email_empty_string(self):
        assert create_email("") == "@mycompany.com"
