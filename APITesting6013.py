"""
Test the citizen and registration apis for the 3:00 AM Group.

@author 6210546013 Vichisorn Wejsupakul
"""
from datetime import date
import unittest
import requests
from dateutil.relativedelta import relativedelta

base_url = 'https://wcg-apis.herokuapp.com'

data = dict(name='', surname='', citizen_id=0, birth_date='',
            occupation='', address='', phone_number='', is_risk=False)


def post_to_register():
    response = requests.post(
        url=base_url + f"/registration?"
                       f"name={data['name']}"
                       f"&surname={data['surname']}"
                       f"&citizen_id={data['citizen_id']}"
                       f"&birth_date={data['birth_date']}"
                       f"&occupation={data['occupation']}"
                       f"&address={data['address']}"
                       f"&phone_number={data['phone_number']}"
                       f"&is_risk={data['is_risk']}"
    )

    return response


class ProjectApiTestCase(unittest.TestCase):
    """
    Test case for Project API from https://wcg-apis.herokuapp.com/.
    """

    def setUp(self) -> None:
        data['name'] = 'Vichisorn'
        data['surname'] = 'Wejsupakul'
        data['citizen_id'] = 1101402211111
        data['birth_date'] = '2000-10-26'
        data['occupation'] = 'Student'
        data['address'] = 'Test Register POST API'
        data['phone_number'] = '0964590546'
        data['is_risk'] = False

    def tearDown(self) -> None:
        requests.delete(f"{base_url}/registration/{data['citizen_id']}")
        for key in data:
            data[key] = ''

    def test_GET_a_registration(self):
        """
        Test get a citizen from /registration/{citizen_id}.
        """

        post_to_register()

        response = requests.get(
            url=f"{base_url}/registration/{data['citizen_id']}"
        )
        self.assertEqual(200, response.status_code, 'GET a citizen from citizen API.')

    def test_GET_invalid_citizen(self):
        """
        Test get a citizen from /registration/{citizen_id} but invalid citizen_id.
        """
        post_to_register()
        response = requests.get(
            url=f"{base_url}/registration/11014022111"
        )
        self.assertEqual(404, response.status_code, 'Cannot GET a citizen from citizen API.')

    def test_DELETE_a_citizen(self):
        """
        Test delete a citizen from /registration/{citizen_id} but
        I cannot test the invalid one because it will be delete all citizen databases.
        """
        post_to_register()
        response = requests.delete(f"{base_url}/registration/{data['citizen_id']}")

        self.assertEqual(200, response.status_code, 'Can delete a citizen from citizen API.')

    def test_POST_to_register(self):
        """
        Test post to /registration with normal data.
        """
        response = post_to_register()

        self.assertEqual(201, response.status_code, 'Can Send to the Register API.')

    def test_POST_name_as_number(self):
        """
        Test post to /registration but name as number.
        """
        data['name'] = 11000100
        response = post_to_register()

        # self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be number!"}\n', response.text)

    def test_POST_name_as_symbol(self):
        """
        Test post to /registration but name as symbol.
        """
        data['name'] = '☺☺☺☺☺☺'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be symbol!"}\n', response.text)

    def test_POST_name_as_None(self):
        """
        Test post to /registration but name as None.
        """
        data['name'] = None
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be None!"}\n', response.text)

    def test_POST_surname_as_number(self):
        """
        Test post to /registration but surname as number.
        """
        data['surname'] = 11000100
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be number!"}\n', response.text)

    def test_POST_surname_as_symbol(self):
        """
        Test post to /registration but surname as symbol.
        """
        data['surname'] = '☺☺☺☺☺☺'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be symbol!"}\n', response.text)

    def test_POST_surname_as_None(self):
        """
        Test post to /registration but surname as None.
        """
        data['surname'] = None
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: name cannot be None!"}\n', response.text)

    def test_POST_citizen_id_less_than_13_number(self):
        """
        Test post to /registration but citizen id number less than 13.
        """
        data['citizen_id'] = 11014022111
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid citizen ID"}\n', response.text)

    def test_POST_citizen_id_more_than_13_number(self):
        """
        Test post to /registration but citizen id number more than 13.
        """
        data['citizen_id'] = 11014022111111111
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid citizen ID"}\n', response.text)

    def test_POST_citizen_id_as_text(self):
        """
        Test post to /registration but citizen id as text.
        """
        data['citizen_id'] = 'citizen_id data'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid citizen ID"}\n', response.text)

    def test_POST_citizen_id_as_symbol(self):
        """
        Test post to /registration but citizen id as symbol.
        """
        data['citizen_id'] = '☺☺☺☺☺☺☺☺☺☺☺☺☺'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid citizen ID"}\n', response.text)

    def test_POST_citizen_id_as_None(self):
        """
        Test post to /registration but citizen_id as None.
        """
        data['citizen_id'] = None
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid citizen ID"}\n', response.text)

    def test_POST_birth_date_as_text(self):
        """
        Test post to /registration but birth date as text.
        """
        data['birth_date'] = 'birth_date data'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid birth date format"}\n', response.text)

    def test_POST_birth_date_as_symbol(self):
        """
        Test post to /registration but birth date as symbol.
        """
        data['birth_date'] = '♂☺'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid birth date format"}\n', response.text)

    def test_POST_too_old_birth_date(self):
        """
        Test post to /registration but too old birth date.
        """
        data['birth_date'] = (date.today() - relativedelta(years=1000)).strftime('%Y-%m-%d')
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid birth date format"}\n', response.text)

    def test_POST_not_achieved_minimum_age(self):

        """
        Test post to /registration but not achieved minimum age.
        """
        data['birth_date'] = (date.today() - relativedelta(years=12)).strftime('%Y-%m-%d')
        response = post_to_register()
        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: not archived minimum age"}\n', response.text)

    def test_POST_future_birth_date(self):
        """
        Test post to /registration but future birth date.
        """
        data['birth_date'] = (date.today() + relativedelta(years=1)).strftime('%Y-%m-%d')
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: not archived minimum age"}\n', response.text)

    def test_POST_birth_date_as_None(self):
        """
        Test post to /registration but birth date is None.
        """
        data['birth_date'] = None
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid birth date format"}\n', response.text)

    def test_POST_occupation_as_number(self):
        """
        Test post to /registration but occupation as number.
        """
        data['occupation'] = 110101020
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid occupation"}\n', response.text)

    def test_POST_occupation_as_symbol(self):
        """
        Test post to /registration but occupation as symbol.
        """
        data['occupation'] = '☺☺☺☺☺☺'
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid occupation"}\n', response.text)

    def test_POST_occupation_as_None(self):
        """
        Test post to /registration but occupation is None.
        """
        data['occupation'] = None
        response = post_to_register()

        self.assertEqual(200, response.status_code, 'Send the citizen')
        self.assertEqual('{"feedback":"registration failed: invalid occupation"}\n', response.text)
