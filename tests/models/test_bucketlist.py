"""
Contains tests for the bucketlist model
"""
from unittest import TestCase
from tests.base_case import BaseCase
from myapp.models.bucketlist import BucketList

class BucketListTests(BaseCase, TestCase):
    """
    Class contains tests for the user model
    """

    def test_bucketlist_table_created(self):
        """
        Method checks that the bucketlist table is created
        """
        bucketlist = BucketList.query.filter_by(id=1).first()
        self.assertEqual(
            1,
            bucketlist.id,
            "No data addded, so the table is not created"
        )