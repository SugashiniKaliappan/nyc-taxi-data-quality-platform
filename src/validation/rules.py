QUALITY_RULES = {
    "pickup_before_dropoff": {
        "description": "Pickup datetime should be before dropoff datetime.",
        "severity": "HIGH",
        "owner": "Data Engineering",
        "threshold_percent": 99.99
    },
    "positive_trip_distance": {
        "description": "Trip distance should be greater than zero.",
        "severity": "HIGH",
        "owner": "Data Engineering",
        "threshold_percent": 99.5
    },
    "non_negative_fare": {
        "description": "Fare amount should not be negative.",
        "severity": "HIGH",
        "owner": "Finance/Data Engineering",
        "threshold_percent": 99.5
    },
    "valid_passenger_count": {
        "description": "Passenger count should be between 1 and 6.",
        "severity": "MEDIUM",
        "owner": "Data Engineering",
        "threshold_percent": 99.0
    }
}
