document.addEventListener('DOMContentLoaded', function () {
  const greetingButton = document.getElementById('greetButton');

  greetingButton.addEventListener('click', () => {
    // Send a message to the background script
    chrome.runtime.sendMessage({ type: 'GREETING', greeting: 'Hello, background!' }, (response) => {
      if (chrome.runtime.lastError) {
        console.error('Error:', chrome.runtime.lastError);
        alert('Error communicating with background script');
        return;
      }
      // Display an alert with the response message
      alert('Response from background: ' + response.response);
    });
  });
});
