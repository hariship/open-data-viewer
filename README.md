# Open data viewer

This project demonstrates how to set up a Cesium globe with an access token using HTML and JavaScript. The access token is kept in a separate configuration file for security and flexibility.

## Getting Started

Follow these steps to set up and run the project:

1. Clone or download this repository to your local machine.

2. Open the project directory in your code editor.

3. Create a `config.js` file in the project root directory and add your Cesium access token.

```javascript
let cesiumAccessToken='your token here'
```

4. Make sure you have Node.js installed on your machine. If not, you can download it from [the official website](https://nodejs.org/). Execute belwo command to install http-server globally

```javascript
npm install -g http-server
```

5. Open your terminal/command prompt and navigate to the project directory.

6. Start the server by running:

```javascript
http-server
```

7. Open your web browser and go to `http://121.0.0.1:8080` to see the Cesium globe with your access token in action.

## Usage

- The globe allows you to click on it to add pins at specific locations.
- Hovering over a pin displays information about the location.
- You can customize the pins, appearance, and functionality as needed in the JavaScript code.

## Configuration

- The access token is stored in the `config.js` file for security. You can create your own in the home directory and access it.

## Troubleshooting

- If you encounter issues, clear your browser cache or use an incognito/private browsing window to ensure your changes take effect.

## Credits

This project is built using [Cesium](https://cesium.com/) for the 3D globe rendering.

