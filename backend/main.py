from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    email: str


@app.get("/")
def home():
    return {
        "message": "PhishGuard backend is running!"
    }


@app.post("/analyze")
def analyze(request: EmailRequest):

    email = request.email.lower()

    score = 0
    reasons = []


    # ==============================
    # 1. URGENCY / THREAT LANGUAGE
    # ==============================

    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "action required",
        "last warning",
        "final warning",
        "account will be suspended",
        "account suspended",
        "within 24 hours",
        "within 48 hours",
        "respond immediately"
    ]

    for word in urgency_words:

        if word in email:

            score += 1

            reasons.append(
                f"Urgency or threat detected: '{word}'"
            )


    # ==============================
    # 2. CREDENTIAL REQUESTS
    # ==============================

    credential_words = [
        "password",
        "verify your account",
        "verify your identity",
        "confirm your password",
        "confirm your identity",
        "login",
        "log in",
        "otp",
        "one time password",
        "one-time password",
        "security code",
        "verification code"
    ]

    for word in credential_words:

        if word in email:

            score += 2

            reasons.append(
                f"Credential-related request detected: '{word}'"
            )


    # ==============================
    # 3. FINANCIAL INFORMATION
    # ==============================

    financial_words = [
        "credit card",
        "debit card",
        "bank account",
        "bank details",
        "account number",
        "card number",
        "payment",
        "refund",
        "transaction",
        "billing information",
        "upi",
        "pin"
    ]

    for word in financial_words:

        if word in email:

            score += 2

            reasons.append(
                f"Financial information request detected: '{word}'"
            )


    # ==============================
    # 4. SUSPICIOUS REWARDS / OFFERS
    # ==============================

    reward_words = [
        "you have won",
        "you won",
        "winner",
        "claim your prize",
        "claim your reward",
        "free gift",
        "congratulations",
        "limited time offer"
    ]

    for word in reward_words:

        if word in email:

            score += 2

            reasons.append(
                f"Suspicious reward or offer detected: '{word}'"
            )


    # ==============================
    # 5. SUSPICIOUS LINKS
    # ==============================

    urls = re.findall(
        r"https?://\S+|www\.\S+",
        email
    )

    if urls:

        score += 2

        reasons.append(
            "A link was detected in the message."
        )


    # ==============================
    # 6. INSECURE HTTP LINKS
    # ==============================

    http_urls = re.findall(
        r"http://\S+",
        email
    )

    if http_urls:

        score += 2

        reasons.append(
            "An insecure HTTP link was detected."
        )


    # ==============================
    # 7. IP-ADDRESS LINKS
    # ==============================

    ip_urls = re.findall(
        r"https?://(?:\d{1,3}\.){3}\d{1,3}",
        email
    )

    if ip_urls:

        score += 2

        reasons.append(
            "A link using a direct IP address was detected."
        )


    # ==============================
    # 8. SHORTENED LINKS
    # ==============================

    shortened_domains = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "goo.gl",
        "is.gd",
        "cutt.ly"
    ]

    for domain in shortened_domains:

        if domain in email:

            score += 2

            reasons.append(
                f"Shortened URL detected: '{domain}'"
            )


    # ==============================
    # 9. SUSPICIOUS URL CHARACTERISTICS
    # ==============================

    suspicious_url_patterns = [
        "verify-",
        "secure-",
        "account-",
        "login-",
        "-verify",
        "-secure",
        "-login"
    ]

    for pattern in suspicious_url_patterns:

        if pattern in email:

            score += 1

            reasons.append(
                f"Suspicious URL pattern detected: '{pattern}'"
            )


    # ==============================
    # 10. IMPERSONATION / AUTHORITY
    # ==============================

    impersonation_words = [
        "security team",
        "support team",
        "customer service",
        "account administrator",
        "it department",
        "bank security",
        "security department",
        "account support",
        "technical support"
    ]

    for word in impersonation_words:

        if word in email:

            score += 1

            reasons.append(
                f"Possible impersonation or authority claim detected: '{word}'"
            )


    # ==============================
    # 11. COMBINATION OF INDICATORS
    # ==============================

    has_urgency = any(
        word in email for word in urgency_words
    )

    has_credentials = any(
        word in email for word in credential_words
    )

    has_financial = any(
        word in email for word in financial_words
    )

    has_impersonation = any(
        word in email for word in impersonation_words
    )

    has_url = len(urls) > 0


    if has_urgency and has_credentials:

        score += 2

        reasons.append(
            "Urgency combined with a credential request."
        )


    if has_credentials and has_url:

        score += 2

        reasons.append(
            "A credential request was combined with a link."
        )


    if has_financial and has_url:

        score += 2

        reasons.append(
            "A financial request was combined with a link."
        )


    if has_impersonation and has_credentials:

        score += 2

        reasons.append(
            "An authority claim was combined with a credential request."
        )


    # ==============================
    # 12. DETERMINE RISK LEVEL
    # ==============================

    if score >= 7:

        risk = "PHISHING"

    elif score >= 3:

        risk = "SUSPICIOUS"

    else:

        risk = "SAFE"


    return {
        "risk": risk,
        "score": score,
        "reasons": reasons,
        "message": f"Risk level: {risk}"
    }