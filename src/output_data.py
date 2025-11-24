# ============================================================
# OUTPUT MODULE (Imperative Version)
# ============================================================
# This file handles saving processed datasets and reports.
# Team members must implement:
#
# 1. save_csv(df, path)
#    - Saves final DataFrame to CSV inside /data/processed/.
#    - Must confirm directory exists, create if not.
#
# 2. save_json(df, path)
#    - Saves dataset in JSON format.
#    - Ensure correct orientation (records).
#
# 3. save_summary_report(summary, path)
#    - Save text-based summaries or analysis reports.
#    - Example: missing-value report, correlation report.
#
# 4. print_to_console(df, max_rows = 10)
#    - Display sample rows to user.
#    - Useful for debugging.
#
# 5. save_plot(fig, path)
#    - Used by visualization module.
#    - Ensures /plots/ directory exists.
#
# NOTES:
# - All saving functions should print confirmation messages.
# - Handle errors (invalid paths, permission issues).
# - ALWAYS save processed results to /data/processed/
# ============================================================
