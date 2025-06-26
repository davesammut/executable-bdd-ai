#!/bin/bash
# BDD Test Runner: Starts the API, runs BDD (behave) tests, then shuts down the API.

export ENABLE_BDD_APP=1

echo "Starting API for BDD tests on port 5001..."
python3 -u -m api.api &
API_PID=$!

# Wait for the server to start
sleep 2

echo "Running BDD tests with behave..."
behave
TEST_EXIT_CODE=$?

echo "Stopping API server..."
kill $API_PID
wait $API_PID 2>/dev/null

exit $TEST_EXIT_CODE
