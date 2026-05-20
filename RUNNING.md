Setup and run the Simple FastAPI App

1. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\Activate.ps1 # Windows PowerShell
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app with uvicorn:

```bash
uvicorn app.main:app --reload
```

4. Open your browser: http://127.0.0.1:8000/
Interactive docs: http://127.0.0.1:8000/docs
