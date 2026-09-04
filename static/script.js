let button = document.getElementById("chatbutton");

button.onclick = function () {

    let input = document.getElementById("inputmsg");
    let msg = input.value.toLowerCase().trim();

    if (msg === "") {
        return;
    }

    let chat = document.getElementById("chatarea");

    let newmsg = document.createElement("p");
    newmsg.className = "user-message";
    newmsg.textContent = msg;

    chat.appendChild(newmsg);

    let thinking = document.createElement("p");
    thinking.className = "bot-message";
    thinking.textContent = "🤔 Thinking...";

    chat.appendChild(thinking);

    saveHistory();

    fetch("/chat", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: msg
        })

    })

    .then(function (response) {
        return response.json();
    })

    .then(function (data) {

        setTimeout(function () {

            thinking.textContent = data;

            let time = document.createElement("small");
            time.textContent = new Date().toLocaleTimeString();

            chat.appendChild(time);

            saveHistory();

        }, 800);

    })

    .catch(function () {

        thinking.textContent = "Sorry, something went wrong. 😔";

        saveHistory();

    });

    input.value = "";

};


function saveHistory() {

    let chat = document.getElementById("chatarea");

    localStorage.setItem(
        "paintingChatHistory",
        chat.innerHTML
    );

}


function loadHistory() {

    let chat = document.getElementById("chatarea");

    let savedHistory = localStorage.getItem(
        "paintingChatHistory"
    );

    if (savedHistory) {

        chat.innerHTML = savedHistory;

    }

}


let themebutton = document.getElementById("themebutton");

themebutton.onclick = function () {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {

        themebutton.textContent = "☀️ Light";

        localStorage.setItem("paintingTheme", "dark");

    } else {

        themebutton.textContent = "🌙 Theme";

        localStorage.setItem("paintingTheme", "light");

    }

};


function loadTheme() {

    let savedTheme = localStorage.getItem("paintingTheme");

    if (savedTheme === "dark") {

        document.body.classList.add("dark-mode");

        themebutton.textContent = "☀️ Light";

    } else {

        document.body.classList.remove("dark-mode");

        themebutton.textContent = "🌙 Theme";

    }

}


let historybutton = document.getElementById("historybutton");
let historypanel = document.getElementById("historypanel");
let historycontent = document.getElementById("historycontent");
let closehistory = document.getElementById("closehistory");


historybutton.onclick = function () {

    historycontent.innerHTML = "";

    let messages = document.querySelectorAll(
        "#chatarea .user-message, #chatarea .bot-message"
    );

    messages.forEach(function (message) {

        let historymessage = document.createElement("p");

        historymessage.textContent = message.textContent;

        historycontent.appendChild(historymessage);

    });

    historypanel.style.display = "block";

};


closehistory.onclick = function () {

    historypanel.style.display = "none";

};


loadHistory();
loadTheme();
