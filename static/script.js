const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");
const errorMessage = document.getElementById("error-message");

function addMessage(text, sender) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", `${sender}-message`);

    const paragraph = document.createElement("p");
    paragraph.textContent = text;

    messageDiv.appendChild(paragraph);
    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage(message) {
    const question = message.trim();

    if (!question) {
        return;
    }

    errorMessage.textContent = "";
    addMessage(question, "user");

    userInput.value = "";
    userInput.disabled = true;
    sendButton.disabled = true;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: question
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        addMessage(data.answer, "bot");

    } catch (error) {
        errorMessage.textContent =
            error.message || "Unable to connect. Please try again.";
    } finally {
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

chatForm.addEventListener("submit", function (event) {
    event.preventDefault();
    sendMessage(userInput.value);
});

document.querySelectorAll(".suggestion").forEach(function (button) {
    button.addEventListener("click", function () {
        sendMessage(button.textContent);
    });
});

