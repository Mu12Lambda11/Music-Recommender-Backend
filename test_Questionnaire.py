import unittest
from unittest.mock import patch
from Questionnaire import questionnaire


class TestQuestionnaire(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "Artist1", "Artist2", "Artist3",  # Mocking the 3 music artists
        "Genre1", "Genre2", "Genre3",  # Mocking the 3 music genres
        "At a party",  # Mocking the context (occasion/location)
        "80s",  # Mocking the favorite decade
        "newer"  # Mocking the preference for older/newer music
    ])
    def test_questionnaire(self, mock_input):
        # Call the questionnaire function
        result = questionnaire()

        # Define the expected complete prompt
        expected_prompt = """Use the following information to produce a spotify-based playlist of recommended music.
            Do not include a title for the playlist, include only the songs.
            Format the songs as following without deviation: Title /// Album ### Artist (Year)
            Music artists I like include Artist1, Artist2, and Artist3. 
            I like Genre1, Genre2, and Genre3. 
            I want to listen to music in/at At a party. 
            My favorite period of music was the 80s. 
            I prefer newer music recommendations."""

        # Assert that the result matches the expected prompt
        self.assertEqual(result.strip(), expected_prompt.strip())

    @patch('builtins.input', side_effect=[
        "Artist1", "Artist2", "Artist3",  # Mocking the 3 music artists
        "Genre1", "Genre2", "Genre3",  # Mocking the 3 music genres
        "At a beach",  # Mocking the context (occasion/location)
        "90s",  # Mocking the favorite decade
        "both"  # Mocking the preference for older/newer music (should be converted to "older and newer")
    ])
    def test_questionnaire_with_mixed_preference(self, mock_input):
        # Call the questionnaire function
        result = questionnaire()

        # Define the expected complete prompt
        expected_prompt = """Use the following information to produce a spotify-based playlist of recommended music.
            Do not include a title for the playlist, include only the songs.
            Format the songs as following without deviation: Title /// Album ### Artist (Year)
            Music artists I like include Artist1, Artist2, and Artist3. 
            I like Genre1, Genre2, and Genre3. 
            I want to listen to music in/at At a beach. 
            My favorite period of music was the 90s. 
            I prefer older and newer music recommendations."""

        # Assert that the result matches the expected prompt
        self.assertEqual(result.strip(), expected_prompt.strip())


if __name__ == '__main__':
    unittest.main()
