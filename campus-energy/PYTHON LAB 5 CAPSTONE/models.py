# models.py  --- Task 3: Object-Oriented Modeling

from datetime import datetime

# ---------------------------------------------------
# MeterReading Class
# ---------------------------------------------------
class MeterReading:
    """
    Represents a single electricity meter reading.
    """
    def __init__(self, timestamp: datetime, kwh: float):
        self.timestamp = timestamp
        self.kwh = float(kwh)


# ---------------------------------------------------
# Building Class
# ---------------------------------------------------
class Building:
    """
    Represents a building with many meter readings.
    """
    def __init__(self, name: str):
        self.name = name
        self.meter_readings = []  # list of MeterReading objects

    def add_reading(self, reading: MeterReading):
        """Adds a MeterReading object to this building."""
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        """Returns total energy consumption in kWh."""
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        """Returns mean, min, max, total energy consumption as a dictionary."""
        if not self.meter_readings:
            return {
                "building": self.name,
                "mean": 0,
                "min": 0,
                "max": 0,
                "total": 0
            }

        kwh_values = [r.kwh for r in self.meter_readings]

        return {
            "building": self.name,
            "mean": sum(kwh_values) / len(kwh_values),
            "min": min(kwh_values),
            "max": max(kwh_values),
            "total": sum(kwh_values)
        }


# ---------------------------------------------------
# BuildingManager Class
# ---------------------------------------------------
class BuildingManager:
    """
    Manages multiple Building objects and populates them with readings.
    """
    def __init__(self):
        self.buildings = {}

    def get_or_create(self, building_name: str):
        """Retrieve a building; create it if it doesn't exist."""
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        return self.buildings[building_name]

    def add_reading_from_row(self, row):
        """
        Given a row of df_combined, create a MeterReading and add it to the correct building.
        Expect row to contain: timestamp, kwh, building
        """
        building = self.get_or_create(row["building"])
        reading = MeterReading(row["timestamp"], row["kwh"])
        building.add_reading(reading)

    def generate_all_reports(self):
        """
        Returns a dictionary of reports for all buildings.
        """
        return {
            building_name: building.generate_report()
            for building_name, building in self.buildings.items()
        }


# ---------------------------------------------------
# Example Usage (To test functionality)
# ---------------------------------------------------
if __name__ == "__main__":
    print("Run via integration script (run_all.py).")

