from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mysql.connector
import requests

# Connexion à la base MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ordonnancement'
}

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/user/"):
            try:
                user_id = int(self.path.split("/")[-1])

                # Connexion à la base
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
                user = cursor.fetchone()
                cursor.close()
                conn.close()

                if not user:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b"User not found")
                    return

                # Appel de l'API Node js
                email = user['email']
                response = requests.get(f"http://localhost:3000/api/users?email={email}")
                if response.status_code == 200:
                    api_data = response.json()
                else:
                    api_data = {}

                # Fusion des données SQL + API
                result = {**user, **api_data}

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Server error: {str(e)}".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

if __name__ == "__main__":
    server = ThreadingHTTPServer(('localhost', 8080), MyHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
