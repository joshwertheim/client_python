from ..resource import Resource
from .timeclock import Timeclock


class Worker(Resource):
    """Organization administrators"""
    PATH = "organizations/{organization_id}/locations/{location_id}/roles/{role_id}/users/{user_id}"
    ID_NAME = "user_id"

    def get_timeclocks(self, **kwargs):
        return Timeclock.get_all(parent=self, **kwargs)

    def get_timeclock(self, id):
        return Timeclock.get(parent=self, id=id)

    def create_timeclock(self, **kwargs):
        return Timeclock.create(parent=self, **kwargs)
