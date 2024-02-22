test PgaeObject on Python using pytest and playright
just a proof of concept


python -m venv venv

#
python3 -m venv venv

#
venv\Scripts\activate
#
pip install pytest playwright pytest-html

#
go to /tests
#

pytest 01_test.py
#

or
#
pytest 01_test.py --html=report.html
