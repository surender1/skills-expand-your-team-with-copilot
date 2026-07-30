import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from backend import database


class DatabaseSeedTests(unittest.TestCase):
    def test_manga_club_seeded_with_requested_details(self):
        activity = database.initial_activities.get("Manga Club")

        self.assertIsNotNone(activity)
        self.assertEqual(
            activity["description"],
            "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        )
        self.assertEqual(activity["schedule"], "Tuesdays, 7:00 PM - 8:00 PM")
        self.assertEqual(activity["max_participants"], 15)


if __name__ == "__main__":
    unittest.main()
