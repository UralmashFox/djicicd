from time import time

from uav_control import UAVControl


class TestLanding:
    def test_landing(self):
        vehicle = UAVControl("tcp://localhost:8000")
        self.assert_true(vehicle.armed)
        self.assert_false(vehicle.landed())

        vehicle.land()
        time.sleep(1)
        self.assert_true(vehicle.landed())

    def run_tests(self):
        self.test_landing()


if __name__ == "__main__":
    TestLanding.run_tests()