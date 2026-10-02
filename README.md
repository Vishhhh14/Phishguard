# 🛡️ PhishGuard

### Web-Based Phishing Detection System

**PhishGuard** is a web-based cybersecurity project designed to help users identify potentially suspicious emails and messages.

Users can paste a message into the PhishGuard interface and scan it for common phishing indicators. The system analyzes the message, calculates a risk score, classifies the message, and explains the indicators detected.

> **Detect Phishing Before It Tricks You.**

---

## 🚨 Problem

Phishing attacks often use social engineering techniques to trick users into revealing sensitive information.

Common phishing messages may contain:

* Urgent or threatening language
* Password or OTP requests
* Requests for financial information
* Suspicious links
* Shortened URLs
* Fake authority or support claims
* Attempts to create a sense of urgency

PhishGuard provides a simple first layer of analysis to help users recognize these warning signs.

---

## 💡 How PhishGuard Works

The system follows this process:

```text
User
  ↓
Web Interface
  ↓
JavaScript
  ↓
POST /analyze
  ↓
FastAPI Backend
  ↓
Rule-Based Detection Engine
  ↓
Risk Score + Detection Reasons
  ↓
Result Display
```

The user enters a message and clicks **Scan for Phishing**.

JavaScript sends the message to the Python backend through the `/analyze` API endpoint.

The backend analyzes the message using multiple detection rules and returns the result as JSON.

The frontend then displays the risk level, score, and detected reasons.

---

## 🔍 Detection Features

PhishGuard currently analyzes several phishing indicators.

### 🚨 Urgency & Threat Detection

Detects phrases such as:

* `urgent`
* `act now`
* `immediately`
* `account will be suspended`
* `within 24 hours`

### 🔐 Credential Requests

Detects requests involving:

* Passwords
* OTPs
* Login information
* Verification codes
* Account verification

### 💳 Financial Information

Detects references to:

* Bank accounts
* Credit/debit cards
* Payments
* Transactions
* UPI
* PINs
* Billing information

### 🎁 Suspicious Rewards

Detects suspicious offers involving:

* Prizes
* Rewards
* Free gifts
* Winners
* Limited-time offers

### 🔗 URL Analysis

PhishGuard can detect:

* URLs
* Insecure HTTP links
* Direct IP-address URLs
* Shortened URLs
* Suspicious URL patterns

### 🎭 Impersonation Detection

Looks for possible authority or support claims such as:

* Bank security teams
* IT departments
* Customer support
* Account administrators
* Technical support

---

## 🧠 Combination-Based Detection

PhishGuard does not rely only on individual keywords.

It also checks combinations of indicators that can represent stronger phishing signals.

Examples include:

```text
Urgency + Credential Request
```

```text
Credential Request + Link
```

```text
Financial Request + Link
```

```text
Impersonation + Credential Request
```

These combinations contribute additional points to the overall risk score.

---

## 📊 Risk Classification

The detection engine assigns a score based on the indicators found.

| Score | Classification |
| ----: | -------------- |
|   0–2 | 🟢 SAFE        |
|   3–6 | 🟡 SUSPICIOUS  |
|    7+ | 🔴 PHISHING    |

These thresholds are currently prototype rules and can be calibrated further using larger datasets.

> **Note:** The displayed score is an internal risk score and is not a probability or guaranteed measure of whether a message is malicious.

---

## 💡 Explainable Results

One of the main features of PhishGuard is that it provides reasons for its classification.

Instead of only displaying:

```text
PHISHING
```

the system can explain:

```text
Urgency or threat detected
Credential-related request detected
A link was detected
A credential request was combined with a link
```

This helps users understand **why** a message was flagged.

---

## 🖥️ Technology Stack

| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| HTML       | Webpage structure                    |
| CSS        | Interface and visual design          |
| JavaScript | Frontend logic and API communication |
| Python     | Detection engine                     |
| FastAPI    | Backend API                          |
| Uvicorn    | Development server                   |
| Pydantic   | Request validation                   |
| Regex      | URL and pattern detection            |

---

## 📁 Project Structure

```text
mail-project/
│
├── index.html
│
├── css/
│   └── style.css
│
├── js/
│   └── app.js
│
└── backend/
    └── main.py
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Move into the project directory:

```bash
cd mail-project
```

### 2. Install Python dependencies

```bash
python -m pip install fastapi uvicorn
```

### 3. Start the backend

Run:

```bash
python -m uvicorn backend.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

### 4. Start the frontend

Open the project in **VS Code** and run `index.html` using a local development server such as **Live Server**.

Then open the displayed local frontend address in your browser.

---

## 🧪 Example

Example suspicious message:

```text
URGENT! Your bank account will be suspended.

Verify your password and OTP immediately.

Please login using the link below:

http://example.com
```

PhishGuard analyzes the message and identifies multiple indicators such as:

* Urgency
* Credential requests
* Financial information
* Link detection
* Combined indicators

The result is then displayed on the webpage with the corresponding risk level and reasons.

---

## ⚠️ Limitations

PhishGuard is currently a **rule-based prototype** and should not be considered a complete phishing detection solution.

Current limitations include:

* It may produce false positives.
* Sophisticated phishing messages may bypass the current rules.
* It does not currently analyze sender headers.
* It does not perform SPF/DKIM/DMARC verification.
* It does not perform live URL reputation checks.
* It does not use a machine-learning model.
* It does not guarantee that a message is safe or malicious.

PhishGuard should therefore be considered an **assistive analysis tool**, rather than a replacement for proper cybersecurity controls.

---

## 🚀 Future Improvements

Potential future versions could include:

### 🤖 Machine Learning

Train models using larger datasets containing phishing and legitimate messages.

### 🌐 URL & Domain Reputation

Integrate reputation services to provide additional information about suspicious domains and URLs.

### 📧 Email Authentication Analysis

Add analysis of:

* SPF
* DKIM
* DMARC
* Sender information

### 🧠 Advanced Content Analysis

Analyze:

* HTML email structure
* Hidden links
* More complex phishing patterns
* Additional social-engineering techniques

### 🛡️ Hybrid Detection

A future version could combine:

```text
Rule-Based Detection
        +
Machine Learning
        +
URL/Domain Intelligence
```

---

## 🎯 Project Objective

The goal of PhishGuard is to provide users with a simple and understandable first layer of phishing analysis.

Rather than only giving a classification, PhishGuard attempts to show the **specific indicators behind the result**, making the detection process more transparent and easier to understand.

---

## 👥 Team

**PhishGuard Project Team**

Developed as an interschool cybersecurity project.

---

## 📌 Disclaimer

PhishGuard is an educational cybersecurity project and prototype.

It is not intended to provide guaranteed protection against phishing, malware, fraud, or other cybersecurity threats.

Always verify suspicious messages through trusted channels and avoid entering sensitive information into unknown websites.

---

### 🛡️ PhishGuard

**Detect Phishing Before It Tricks You.**
