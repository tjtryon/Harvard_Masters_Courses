#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════════
# ⏱️ TRTS Console Launcher
# ═══════════════════════════════════════════════════════════════════════════════

# Detect if we're in Docker
if [ -f /.dockerenv ]; then
    echo "🐳 Running in Docker environment"
    PYTHON_CMD="python3"
else
    echo "💻 Running in local environment"
    
    # Check for virtual environment
    if [ -d "venv" ]; then
        echo "🐍 Activating virtual environment..."
        source venv/bin/activate
        PYTHON_CMD="python"
    elif [ -d ".venv" ]; then
        echo "🐍 Activating virtual environment..."
        source .venv/bin/activate
        PYTHON_CMD="python"
    else
        PYTHON_CMD="python3"
    fi
fi

# Set environment variables
export TRMS_BASE="$(pwd)"
export TRMS_ENV="${TRMS_ENV:-development}"

# Run TRTS console
echo "⏱️ Starting TRTS: The Race Timing Solution (Console)"
echo "════════════════════════════════════════════════════════════════════════════════"

cd "TRTS: The Race Timing Solution"

# Check for the actual TRTS console file structure from GitHub
if [ -f "race_timing_console.py" ]; then
    $PYTHON_CMD race_timing_console.py
elif [ -f "console/race_timing_console.py" ]; then
    cd console
    $PYTHON_CMD race_timing_console.py
elif [ -f "src/race_timing_console.py" ]; then
    cd src
    $PYTHON_CMD race_timing_console.py
else
    echo "⚠️  TRTS console application not found"
    echo "Please ensure TRTS is properly installed from GitHub"
    echo "Repository: https://github.com/tjtryon/TRTS-The-Race-Timing-Solution"
fi
