import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_doesnt_find(self):
        player = self.stats.search("Jaakko")
        self.assertEqual(player, None)

    def test_find_team(self):
        team = self.stats.team("PIT")
        self.assertEqual(team[0].name, "Lemieux")

    def test_most_points(self):
        player = self.stats.top(1)
        self.assertEqual(player[0].name, "Gretzky")

