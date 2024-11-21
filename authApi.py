#THIS IS AN API BUILDING WHICH NEEDS TOKEN TO ACCESS THE LINK
#http://127.0.0.1:5000/download?token=lol

from flask import Flask, request, abort, send_file

# Initialize the Flask application
app = Flask(__name__)

# Define the secret token used for authentication
API_TOKEN = 'lol'  # This is the secret token needed to access the CSV file

# Path to the local CSV file that will be served for download
CSV_FILE_PATH = r"C:\Users\pooji\Desktop\cvs\athlete_events.csv"  # Path to your CSV file on your system

# Define the route for downloading the file
@app.route('/download', methods=['GET'])  # This route is triggered by a GET request to '/download'
def download_file():
    # Retrieve the token from the query string in the URL
    token = request.args.get('token')

    # Check if the token matches the expected secret token
    if token != API_TOKEN:
        # If the token is incorrect, return a 401 Unauthorized error
        abort(401, description="Unauthorized: Invalid API token")

    # If the token is correct, serve the CSV file to the user
    return send_file(CSV_FILE_PATH, as_attachment=True, download_name='athlete1.csv')  # Send the file as a download with the given name

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask application in debug mode for easier troubleshooting
