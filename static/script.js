document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.body;
    const editor = document.getElementById("code");
    const suggestionsBox = document.getElementById("suggestions");

    // Load theme from local storage
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        themeToggle.textContent = "☀️ Light Mode";
    } else {
        body.classList.add("light-mode");
        themeToggle.textContent = "🌙 Dark Mode";
    }

    // Toggle dark/light mode
    themeToggle.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        body.classList.toggle("light-mode");
        const theme = body.classList.contains("dark-mode") ? "dark" : "light";
        localStorage.setItem("theme", theme);
        themeToggle.textContent = theme === "dark" ? "☀️ Light Mode" : "🌙 Dark Mode";
    });

    // Submit Code
    window.submitCode = function() {
        let code = editor.value;
        fetch("/process_code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code })
        })
        .then(response => response.json())
        .then(data => {
            // Populate Parser Table
            const tableBody = document.querySelector("#parser-table tbody");
            tableBody.innerHTML = "";
            data.tokens.forEach(token => {
                const row = `<tr><td>${token[0]}</td><td>${token[1]}</td></tr>`;
                tableBody.innerHTML += row;
            });

            // Populate AST Section
            document.getElementById("ast-output").innerText = JSON.stringify(data.ast, null, 2);

            // Populate Suggestions
            document.getElementById("trie-suggestions").innerText = data.trie_suggestions.join(", ");
            document.getElementById("ml-suggestions").innerText = data.ml_suggestions.join(", ");
        });
    };
});
