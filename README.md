# 🧾 Invoice Generator (Python CLI App)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/nightman19/invoice-generator.svg)

---

## 🌄 Project Overview

![Project Banner](https://raw.githubusercontent.com/nightman19/invoice-generator/main/assets/banner.png)

> *A simple Python CLI tool that helps freelancers and small business owners generate professional PDF invoices instantly.*

If you’d like to create your own banner, you can design one using **Canva**, **Figma**, or **Bannersnack** (recommended size: **1280×640px**) and place it in an `assets/` folder named `banner.png`.

---

## 🚀 Features

✅ Generate clean PDF invoices instantly
✅ Auto-create timestamped filenames for record keeping
✅ Simple command-line interface (no setup hassle)
✅ Organized output folder for all invoices
✅ Built with standard Python libraries + ReportLab

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **ReportLab** (for PDF generation)

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/nightman19/invoice-generator.git
   cd invoice-generator
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Usage

Run the script:

```bash
python main.py
```

Enter your invoice details:

```
Client Name: John Doe
Project Description: Website redesign
Amount ($): 500
```

A new PDF file will be generated inside the `invoices/` folder:

```
invoices/invoice_John Doe_20251106_204648.pdf
```

---

## 🧩 Example Output

Here’s what a generated invoice looks like:

```
INVOICE
Client: John Doe
Project: Website redesign
Date: 2025-11-06
Amount Due: $500

Thank you for your business!
```

---

## 🚧 Future Improvements

* [ ] Add logo and better layout formatting
* [ ] Automatically increment invoice numbers
* [ ] Include tax and currency options
* [ ] Email invoices directly from the CLI
* [ ] Export invoice history to CSV/JSON

---

## 💡 Author

**Nuru Umar Mohammed**
💼 [LinkedIn Profile](https://www.linkedin.com/in/nuru-umar-mohammed)
📂 [GitHub Portfolio](https://github.com/nightman19)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
