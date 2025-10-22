
# 🕵️‍♀️ Phishing Email Analysis — Task 2  
### Cyber Security Internship Project  

This project demonstrates how to identify and analyze a **phishing email** using simple tools and investigative methods.  
It was created as part of my cybersecurity internship to build awareness of **email spoofing, header analysis, and social engineering tactics**.

---

## 🎯 Objective
Analyze a suspicious email and identify key phishing indicators — such as spoofed sender addresses, mismatched URLs, failed authentication (SPF/DKIM/DMARC), and psychological manipulation in the email body.

---

## 🧰 Tools & Resources Used
| Tool | Purpose |
|------|----------|
| **Python (`extract_urls.py`)** | To extract URLs from the phishing email |
| **MXToolbox Email Header Analyzer** | To check SPF, DKIM, and DMARC authentication |
| **Notepad / VS Code** | For inspecting raw email text and writing the report |
| **Git & GitHub** | For version control and submission |

---

## 📂 Repository Structure
Phishing-Email-Analysis/
├── README.md # Project overview (this file)
├── sample_email.txt # Raw phishing email sample
├── headers.txt # Extracted email headers
├── urls.txt # URLs extracted from the email
├── analysis.md # Detailed phishing analysis report
├── scripts/
│ └── extract_urls.py # Python script to extract URLs
└── screenshots/
├── screenshot_sample_email.png
├── screenshot_urls_txt.png
├── screenshot_header_analysis.png


---

## 🧠 Summary of Findings
- **Sender domain spoofed:** `security@paypal-update.com` (not an official PayPal domain)  
- **SPF/DKIM/DMARC:** All failed — confirms email not sent from authorized PayPal servers  
- **URL mismatch:**  
  Displayed: `https://paypal.com.verify-account-security-update.com/login`  
  Actual domain: `verify-account-security-update.com`  
- **Urgent language:** “Verify within 24 hours or account will be suspended”  
- **Generic greeting:** “Dear Customer” → common in phishing attempts  

🟡 *Conclusion:* This email is a **phishing attempt** designed to steal user credentials through a fake login page.

---

## 📸 Screenshots
- `screenshots/screenshot_sample_email.png` — Raw email content  
- `screenshots/screenshot_urls_txt.png` — Extracted URLs  
- `screenshots/screenshot_header_analysis.png` — MXToolbox results (SPF/DKIM/DMARC failed)

---

## 🛡️ Key Takeaways
- Always check **email headers** for authentication results.  
- Be suspicious of **links that don’t match the sender’s domain**.  
- Phishing emails often use **urgency, fear, or reward-based language**.  
- Verify the sender through official channels before taking any action.

---

## 🧩 Learning Outcome
By completing this task, I learned:
- How to read and interpret raw email headers  
- How SPF, DKIM, and DMARC mechanisms work  
- How attackers use **social engineering** to trick users  
- How to document and report phishing incidents effectively  

---

## 📝 Submission Info
This repository is the final deliverable for **Cyber Security Internship – Task 2**:  
**Phishing Email Analysis**  
> Submission Link: [https://forms.gle/8Gm83s53KbyXs3Ne9](https://forms.gle/8Gm83s53KbyXs3Ne9)

---

## 💡 Author
**Animesh Goud**  
Cyber Security Intern | GitHub: [@axnimesh](https://github.com/axnimesh)  
📧 *Focused on practical cybersecurity, awareness, and digital safety.*
