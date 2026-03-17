# Halleyx Dashboard — Custom Dashboard Builder

A full-stack web application built with **Django REST Framework** and **Vanilla JS** that allows users to create personalized dashboards by combining various widgets such as Charts, Tables, and KPI cards — all powered by real Customer Order data.

> Built as part of Halleyx Pre-Placement Challenge 2026

---

## 🚀 Features

### 📋 Orders Management
- Create, Edit, Delete customer orders via popup form
- 15-field form with full validation — "Please fill the field" on every mandatory field
- Auto-calculated Total Amount (Quantity × Unit Price)
- Status badges — Pending, In Progress, Completed
- Live search + status filter
- CSV bulk upload with file picker
- Stats row — Total Orders, Completed, Pending, Total Revenue

### ⚙️ Dashboard Configuration
- Select widgets by clicking cards — KPI, Bar Chart, Line Chart, Area Chart, Pie Chart, Scatter Plot, Table
- Per-widget settings — metric, aggregation, axis, color, pagination, font size
- Save configuration → persisted to database → loads on dashboard

### 📊 Dashboard
- Dynamically renders saved widgets with real order data
- KPI cards with Sum / Average / Count aggregation
- 5 chart types — Bar, Line, Area, Scatter, Pie (Doughnut)
- Table widget with live search + status filter
- Date filter — All time, Today, Last 7/30/90 days
- Empty state when no widgets configured

### 🎨 Design
- Dark / Light theme toggle on all pages (persists via localStorage)
- Responsive design — Desktop (12-col), Tablet (8-col), Mobile (4-col)
- Mobile hamburger sidebar navigation
- Toast notifications for all actions
- Loading skeletons

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.x + Django REST Framework |
| Database | MySQL |
| Frontend | Vanilla HTML / CSS / JavaScript |
| Charts | Chart.js |
| Fonts | Plus Jakarta Sans (Google Fonts) |

---

## 📁 Project Structure

```
halleyx-dashboard/
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── orders/
│   ├── models.py          # CustomerOrder, DashboardLayout
│   ├── views.py           # All API endpoints
│   ├── serializers.py
│   ├── admin.py
│   └── urls.py
├── templates/
│   ├── dashboard.html     # Dashboard page
│   ├── orders.html        # Orders page
│   ├── configure.html     # Configure page
│   └── admin/
│       └── base_site.html # Custom admin theme
├── static/
│   └── js/
│       └── dashboard.js
└── manage.py
```

---

## ⚡ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/orders/` | List all orders |
| POST | `/api/orders/create/` | Create new order |
| PUT | `/api/orders/<id>/update/` | Update order |
| DELETE | `/api/orders/<id>/delete/` | Delete order |
| GET | `/api/dashboard/kpi/` | KPI aggregates with date filter |
| GET | `/api/dashboard/product-revenue/` | Revenue by product |
| GET | `/api/dashboard/order-status/` | Orders by status |
| POST | `/api/upload-orders/` | Bulk CSV upload |
| POST | `/api/save-layout/` | Save dashboard config |
| GET | `/api/load-layout/` | Load dashboard config |

All date-filterable endpoints support `?range=today|7|30|90|all`

---

## 🗄️ Data Model

### CustomerOrder
| Field | Type | Notes |
|-------|------|-------|
| first_name, last_name | CharField | — |
| email | EmailField | — |
| phone | CharField | — |
| street_address, city, state, postal_code | CharField | — |
| country | CharField | Choices: US, CA, AU, SG, HK |
| product | CharField | 5 product choices |
| quantity | IntegerField | Min 1 |
| unit_price | DecimalField | 10,2 |
| total_amount | DecimalField | Auto: qty × price |
| status | CharField | pending / in_progress / completed |
| created_by | CharField | 4 staff choices |
| created_at | DateTimeField | Auto |

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.10+
- MySQL
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/halleyx-dashboard.git
cd halleyx-dashboard
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install django djangorestframework mysqlclient
```

**4. Configure database**

Create a MySQL database:
```sql
CREATE DATABASE halleyx_dashboard;
```

Update `backend/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'halleyx_dashboard',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**5. Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Create superuser**
```bash
python manage.py createsuperuser
```

**7. Run server**
```bash
python manage.py runserver
```

**8. Open in browser**
```
http://127.0.0.1:8000/dashboard/     # Dashboard
http://127.0.0.1:8000/orders/        # Orders
http://127.0.0.1:8000/configure/     # Configure
http://127.0.0.1:8000/admin/         # Admin
```

---

## 📊 Sample CSV Format

Use this format for bulk order upload:

```csv
first_name,last_name,email,phone,street_address,city,state,postal_code,country,product,quantity,unit_price,status,created_by
John,Doe,john@example.com,+1555001,123 Main St,New York,NY,10001,US,fiber_300,2,49.99,pending,michael_harris
Jane,Smith,jane@example.com,+1555002,456 Oak Ave,Toronto,ON,M5V,CA,5g_unlimited,1,39.99,completed,ryan_cooper
```

**Valid values:**
- `country` — IND,US, CA, AU, SG, HK
- `product` — fiber_300, 5g_unlimited, fiber_1gb, business_500, voip_corporate
- `status` — pending, in_progress, completed
- `created_by` — michael_harris, ryan_cooper, olivia_carter, lucas_martin

---

## 📱 Responsive Breakpoints

| Device | Columns | Behavior |
|--------|---------|----------|
| Desktop | 12 columns | Full layout |
| Tablet (≤1024px) | 8 columns | Widgets reflow |
| Mobile (≤768px) | 4 columns | Hamburger menu, stacked layout |

---

## 🎨 Theme

Supports **Dark** and **Light** themes:
- Toggle button on every page topbar
- Preference saved in `localStorage`
- Consistent across all pages

---

## 👨‍💻 Developer

**Ramprasad**
Built for Halleyx Pre-Placement Challenge 2026

---

## 📄 License

This project was built as a company challenge submission.

## 🎥 Demo Video

▶️ Watch the full demo on YouTube:
[Click here to watch](https://youtu.be/y6JQEQLILjc)

---