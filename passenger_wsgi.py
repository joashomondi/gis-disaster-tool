"""
Passenger WSGI Entry Point for cPanel
This file is required for deploying Flask applications on cPanel using Passenger
"""

import sys
import os

# Add your application directory to the Python path
INTERP = os.path.join(os.environ['HOME'], 'virtualenv', 'gis-disaster-app', '3.11', 'bin', 'python3')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add application directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app as application

# Optional: Set production configurations
application.config['DEBUG'] = False

# Passenger expects the WSGI application to be named 'application'
# Our Flask app is imported as 'application' already

