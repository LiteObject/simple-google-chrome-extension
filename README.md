# A Simple Google Chrome Extension

Here's an example of a small Google Chrome extension that displays a "Hello, World!" message when the extension icon is clicked.

### 1. Create a project folder

A new folder for your extension and name it "HelloWorldExtension".

### 2. Add a `manifest.json` file

Inside the root folder, create a new file named `manifest.json` and add the following content:

```json
{
  "manifest_version": 3,
  "name": "Hello Extension",
  "version": "1.0",
  "description": "A simple Hello World! extension",
  "icons": {
      "16": "icon.png",
      "48": "icon.png",
      "128": "icon.png"
  },
  "action": {
      "default_title": "Read text",
      "default_icon": {
          "16": "icon.png",
          "48": "icon.png",
          "128": "icon.png"
      },
      "default_popup": "popup.html"
  },
  "permissions": ["activeTab", "scripting"],
  "background": {
      "service_worker": "background.js"
  }
}

```
### 3. Add a `background.js` file.
In Chrome extensions, a background script is a central part of an extension’s architecture. It runs in the background and can handle events, perform tasks in the background, and manage the extension’s state.

With Manifest V3, background scripts have been replaced by service workers, which are more efficient because they don’t run continuously but can be woken up by events.

Example of `background.js` as a Service Worker in Manifest V3:

```javascript
// background.js

// Listen for messages from other parts of the extension (e.g., popup or content scripts)
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type === 'GREETING') {
        console.log('Received greeting:', message.greeting);
        sendResponse({ response: 'Hello from the background script!' });
    }
});

// Example of handling an event
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.active) {
        console.log('Tab updated:', tab);
    }
});

```
#### When to Use a Background Script/Service Worker
- **Event handling**: Listening for events that occur in the browser (e.g., tab updates, browser actions).
- **Persistent state**: Maintaining state or data that should persist between different parts of the extension.
- **Communication**: Facilitating communication between different parts of the extension (e.g., content scripts, popup scripts).

### 4. Create a new file named "popup.js" and add the following content:

```javascript
document.addEventListener('DOMContentLoaded', function () {
    const greetingButton = document.getElementById('greetButton');

    greetingButton.addEventListener('click', () => {
        chrome.runtime.sendMessage({ type: 'GREETING', greeting: 'Hello, background!' }, (response) => {
            console.log('Response from background:', response.response);
        });
    });
});

```

### 5. Create a new file named `popup.html` and add the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Popup</title>
    <script src="popup.js"></script>
</head>
<body>
    <button id="greetButton">Send Greeting</button>
</body>
</html>

```

### 5. Place an image file named "icon.png" (preferably 16x16 pixels) in the root folder.

### 6. Open Google Chrome and navigate to [chrome://extensions](chrome://extensions/).

### 7. Enable _Developer mode_ by toggling the switch in the top right corner.

### 8. Click on _Load unpacked_ and select the "HelloWorldExtension" folder.

### 9. The extension should now appear in the list of installed extensions. You can click on the extension icon to see the "Hello, World!" message and clicking on the message will display an alert saying "Hello, World!".

That's it! You've created a basic Google Chrome extension. Feel free to modify the code and experiment with different functionalities. Remember to reload the extension on the chrome://extensions page whenever you make changes to the code.