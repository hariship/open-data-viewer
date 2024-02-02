# Open Data Viewer

This project demonstrates how to set up a Cesium globe with an access token using HTML and JavaScript on the client side and a Flask server on the server side for backend operations. The access token is kept in a separate configuration file for security and flexibility.

![Demo](client/static/globe_population-ezgif.com-video-to-gif-converter.gif)

## Client Side

### Getting Started

Follow these steps to set up and run the client part of the project:

1. Clone or download this repository to your local machine.

2. Navigate to the `client` directory in your code editor.

3. Create a `config.js` file in the `client` directory and add your Cesium access token.

    ```javascript
    let cesiumAccessToken = 'your token here';
    ```

4. Make sure you have Node.js installed on your machine. If not, you can download it from [the official website](https://nodejs.org/). Execute the below command to install `http-server` globally.

    ```javascript
    npm install -g http-server
    ```

5. Open your terminal/command prompt and navigate to the `client` directory.

6. Start the server by running:

    ```javascript
    http-server
    ```

7. Open your web browser and go to `http://127.0.0.1:8080` to see the Cesium globe with your access token in action.

### Usage

- The globe allows you to click on it to add pins at specific locations.
- Hovering over a pin displays information about the location.
- You can customize the pins, appearance, and functionality as needed in the JavaScript code.

### Configuration

- The access token is stored in the `config.js` file for security. You can create your own in the home directory and access it.

## Server Side

### Getting Started

Follow these steps to set up and run the server part of the project:

1. Navigate to the `server` directory.

2. Make sure you have Python and pip installed on your machine.

3. Install the necessary Python packages using:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the `main.py` script to start the server.

    ```bash
    python main.py
    ```

### Troubleshooting

- If you encounter issues, you may want to ensure that all dependencies are correctly installed and that the server is running properly.
- For client-side issues, clear your browser cache or use an incognito/private browsing window to ensure your changes take effect.

## Data Sources

This project makes use of below external APIs:

- **[Cesium](https://cesium.com/)**: Used for the 3D globe rendering on the client side. Cesium provides an interactive globe platform which can be used to visualize spatial data.
- **[OpenCage](https://opencagedata.com/)**: Utilized for geocoding services. OpenCage offers an API that provides forward and reverse geocoding.
- **[Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)**: Used for fetching detailed information for the server side. The Wikipedia API allows access to various features of Wikipedia content.

