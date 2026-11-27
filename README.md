
# Odoo 19 — Real Estate Management

<p align="center">
  <strong>A custom Real Estate application module built with the Odoo 19 framework.</strong>
  <br>
  Manage property records, track offers, calculate property metrics, and control property status from the Odoo interface.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Odoo-19.0-714B67?logo=odoo&logoColor=white" alt="Odoo 19">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Odoo%20Addon-714B67" alt="Odoo addon">
  <img src="https://img.shields.io/badge/Repository-Public-2DA44E?logo=github&logoColor=white" alt="Public repository">
</p>

---

## Overview

**Odoo 19 Real Estate** is a custom Odoo addon that introduces property and property-offer records to an Odoo database.

It provides property list and form views, links offers to properties and contacts, computes useful property values, and includes actions for selling or cancelling a property.

The module is maintained in the `estate/` directory and is intended to be added to an existing Odoo 19 installation as a custom addon.

## Features

| Feature                | Description                                                                      |
| ---------------------- | -------------------------------------------------------------------------------- |
| Property Management    | Create and manage property records, descriptions, availability dates and prices. |
| Property Offers        | Record offers and associate them with properties and contacts.                   |
| Best Offer Calculation | Automatically calculate the highest offer associated with a property.            |
| Total Area Calculation | Calculate total area using living area and garden area.                          |
| Property Status        | Track New, Offer Received, Offer Accepted, Sold and Cancelled states.            |
| Property Actions       | Sell and Cancel actions with validation.                                         |
| Data Integrity         | Enforce unique property names and positive expected prices.                      |
| Access Control         | Provide internal users with read, write, create and delete permissions.          |

## Technology Stack

- **Odoo 19** — ERP framework and application platform.
- **Python** — Business models, computed fields and server-side actions.
- **XML** — Odoo views, actions and menu definitions.
- **CSV** — Model access-control declarations.
- **PostgreSQL** — Database backend used by Odoo.

## Project Structure

```text
Odoo-19-Real-Estate-Assignment/
│
├── estate/
│   │
│   ├── __init__.py
│   ├── __manifest__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── estate_property.py
│   │   └── estate_property_offer.py
│   │
│   ├── security/
│   │   └── ir.model.access.csv
│   │
│   └── views/
│       ├── estate_menus.xml
│       ├── estate_property_views.xml
│       ├── estate_property_offer_views.xml
│       ├── estate_property_tag_views.xml
│       ├── estate_property_type_views.xml
│       └── res_users_views.xml
│
├── .gitignore
└── README.md
```

## Requirements

- A working Odoo 19 installation.
- Python and PostgreSQL versions supported by that Odoo installation.
- Access to an Odoo database.
- An Odoo user with permission to install applications or modules.

> This repository contains the custom `estate` addon, not the complete Odoo server or PostgreSQL database. Odoo must be installed and configured separately.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/M-Abdul-Kareem/Odoo-19-Real-Estate-Assignment.git
```

### 2. Configure the Addons Path

Odoo's `addons_path` must include the parent directory containing the `estate` folder, not the `estate` folder itself.

For example, if the repository is located at:

```text
D:\Projects\Odoo-19-Real-Estate-Assignment\
    └── estate\
```

Add the repository directory to the existing `addons_path` in your Odoo configuration:

```ini
addons_path = <your-existing-Odoo-addons-path>,D:\Projects\Odoo-19-Real-Estate-Assignment
```

Keep your existing standard Odoo addons paths. Adapt this example to your own installation.

### 3. Start Odoo

1. Start your Odoo 19 server using your configured Odoo environment.
2. Open the Odoo web interface.
3. Sign in to your database.
4. Navigate to the **Apps** menu.
5. Update the Apps list if the Real Estate module is not visible.
6. Search for **Real Estate**.

### 4. Install the Module

Locate the Real Estate application and install it.

After installation, open the Real Estate menu and navigate to Properties.

## Data Models

### 1. Estate Property (`estate.property`)

The property model includes:

- Property name and description.
- Availability date.
- Expected and selling prices.
- Number of bedrooms.
- Living area.
- Garden availability.
- Garden area.
- Related property offers.
- Computed best offer.
- Computed total area.
- Property status.
- Buyer relationship.
- Property manager relationship.

### 2. Estate Property Offer (`estate.property.offer`)

The offer model includes:

- Offer price.
- Related property.
- Related customer/contact (`res.partner`).

## Business Rules and Validations

The implementation contains the following business rules:

1. Property names are required.
2. Property names must be unique.
3. Expected property prices must be greater than zero.
4. Best offer is calculated from the prices of related offers.
5. When no offers exist, the best offer is zero.
6. Total area is calculated as living area plus garden area.
7. Cancelled properties cannot be sold.
8. Sold properties cannot be cancelled.

## Property Lifecycle

The property model defines five states:

| State          | Description                                    |
| -------------- | ---------------------------------------------- |
| New            | Newly created property.                        |
| Offer Received | Property has entered the offer-received stage. |
| Offer Accepted | An offer has been accepted.                    |
| Sold           | Property has been sold.                        |
| Cancelled      | Property has been cancelled.                   |

## Development Notes

When modifying the module:

1. Make changes inside the `estate/` directory.
2. Restart Odoo when necessary after Python or server-side changes.
3. Upgrade the Real Estate module to apply model, view or security changes.
4. Test property creation, offer entry and computed values.
5. Verify the Sell and Cancel operations.
6. Commit and push verified changes to GitHub.

## Current Implementation Notes

Some additional XML files for property types, property tags and user form inheritance are present in the repository.

However, these files are not currently included in the module manifest's data-loading list. Therefore, their presence in the repository does not mean their corresponding functionality is currently loaded into Odoo.

The active property and offer functionality documented above is based on the models and views currently loaded by the manifest.

---

## Repository

**GitHub Repository:**

[Odoo-19-Real-Estate-Assignment](https://github.com/M-Abdul-Kareem/Odoo-19-Real-Estate-Assignment)

<p align="center">
  <strong>Odoo 19 Real Estate Management</strong>
  <br>
  <sub>Custom Odoo addon · Python · XML · PostgreSQL</sub>
</p>
