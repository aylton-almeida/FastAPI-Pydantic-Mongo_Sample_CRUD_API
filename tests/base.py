"""TEST - BASE
Definition of BaseTest class, used on all the test classes
"""

# # Native # #
from multiprocessing import Process

# # Installed # #
import httpx
from wait4it import get_free_port, wait_for

# # Project # #
from people_api import run
from people_api.database import collection
from people_api.settings import api_settings

__all__ = ("BaseTest",)


class BaseTest:
    api_process: Process
    api_url: str

    @classmethod
    def setup_class(cls):
        # Startup the API on a process before all tests
        # NOTE process can make mocking more difficult
        api_port = api_settings.port = get_free_port()
        cls.api_url = f"http://localhost:{api_port}"
        cls.api_process = Process(target=run, daemon=True)
        cls.api_process.start()
        wait_for(port=api_port)

    @classmethod
    def teardown_class(cls):
        cls.api_process.terminate()

    @classmethod
    def teardown_method(cls):
        # Delete all documents from collection after each test
        collection.delete_many({})

    # # API Methods # #

    async def get_person(self, person_id: str, statuscode: int = 200):
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.api_url}/people/{person_id}")
        assert r.status_code == statuscode, r.text
        return r

    async def list_people(self, statuscode: int = 200):
        async with httpx.AsyncClient() as client:
            r = await client.get(f"{self.api_url}/people")
        assert r.status_code == statuscode, r.text
        return r

    async def create_person(self, create: dict, statuscode: int = 201):
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.api_url}/people", json=create)
        assert r.status_code == statuscode, r.text
        return r

    async def update_person(self, person_id: str, update: dict, statuscode: int = 204):
        async with httpx.AsyncClient() as client:
            r = await client.patch(f"{self.api_url}/people/{person_id}", json=update)
        assert r.status_code == statuscode, r.text
        return r

    async def delete_person(self, person_id: str, statuscode: int = 204):
        async with httpx.AsyncClient() as client:
            r = await client.delete(f"{self.api_url}/people/{person_id}")
        assert r.status_code == statuscode, r.text
        return r

