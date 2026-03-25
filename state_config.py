"""
State configuration for this OregonDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "OR"
STATE_NAME = "Oregon"
APP_NAME = "OregonDischargeWatch"
APP_TAGLINE = "Oregon Discharge Monitoring"
DOMAIN = "oregondischargewatch.org"
DATA_FILE = "or_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@oregondischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "PST"
EPA_REGION = 10
