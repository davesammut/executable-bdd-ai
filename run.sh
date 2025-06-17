#!/bin/bash
echo "Starting API on port 5001..."
# Start the Flask API in the background and capture its PID
python3 -u -m api.api &
API_PID=$!

# Wait a moment to ensure the server starts up
sleep 2

echo "Running BDD tests..."
behave
TEST_EXIT_CODE=$?

# Kill the Flask API server
kill $API_PID
# Wait for the process to actually terminate
wait $API_PID 2>/dev/null

exit $TEST_EXIT_CODE
