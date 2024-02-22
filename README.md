python -m venv venv
python3 -m venv venv


venv\Scripts\activate

pip install -r requirements.txt

go to /tests
pytest 01_test.py

pytest 01_test.py --html=report.html
