cd ..
call .venv\Scripts\activate.bat
pytest test_app.py
start http://127.0.0.1:8000/nfe/
