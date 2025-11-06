from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_invoice(client_name, project_desc, amount):
    # Ensure invoices folder exists
    os.makedirs("invoices", exist_ok=True)

    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"invoices/invoice_{client_name}_{timestamp}.pdf"

    # Initialize PDF canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "INVOICE")

    # Client Info
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Client: {client_name}")
    c.drawString(50, height - 120, f"Project: {project_desc}")
    c.drawString(50, height - 140, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    # Amount
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 180, f"Amount Due: ${amount}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 50, "Thank you for your business!")

    # Save PDF
    c.save()
    print(f"✅ Invoice saved as: {filename}")


if __name__ == "__main__":
    client = input("Client Name: ")
    project = input("Project Description: ")
    amount = input("Amount ($): ")
    generate_invoice(client, project, amount)