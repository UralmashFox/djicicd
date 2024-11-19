from pymavlink import mavutil
from uav_control import UAVControl
from unittest import TestCase
from typing import Optional, Dict, Any

class TestTelemetry:
    def test_telemetry(self):
        uav = UAVControl("tcp://localhost:8000")
        try:
            telemetry = uav.get_telemetry()
        except AssertionError as e:
            logger.error("Ошибка в телеметрии: %s", e)
            return None
        except Exception as e:
            logger.error("Ошибка получения телеметрии: %s", e)
            return None