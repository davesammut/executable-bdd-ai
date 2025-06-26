#!/bin/bash
# Normal app runner: starts the Flask API server on port 5001 in the foreground.

echo "Starting API on port 5001..."
python3 -u -m api.api
