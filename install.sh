#!/bin/bash
pip3 install virtualenv==20.0.23
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python download_dataset.py
deactivate
