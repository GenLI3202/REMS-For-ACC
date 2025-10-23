# REMS Preview & User Guide for ACC Cycling Club Management

## 📖 Table of Contents
1. [What is REMS?](#what-is-rems)
2. [Core Features Overview](#core-features-overview)
3. [Technology Stack](#technology-stack)
4. [Getting Started Guide](#getting-started-guide)
5. [Adapting REMS for Your Cycling Club](#adapting-rems-for-your-cycling-club)
6. [Development Workflow](#development-workflow)
7. [Key Areas for Customization](#key-areas-for-customization)
8. [Best Practices](#best-practices)

---

## 🎯 What is REMS?

**REMS (Resources and Event Management System)** is a comprehensive web application built with Python Flask that helps clubs and small organizations manage their events, members, and communications. Originally developed for academic organizations, it's perfect for managing cycling clubs like ACC.

### Why REMS for a Cycling Club?

- ✅ **Event Registration**: Create custom forms for rides, races, and cycling events
- ✅ **Certificate Distribution**: Generate and distribute achievement certificates (e.g., race completions, milestones)
- ✅ **Member Communication**: Bulk email capabilities for newsletters and event announcements
- ✅ **Database Management**: Track members, events, and participation records
- ✅ **Link Shortening**: Create short URLs for event registration and announcements
- ✅ **User Profiles**: Member profiles with authentication

---

## 🚀 Core Features Overview

### 1. **Certificate Generation & Distribution System (CGDS)**
- **What it does**: Automatically generates certificates from templates and CSV data
- **For ACC**: Perfect for race completion certificates, achievement awards, membership certificates
- **How it works**: Upload a certificate template (image), provide a CSV with participant data, and generate personalized certificates
- **Public access**: Members can search and download their certificates

### 2. **Form Generation System**
- **What it does**: Create custom registration forms with field validation
- **For ACC**: Event registrations, membership sign-ups, ride waivers, skill level assessments
- **Features**: 
  - Markdown support for instructions
  - Multiple field types (text, email, number, date, etc.)
  - Automatic database table creation for responses
  - CSV export of all responses

### 3. **Bulk Mailing System**
- **What it does**: Send HTML emails to mailing lists
- **For ACC**: Weekly ride announcements, newsletters, event reminders, safety updates
- **Features**:
  - HTML email templates with customization
  - Upload CSV of recipients
  - Track sent emails in database

### 4. **Database Management**
- **What it does**: Browse, insert, update, and delete records across all databases
- **For ACC**: Manage member records, event history, attendance tracking
- **Features**: Web-based interface to view and modify any table

### 5. **User Authentication & Profiles**
- **What it does**: Secure login system with user profiles
- **For ACC**: Member accounts, admin roles, profile pictures
- **Security**: Password hashing, session management, role-based access

### 6. **Link Shortener**
- **What it does**: Create short URLs using short.io API
- **For ACC**: Share registration links, event details, Strava routes

### 7. **Activity Logging**
- **What it does**: Tracks all user actions in the system
- **For ACC**: Audit trail of registrations, certificate downloads, email sends

---

## 🛠️ Technology Stack

### Backend
- **Python 3.13+** with Flask web framework
- **SQLAlchemy**: Database ORM (supports MySQL, PostgreSQL, SQLite)
- **Pydantic**: Data validation
- **Alembic**: Database migrations
- **Pillow**: Image processing for certificates
- **Loguru**: Logging system

### Frontend
- **Bootstrap 5**: Responsive UI framework
- **Jinja2**: Template engine
- **SB Admin 2 theme**: Professional admin interface
- **FontAwesome**: Icons

### Deployment
- **Docker & Docker Compose**: Containerized deployment
- **MariaDB/MySQL**: Production database (SQLite for development)

---

## 🏁 Getting Started Guide

### Step 1: Environment Setup

You've already completed:
✅ Cloned the repository
✅ Created `acc-rems` branch

### Step 2: Install Dependencies

**Option A: Using Docker (Recommended)**
```bash
cd H:\TUM-PC\TUM_CEM_PhD\REMS_ACC\REMS-For-ACC
docker-compose up -d
```

**Option B: Manual Installation**
```powershell
# Install Python dependencies
cd H:\TUM-PC\TUM_CEM_PhD\REMS_ACC\REMS-For-ACC
pip install -r requirements.txt

# Or using Poetry
poetry install
```

### Step 3: Configure Database

```powershell
# For development (SQLite)
$env:MAIN_DB_URI="sqlite:///H:/TUM-PC/TUM_CEM_PhD/REMS_ACC/REMS-For-ACC/acc_rems.db"

# For production (MySQL)
$env:MAIN_DB_URI="mysql+pymysql://username:password@localhost/acc_rems_db"
```

### Step 4: Initialize Database

```powershell
# Run database migrations
alembic upgrade head
```

### Step 5: Run the Application

```powershell
# Development mode
flask --app src.app run

# Production mode (with Gunicorn)
gunicorn -w 4 -b 0.0.0.0:5000 "src.app:create_app()"
```

### Step 6: First Login

1. Navigate to `http://localhost:5000`
2. Default credentials:
   - **Username**: `admin`
   - **Password**: `admin`
3. ⚠️ **IMPORTANT**: Change these credentials immediately in Settings!

---

## 🚴 Adapting REMS for Your Cycling Club

### Phase 1: Branding & Theme (Week 1)

#### 1.1 Update Organization Name
**Files to modify:**
- `src/app/templates/partials/navigation.html` - Update sidebar logo and title
- `src/app/templates/dashboard.html` - Welcome messages
- `README.md` - Update documentation

**Example changes:**
```html
<!-- Before -->
<span class="navbar-brand">REMS</span>

<!-- After -->
<span class="navbar-brand">ACC Cycling Club</span>
```

#### 1.2 Customize Logo & Colors
**Files to modify:**
- `src/app/static/assets/img/` - Add ACC logo
- `src/app/static/assets/css/custom.css` - Brand colors

**Create custom CSS:**
```css
/* acc_custom.css */
:root {
  --acc-primary: #E30613;  /* ACC Red */
  --acc-secondary: #000000;  /* Black */
  --acc-accent: #FFFFFF;  /* White */
}

.navbar-brand {
  color: var(--acc-primary) !important;
}
```

#### 1.3 Update Landing Page
**File**: `public/index.html` or create new landing page
- Add information about ACC
- Link to membership registration
- Display upcoming rides/events

### Phase 2: Cycling-Specific Features (Week 2-3)

#### 2.1 Create Cycling Event Forms
Navigate to Forms section and create:
- **Weekly Ride Registration**
  - Fields: Name, Email, Skill Level, Bike Type, Emergency Contact
- **Race Registration**
  - Fields: Name, Age Category, Race Category, UCI License Number
- **Membership Application**
  - Fields: Personal info, Bike details, Insurance info, Medical conditions

#### 2.2 Design Certificate Templates
Create certificate templates for:
- Race completion certificates
- Milestone achievements (100km, 500km, 1000km clubs)
- Annual membership certificates
- Safety course completion

**Certificate Template Tips:**
- Use Pillow-compatible fonts (install in `members/fonts/`)
- Design template images (1920x1080 recommended)
- Mark text positions in your template design
- Store templates in `members/certificates/`

### Phase 3: Member Database (Week 3-4)

#### 3.1 Extend Member Model
**File**: `src/app/models.py`

Add cycling-specific fields:
```python
class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    
    # Cycling-specific fields
    bike_type = db.Column(db.String(100))  # Road, Mountain, Gravel, etc.
    skill_level = db.Column(db.String(50))  # Beginner, Intermediate, Advanced
    uci_license = db.Column(db.String(50))
    emergency_contact = db.Column(db.String(255))
    emergency_phone = db.Column(db.String(50))
    medical_conditions = db.Column(db.Text)
    membership_expiry = db.Column(db.Date)
    total_rides = db.Column(db.Integer, default=0)
    total_distance = db.Column(db.Float, default=0.0)
```

#### 3.2 Create Migration
```powershell
alembic revision --autogenerate -m "Add cycling fields to members"
alembic upgrade head
```

### Phase 4: Custom Routes for Cycling (Week 4-5)

#### 4.1 Create Rides Module
**New file**: `src/app/routes/rides.py`

```python
from flask import Blueprint, render_template, request
from src.app.models import db

rides_bp = Blueprint('rides', __name__, url_prefix='/rides')

@rides_bp.route('/')
def list_rides():
    """Display all upcoming rides"""
    # Query rides from database
    return render_template('rides/list.html')

@rides_bp.route('/create', methods=['GET', 'POST'])
def create_ride():
    """Create a new ride event"""
    # Form to create rides
    return render_template('rides/create.html')

@rides_bp.route('/<int:ride_id>/register')
def register_for_ride(ride_id):
    """Register for a specific ride"""
    # Registration logic
    return render_template('rides/register.html')
```

#### 4.2 Register Blueprint
**File**: `src/app/__init__.py`

```python
from src.app.routes.rides import rides_bp
app.register_blueprint(rides_bp)
```

### Phase 5: Email Templates (Week 5)

#### 5.1 Create Cycling Email Templates
**Directory**: `src/app/templates/emails/`

Create templates for:
- `weekly_ride_announcement.html`
- `event_reminder.html`
- `membership_renewal.html`
- `safety_alert.html`

**Example template:**
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .header { background: #E30613; color: white; padding: 20px; }
        .content { padding: 20px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>ACC Weekly Ride</h1>
    </div>
    <div class="content">
        <h2>This Weekend's Ride</h2>
        <p><strong>Date:</strong> {{ ride_date }}</p>
        <p><strong>Distance:</strong> {{ distance }}km</p>
        <p><strong>Pace:</strong> {{ pace }}</p>
        <p><strong>Meeting Point:</strong> {{ location }}</p>
    </div>
</body>
</html>
```

---

## 💻 Development Workflow

### Daily Development Process

1. **Pull Latest Changes**
```powershell
git pull origin acc-rems
```

2. **Create Feature Branch**
```powershell
git checkout -b feature/ride-registration
```

3. **Make Changes**
- Edit files in `src/app/`
- Test locally with `flask --app src.app run`

4. **Test Your Changes**
```powershell
# Run the app
flask --app src.app run

# Visit http://localhost:5000
# Test the feature manually
```

5. **Commit Changes**
```powershell
git add .
git commit -m "Add ride registration feature"
```

6. **Push to Branch**
```powershell
git push origin feature/ride-registration
```

7. **Merge to acc-rems**
```powershell
git checkout acc-rems
git merge feature/ride-registration
git push origin acc-rems
```

### Code Organization Best Practices

1. **One feature = One route file**
   - Keep related functionality together
   - Example: All ride-related routes in `rides.py`

2. **Reuse templates**
   - Create base templates in `src/app/templates/base/`
   - Extend base templates for consistency

3. **Use utility functions**
   - Add helpers to `src/app/utils/helpers.py`
   - Keep routes clean and readable

4. **Log everything**
   - Use `from src.app.utils.logger import logger`
   - Log important actions: `logger.info(f"User {user_id} registered for ride {ride_id}")`

---

## 🎨 Key Areas for Customization

### 1. Navigation Menu
**File**: `src/app/templates/partials/navigation.html`

Add cycling-specific menu items:
```html
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('rides.list_rides') }}">
        <i class="fas fa-bicycle"></i>
        <span>Rides</span>
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{{ url_for('races.list_races') }}">
        <i class="fas fa-trophy"></i>
        <span>Races</span>
    </a>
</li>
```

### 2. Dashboard
**File**: `src/app/templates/dashboard.html`

Customize to show:
- Upcoming rides
- Recent member registrations
- Total distance covered by club
- Recent achievements

### 3. Database Schema
**File**: `src/app/models.py`

Add new tables:
- `Ride` - Track ride events
- `RideAttendance` - Track who attended which ride
- `Race` - Track race events
- `Achievement` - Track member achievements

### 4. Settings
**File**: `src/app/routes/settings.py`

Add ACC-specific settings:
- Club name and description
- Contact information
- Social media links
- Default ride meeting points
- Email sender configuration

---

## ✅ Best Practices

### Security
1. ✅ Change default admin credentials immediately
2. ✅ Use environment variables for sensitive data
3. ✅ Never commit `.env` files to git
4. ✅ Use HTTPS in production
5. ✅ Implement proper role-based access control

### Database
1. ✅ Always create Alembic migrations for schema changes
2. ✅ Backup database regularly
3. ✅ Use indexes on frequently queried fields
4. ✅ Test migrations on development database first

### Code Quality
1. ✅ Follow PEP 8 style guide
2. ✅ Write descriptive commit messages
3. ✅ Comment complex logic
4. ✅ Use type hints in Python functions
5. ✅ Test features before committing

### Performance
1. ✅ Optimize database queries (use joins instead of multiple queries)
2. ✅ Cache frequently accessed data
3. ✅ Compress images for certificates
4. ✅ Use pagination for large lists

### User Experience
1. ✅ Provide clear error messages
2. ✅ Show loading indicators for slow operations
3. ✅ Make forms mobile-responsive
4. ✅ Add confirmation dialogs for destructive actions

---

## 📚 Learning Resources

### Flask Documentation
- Official Flask docs: https://flask.palletsprojects.com/
- Flask SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/

### Database Migrations
- Alembic tutorial: https://alembic.sqlalchemy.org/en/latest/tutorial.html

### Frontend
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Jinja2 templates: https://jinja.palletsprojects.com/

### Python Libraries
- Pillow (image processing): https://pillow.readthedocs.io/
- Pydantic (validation): https://docs.pydantic.dev/

---

## 🆘 Troubleshooting

### Common Issues

**1. Database connection errors**
- Check `MAIN_DB_URI` environment variable
- Verify database server is running
- Check credentials are correct

**2. Certificate generation fails**
- Verify template image exists
- Check CSV format matches expected columns
- Ensure fonts are installed in `members/fonts/`

**3. Email sending fails**
- Configure SMTP settings in environment variables
- Check email credentials
- Verify email server allows SMTP connections

**4. Port already in use**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process
taskkill /PID <process_id> /F
```

---

## 📞 Next Steps

1. ✅ Read through this entire guide
2. ✅ Run the application locally
3. ✅ Explore existing features
4. ✅ Plan your ACC-specific customizations
5. ✅ Start with Phase 1 (Branding)
6. ✅ Test each feature as you build
7. ✅ Document your changes in `acc_docs/`

Good luck building your ACC cycling club management system! 🚴‍♂️🚴‍♀️

---

**Document created**: October 21, 2025  
**Branch**: acc-rems  
**Version**: 2.0.0
