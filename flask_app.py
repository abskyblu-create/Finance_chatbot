# flask_app.py

print(">>> flask_app.py started running")

import os
import pandas as pd
from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename

from chatbot_logic import chatbot_web, df as default_df

app = Flask(__name__)

# Safety limits (demo-friendly)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB max upload

# Simple in-memory storage for uploaded data (DEMO).
# NOTE: On free Render instances / multi-user use, this is shared across users.
uploaded_df = None

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Finance Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 30px auto; padding: 0 12px; }
        input[type="text"] { padding: 10px; }
        input[type="file"] { padding: 6px; }
        input[type="submit"] { padding: 10px 14px; cursor: pointer; }
        .box { border: 1px solid #ddd; padding: 14px; border-radius: 10px; margin: 14px 0; }
        .muted { color: #666; font-size: 14px; }
        pre { background: #f7f7f7; padding: 12px; border-radius: 8px; overflow-x: auto; }
        .footer { margin-top: 18px; font-size: 14px; color: #444; }
    </style>
</head>
<body>
    <h2>Finance Chatbot</h2>

    <div class="box">
        <h3>1) Upload your CSV/Excel (optional)</h3>
        <div class="muted">
            Upload a file to use your own dataset. If you don't upload, the app uses the default dataset.
            Supported: .csv, .xlsx, .xls (max 5 MB)
        </div>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv,.xlsx,.xls" />
            <input type="submit" name="action" value="Upload" />
        </form>

        {% if upload_msg %}
            <p><b>{{ upload_msg }}</b></p>
        {% endif %}
    </div>

    <div class="box">
        <h3>2) Ask a question</h3>
        <div class="muted">
            Tip: Type <b>help</b> to see the 10 questions, or type a question number (1-10).
        </div>

        <form method="post">
            <input type="text" name="query" placeholder="Ask question..." size="50" />
            <input type="submit" name="action" value="Ask" />
        </form>

        {% if response %}
            <h3>Response:</h3>
            <pre>{{ response }}</pre>
        {% endif %}
    </div>

    <div class="footer">
        Created by
        <a href="https://www.linkedin.com/in/ankit-bhatt-4a1631388/" target="_blank" rel="noopener noreferrer">
            Ankit Bhatt
        </a>
    </div>
</body>
</html>
"""

def normalize_columns(df_in: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizes column names so user files with different casing/spaces don't break as easily.
    Example: 'Total Revenue' -> 'total_revenue'
    """
    df_in = df_in.copy()
    df_in.columns = (
        df_in.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )
    return df_in

def load_user_file(file_storage):
    """
    Reads an uploaded CSV/Excel file and returns (df, message).
    """
    filename = secure_filename(file_storage.filename or "")
    if not filename:
        return None, " No file selected."

    ext = os.path.splitext(filename)[1].lower()

    try:
        if ext == ".csv":
            df_u = pd.read_csv(file_storage)
        elif ext in [".xlsx", ".xls"]:
            df_u = pd.read_excel(file_storage)
        else:
            return None, " Unsupported file type. Please upload .csv or .xlsx/.xls only."
    except Exception as e:
        return None, f" Could not read file: {e}"

    df_u = normalize_columns(df_u)

    return df_u, f" Uploaded '{filename}' successfully. Rows: {len(df_u)}, Columns: {len(df_u.columns)}"

@app.route("/", methods=["GET", "POST"])
def home():
    global uploaded_df

    response = ""
    upload_msg = ""

    if request.method == "POST":
        action = request.form.get("action", "")

        # 1) Upload
        if action == "Upload":
            f = request.files.get("file")
            if not f:
                upload_msg = " No file received."
            else:
                new_df, msg = load_user_file(f)
                upload_msg = msg
                if new_df is not None:
                    uploaded_df = new_df

        # 2) Ask
        elif action == "Ask":
            user_query = request.form.get("query", "").strip()

            # Choose uploaded df if available, otherwise default df from chatbot_logic
            active_df = uploaded_df if uploaded_df is not None else default_df

            # Call your existing chatbot logic (do not change your chatbot)
            response = chatbot_web(user_query, active_df)

    return render_template_string(HTML_PAGE, response=response, upload_msg=upload_msg)

if __name__ == "__main__":
    # For local only. In Render production, Gunicorn will run flask_app:app
    app.run(debug=True)
