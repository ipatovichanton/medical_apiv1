> python3 -m venv .venv
#
> source .venv/bin/activate
#
> pip install -r requirements.txt
#
> python manage.py migrate
### this operation is slow, please wait finishing
> python manage.py cities_light
# medical_api_v2