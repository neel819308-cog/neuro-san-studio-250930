# Copyright (C) 2023-2025 Cognizant Digital Business, Evolutionary AI.
# All Rights Reserved.
# Issued under the Academic Public License.
#
# You can be released from the terms, and requirements of the Academic Public
# License by purchasing a commercial license.
# Purchase of a commercial license is mandatory for any use of the
# neuro-san-studio SDK Software in commercial settings.
#

import asyncio
import os
import unittest
from unittest.mock import Mock
from unittest.mock import patch

from coded_tools.now_agents.nowagent_api_get_agents import NowAgentAPIGetAgents

# Mock response data for testing
MOCK_AGENTS_RESPONSE = {
    "result": [
        {
            "name": "Test ITSM Agent",
            "description": "Handles IT service management inquiries",
            "sys_id": "12345678-1234-1234-1234-123456789abc",
        },
        {
            "name": "Test HR Agent",
            "description": "Assists with human resources questions",
            "sys_id": "87654321-4321-4321-4321-cba987654321",
        },
    ]
}


class TestNowAgentAPIGetAgents(unittest.TestCase):
    """
    Unit tests for NowAgentAPIGetAgents class.
    """

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.tool = NowAgentAPIGetAgents()
        self.test_args = {"inquiry": "Show me available agents"}
        self.test_sly_data = {}

    @patch.dict(
        os.environ,
        {
            "SERVICENOW_INSTANCE_URL": "https://test.service-now.com/",
            "SERVICENOW_GET_AGENTS_QUERY": "active=true",
            "SERVICENOW_USER": "test_user",
            "SERVICENOW_PWD": "test_password",
        },
    )
    @patch("coded_tools.now_agents.nowagent_api_get_agents.requests.get")
    def test_invoke_success(self, mock_get):
        """
        Test successful agent discovery.

        This test verifies that the tool correctly discovers ServiceNow AI agents
        when valid environment variables are set and the API returns a successful response.
        """
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_AGENTS_RESPONSE
        mock_get.return_value = mock_response

        # Execute the tool
        result = self.tool.invoke(self.test_args, self.test_sly_data)

        # Verify the result
        self.assertEqual(result, MOCK_AGENTS_RESPONSE)
        self.assertIn("result", result)
        self.assertEqual(len(result["result"]), 2)
        self.assertEqual(result["result"][0]["name"], "Test ITSM Agent")

        # Verify API call was made correctly
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertIn("api/now/table/sn_aia_agent", call_args[0][0])
        self.assertIn("sysparm_query=active=true", call_args[0][0])
        self.assertEqual(call_args[1]["auth"], ("test_user", "test_password"))

    @patch.dict(
        os.environ,
        {
            "SERVICENOW_INSTANCE_URL": "https://test.service-now.com/",
            "SERVICENOW_GET_AGENTS_QUERY": "active=true",
            "SERVICENOW_USER": "test_user",
            "SERVICENOW_PWD": "test_password",
        },
    )
    @patch("coded_tools.now_agents.nowagent_api_get_agents.requests.get")
    @patch("builtins.print")
    def test_invoke_authentication_failure(self, mock_print, mock_get):
        """
        Test handling of authentication failure.

        This test verifies that the tool properly handles 401 authentication errors
        from the ServiceNow API and prints error information.
        """
        # Mock 401 authentication error
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json.return_value = {"error": {"message": "User Not Authenticated"}}
        mock_get.return_value = mock_response

        # Execute the tool and expect error response instead of SystemExit
        result = self.tool.invoke(self.test_args, self.test_sly_data)

        # Verify error response structure
        self.assertIn("error", result)
        self.assertIn("status_code", result)
        self.assertIn("error_response", result)
        self.assertEqual(result["status_code"], 401)
        self.assertEqual(result["result"], [])

        # Verify error information was printed
        error_calls = [
            call for call in mock_print.call_args_list if "Status: 401" in str(call) or "Error Response:" in str(call)
        ]
        self.assertTrue(len(error_calls) >= 2, "Error messages should be printed")

    @patch.dict(
        os.environ,
        {
            "SERVICENOW_INSTANCE_URL": "https://test.service-now.com/",
            "SERVICENOW_GET_AGENTS_QUERY": "active=true",
            "SERVICENOW_USER": "test_user",
            "SERVICENOW_PWD": "test_password",
        },
    )
    @patch("coded_tools.now_agents.nowagent_api_get_agents.requests.get")
    def test_invoke_empty_results(self, mock_get):
        """
        Test handling of empty agent results.

        This test verifies that the tool correctly handles responses with no agents.
        """
        # Mock empty results response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": []}
        mock_get.return_value = mock_response

        # Execute the tool
        result = self.tool.invoke(self.test_args, self.test_sly_data)

        # Verify empty results are handled correctly
        self.assertEqual(result["result"], [])

    @patch("builtins.print")
    def test_get_env_variable(self, mock_print):
        """
        Test environment variable retrieval.

        This test verifies that the _get_env_variable helper method correctly
        retrieves environment variables.
        """
        with patch.dict(os.environ, {"TEST_VAR": "test_value"}):
            result = self.tool._get_env_variable("TEST_VAR")  # pylint: disable=protected-access
            self.assertEqual(result, "test_value")

        # Test missing environment variable - should print NOT defined message
        result = self.tool._get_env_variable("NONEXISTENT_VAR")  # pylint: disable=protected-access
        self.assertIsNone(result)

        # Verify the "NOT defined" message was printed
        not_defined_calls = [
            call for call in mock_print.call_args_list if "NONEXISTENT_VAR is NOT defined" in str(call)
        ]
        self.assertTrue(len(not_defined_calls) >= 1, "NOT defined message should be printed")

    @patch.dict(
        os.environ,
        {
            "SERVICENOW_INSTANCE_URL": "https://test.service-now.com/",
            "SERVICENOW_GET_AGENTS_QUERY": "active=true",
            "SERVICENOW_USER": "test_user",
            "SERVICENOW_PWD": "test_password",
        },
    )
    @patch("coded_tools.now_agents.nowagent_api_get_agents.requests.get")
    def test_async_invoke(self, mock_get):
        """
        Test asynchronous invoke method.

        This test verifies that the async_invoke method delegates correctly
        to the synchronous invoke method.
        """
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = MOCK_AGENTS_RESPONSE
        mock_get.return_value = mock_response

        # Execute the async tool
        result = asyncio.run(self.tool.async_invoke(self.test_args, self.test_sly_data))

        # Verify the result matches synchronous behavior
        self.assertEqual(result, MOCK_AGENTS_RESPONSE)


if __name__ == "__main__":
    unittest.main()
