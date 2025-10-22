
# Phishing Email Analysis – Task 2

## 1. Summary
A suspicious email claiming to be from PayPal was analyzed.  
It urges the user to “verify your account” and leads to a fake login site.  
Header analysis shows spoofed sender information and failed SPF/DKIM/DMARC checks.

---

## 2. Email Artifacts
| File | Description |
|------|--------------|
| sample_email.txt | Raw email body |
| headers.txt | Original headers |
| urls.txt | URLs extracted with `extract_urls.py` |
| screenshots/ | Evidence screenshots |

---

## 3. Header Analysis
**Key Results (from MXToolbox):**
- SPF → **Fail**
- DKIM → **Not Found**
- DMARC → **Fail**
- `Received` path includes `mail.fakehost.com` (not paypal.com)
- Return-Path domain differs from displayed domain.

🖼 Screenshot: `screenshots/screenshot_header_analysis.png`

---

## 4. Body and Link Inspection
Extracted URL (from `urls.txt`):  
`https://paypal.com.verify-account-security-update.com/login`

**Observed issues**
- Domain `verify-account-security-update.com` ≠ `paypal.com`
- Generic greeting “Dear Customer”
- Urgent language: “Failure to verify within 24 hours …”
- Threat of account suspension → social engineering.

🖼 Screenshots: `screenshots/screenshot_sample_email.png`, `screenshots/screenshot_urls_txt.png`, `screenshots/screenshot_link_hover.png`

---

## 5. Phishing Indicators
| # | Indicator | Evidence |
|--|--|--|
| 1 | Mismatched domain | Displayed vs actual link |
| 2 | SPF/DKIM/DMARC fail | Header analysis |
| 3 | Generic greeting | “Dear Customer” |
| 4 | Urgency + threat | Suspension warning |
| 5 | Suspicious Return-Path | security@paypal-update.com |

---

## 6. Recommendations
- Do not click links or download attachments.  
- Report email as phishing to your email provider.  
- Contact PayPal via official website only.  
- Block sender domain and enable 2FA on accounts.  

---

## 7. Tools Used
- MXToolbox Email Header Analyzer  
- Python `extract_urls.py` script  
- Notepad / VS Code for inspection  

---

## 8. Interview Q&A
1. **What is phishing?** Fraudulent emails that trick users into sharing credentials or money.  
2. **How to identify phishing emails?** Mismatched links, fake domains, urgent tone, errors.  
3. **What is email spoofing?** Forging the sender address to look legitimate.  
4. **Why are phishing emails dangerous?** They steal data and install malware.  
5. **How to verify sender authenticity?** Check SPF/DKIM/DMARC and domain names.  
6. **Tools to analyze headers?** MXToolbox, Google Message Header Analyzer.  
7. **What to do if you get one?** Don’t click; report and delete.  
8. **How do attackers use social engineering?** They exploit fear and urgency to trick users.  
