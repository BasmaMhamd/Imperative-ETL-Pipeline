# ============================================================
# PIPELINE CONTROLLER (Imperative Version)
# ============================================================
# This file controls the ENTIRE workflow logically:
#
# 1. Load data
# 2. Handle missing values
# 3. Transform data
# 4. Analyze results
# 5. Save outputs
#
# Team members should implement:
#
# pipeline():
#    - Reads config or hardcoded paths.
#    - Calls loader → cleaning → transform → analysis.
#    - Each step prints clear log messages.
#    - Saves final cleaned dataset to /data/processed.
#
# NOTES:
# - This is the main place to connect all modules together.
# - Use clear step-by-step procedural logic.
# ============================================================
