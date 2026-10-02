const emailInput = document.getElementById("emailInput");
const scanButton = document.getElementById("scanButton");
const resultContent = document.getElementById("resultContent");


scanButton.addEventListener("click", async function () {

    const email = emailInput.value.trim();


    if (email === "") {

        resultContent.innerHTML = `
            <p id="resultText">
                Please paste an email or message before scanning.
            </p>
        `;

        return;
    }


    resultContent.innerHTML = `
        <p id="resultText">
            Analyzing message...
        </p>
    `;


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email
                })
            }
        );


        const result = await response.json();


        let resultClass = "";
        let icon = "";
        let subtitle = "";


        if (result.risk === "PHISHING") {

            resultClass = "phishing-result";
            icon = "🔴";
            subtitle = "HIGH RISK";

        } else if (result.risk === "SUSPICIOUS") {

            resultClass = "suspicious-result";
            icon = "🟡";
            subtitle = "REVIEW REQUIRED";

        } else {

            resultClass = "safe-result";
            icon = "🟢";
            subtitle = "LOW RISK";
        }


        const scorePercentage =
            Math.min(result.score * 10, 100);


        let reasonsHTML = "";


        if (result.reasons.length > 0) {

            result.reasons.forEach(function (reason) {

                reasonsHTML += `
                    <div class="reason">
                        ${reason}
                    </div>
                `;

            });

        } else {

            reasonsHTML = `
                <div class="reason">
                    No major phishing indicators detected.
                </div>
            `;
        }


        resultContent.innerHTML = `

            <div class="${resultClass}">

                <div class="result-status">

                    <div class="status-icon">
                        ${icon}
                    </div>

                    <div>

                        <div class="status-text">
                            ${result.risk}
                        </div>

                        <div class="status-subtitle">
                            ${subtitle}
                        </div>

                    </div>

                </div>


                <div class="score-section">

                    <div class="score-label">
                        RISK SCORE
                    </div>

                    <div class="score-value">
                        ${result.score}
                    </div>

                    <div class="score-bar">

                        <div
                            class="score-fill"
                            style="width: ${scorePercentage}%"
                        ></div>

                    </div>

                </div>


                <div class="reasons-title">
                    DETECTION REASONS
                </div>

                ${reasonsHTML}

            </div>
        `;


    } catch (error) {

        resultContent.innerHTML = `
            <p id="resultText">
                Could not connect to the PhishGuard backend.
            </p>
        `;

        console.error(error);
    }

})