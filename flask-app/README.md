# Flask Application

This is a simple Flask application that demonstrates basic routing and JSON handling.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   └── api_teste.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables in the `.env` file as needed.

2. Run the application:
   ```
   python -m app.api_teste
   ```

3. Access the endpoints:
   - GET request to `/hello` will return a greeting message.
   - POST request to `/echo` will return the JSON data you send.

## License

This project is licensed under the MIT License.