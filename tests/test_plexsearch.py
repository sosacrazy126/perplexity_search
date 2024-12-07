import pytest
from unittest.mock import patch, MagicMock
from plexsearch.core import perform_search

def test_perform_search_success():
    with patch('requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.json.return_value = {"text": "Test response"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        result = perform_search("test query", api_key="test_key")
        assert result == "Test response"
        mock_post.assert_called_once()

def test_perform_search_error():
    with patch('requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        
        with pytest.raises(Exception):
            perform_search("test query", api_key="test_key")