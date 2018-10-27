git clone https://github.com/aeifn/savva3
virtualenv -ppython3 venv
. venv/bin/activate
cd savva3/
pip install -r requirements.txt
mv savva3/env_settings.py.example savva3/env_settings.py
