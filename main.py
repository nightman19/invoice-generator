from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle, Spacer, Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# =========================================
# Helper: Build Services Table
# =========================================



def collect_services():
    services = []

    while True:
        add_service = input("Add a service? (y/n): ").strip().lower()
        if add_service != "y":
            break

        title = input("Service title: ")
        description = input("Service description: ")
        amount = float(input("Amount (GHS): "))

        services.append({
            "title": title,
            "description": description,
            "amount": amount,
        })

    return services


def build_services_table(services):
    """
    Build a tabular invoice section for services.
    Columns:
        # | Service | Description | Amount
    """
    # Table header
    table_data = [
        ['#', "Service", "Description", "Amount (GHS)"]
    ]
    
    total = 0
    for idx, service in enumerate(services, start=1):
        table_data.append([
            str(idx),
            service["title"],
            service["description"],
            f'{service["amount"]:.2f}'
        ])
        total += service["amount"]

    table_data.append(["", "Total", "", f"{total:.2f}"])

    table = Table(
        table_data,
        colWidths=[30, 120, 250, 80]
    )

    table.setStyle(TableStyle({
        ("GRID", (0, 0), (-1, 1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("SPAN", (0, -1), (2, -1)),
        ("BACKGROUND", (0, -1), (-1, -1), colors.whitesmoke), 
    }))

    return table, total

# ==============================================================
# Main Invoice Generator
# ==============================================================
# def generate_invoice(invoice_no, invoice_date, due_date, services):
def generate_invoice(client_name, services):
    os.makedirs("invoices", exist_ok=True)

    # Create filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"invoices/invoice_{client_name.replace(' ', '-')}_{timestamp}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("<b>INVOICE</b>", styles["title"]))
    elements.append(Spacer(1, 12))
    
    # Client Info
    elements.append(Paragraph(f"<b>BILL TO:</b> {client_name}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Services Table
    services_table, total = build_services_table(services)
    elements.append(services_table)
    elements.append(Spacer(1, 20))

    # Footer
    elements.append(Paragraph(
        f"<b>Total Due:</b> GHS {total:.2f}", styles["Normal"]
    ))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(
        "Thank you for doing business with us.", styles["Italic"]
    ))

    # Save PDF
    doc.build(elements)

    print(f"✅ Invoice saved as: {filename}")


# ==========================================================================
# CLI Entry Point
# ==========================================================================
if __name__ == "__main__":
    client_name = input("Client Name: ")

    services = []
    while True:
        title = input("Service (leave empty to finish): ")

        if not title:
            break
        
        description = input("Description: ")
        amount = float(input("Amount (GHS): "))
        services.append({
            "title": title,
            "description": description,
            "amount": amount,
        })

    generate_invoice(client_name, services)