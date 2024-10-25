// static/chat.js

function addUserMessage(event) {
    event.preventDefault();
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value.trim();

    if (userMessage === '') return;

    const messagesDiv = document.getElementById('messages');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user-message';
    userMessageDiv.textContent = userMessage;

    messagesDiv.appendChild(userMessageDiv);

    userInput.value = '';

    const typingIndicator = document.getElementById('typing-indicator');
    typingIndicator.style.display = 'flex';

    htmx.ajax('POST', '/ask', {
        target: '#messages',
        swap: 'beforeend',
        values: {
            question: userMessage
        }
    });
}

// Hide typing indicator after the response has been swapped into the page
document.addEventListener("htmx:afterSwap", function(event) {
    if (event.detail.target.id === 'messages') {
        // Hide the typing indicator
        const typingIndicator = document.getElementById('typing-indicator');
        typingIndicator.style.display = 'none';

        // Scroll to the bottom of the messages div
        const messages = document.getElementById("messages");
        messages.scrollTop = messages.scrollHeight;
    }
});

// Hide typing indicator if an error occurs during the request
document.addEventListener("htmx:responseError", function() {
    const typingIndicator = document.getElementById('typing-indicator');
    typingIndicator.style.display = 'none';
});
