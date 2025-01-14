# Kitchen Showrooms Finder

This Python script allows you to find kitchen showrooms near a specified location using the Google Places API. The results are saved in a CSV file.

## Prerequisites

- Python 3.x installed on your system.
- A Google Cloud Platform account to obtain an API key.

## Getting a Google API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to the [API & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
4. Click on "Enable APIs and Services" and search for "Places API".
5. Enable the "Places API".
6. Go to the [Credentials page](https://console.cloud.google.com/apis/credentials).
7. Click "Create Credentials" and select "API Key".
8. Copy the API key and save it for later use.

## Downloading the Code

1. **Clone the Repository**: To clone the repository using Git, open your terminal or command prompt and run the following command:
   ```bash
   git clone https://github.com/AndrewVII/allstyle-maps-scraper.git
   ```

2. **Download as ZIP**: Alternatively, you can download the code as a ZIP file. Click on the "Code" button at the top of this page, and select "Download ZIP". Extract the ZIP file to your desired location.

Once you have the code on your local machine, proceed with setting up the environment as described below.

## Setting Up the Environment

### macOS

1. **Open Terminal**: You can find it in Applications > Utilities or search for it using Spotlight (Cmd + Space).

2. **Navigate to the Project Directory**: Use the `cd` command to change to the directory where your `main.py` file is located. For example:
   ```bash
   cd path/to/your/project
   ```

3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Windows

1. **Open Command Prompt**: Press `Win + R`, type `cmd`, and press Enter.

2. **Navigate to the Project Directory**: Use the `cd` command to change to the directory where your `main.py` file is located. For example:
   ```cmd
   cd path\to\your\project
   ```

3. **Create a Virtual Environment**:
   ```cmd
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:
   ```cmd
   venv\Scripts\activate
   ```

5. **Install Required Packages**:
   ```cmd
   pip install -r requirements.txt
   ```

## Running the Script

1. **Create a `.env` File**: In the same directory as `main.py`, create a file named `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **View the Results**: The script will output the results in JSON format and save them to a file named `showrooms.csv`.

## Notes

- Ensure your API key is kept secure and not shared publicly.
- The script is set to search for "kitchen showrooms near Hotel Indigo in Miami Brickell" by default. You can modify the `search_query` variable in `main.py` to change the search location or query.

## Troubleshooting

- If you encounter any issues with package installation, ensure that your virtual environment is activated and that you have an active internet connection.
- For any API-related errors, verify that your API key is correct and that the Places API is enabled in your Google Cloud project.
