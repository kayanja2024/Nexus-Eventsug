**Nexus Events Website**

Professional Django website for Nexus Events Ltd — showcase services, portfolio, blog, and manage bookings and contacts.

**Overview**
- **Repository:**: Django project implementing frontend pages and admin-managed content for services, portfolio, bookings, contacts and blog.
- **Purpose:**: Promote Nexus Events Ltd, accept bookings, and manage media and content via the Django admin.

**Key Features**
- **Public pages:**: Home, About, Services, Portfolio, Blog, Contact, Booking forms.
- **Admin management:**: Manage services, gallery items, blog posts and booking inquiries via Django Admin.
- **Email notifications:**: SMTP-backed notifications for new bookings and contact messages (configurable via env vars).

**Tech Stack**
- **Framework:**: Django 5.x
- **Database:**: SQLite (development). Switch to PostgreSQL for production.
- **Language:**: Python 3.10+ (recommended)

**Quick Start (Development)**
- **Prerequisites:**: Python 3.10+, pip, virtualenv or venv.
- **Clone:**:

```bash
git clone <repo-url>
cd "Nexus Events"
```
- **Create virtualenv and install:**:

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt || pip install -r NEXUS_EVENTS_WEBSITE_REQUIREMENTS.md
```
- **Database migrations:**:

```bash
python manage.py migrate
```
- **Create admin user:**

```bash
python manage.py createsuperuser
```
- **Run development server:**

```bash
python manage.py runserver
```

**Important Files**
- **Django settings:**: [nexus_events_site/settings.py](nexus_events_site/settings.py#L1-L400)
- **Project requirements & spec:**: [NEXUS_EVENTS_WEBSITE_REQUIREMENTS.md](NEXUS_EVENTS_WEBSITE_REQUIREMENTS.md#L1-L400)
- **Management script:**: [manage.py](manage.py#L1-L200)

**Environment Variables**
- **Required / Recommended:**
  - `SECRET_KEY`: production secret key (do not commit)
  - `DEBUG`: set to `false` in production
  - `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`
  - `DEFAULT_FROM_EMAIL` and `BOOKINGS_NOTIFICATION_EMAIL`

Set environment variables locally using a `.env` file or your host environment; the project reads many of these from `os.getenv` in [nexus_events_site/settings.py](nexus_events_site/settings.py#L1-L400).

**Static & Media**
- **Static files:**: served from the `static/` folder during development; `STATIC_ROOT` defined in settings for production collection.
- **Media files:**: uploaded media stored in the `media/` folder (`MEDIA_ROOT`).

**Running Tests**
- **Run app tests:**

```bash
python manage.py test
```

**Deployment Notes**
- **Production settings:**: turn off `DEBUG`, configure `ALLOWED_HOSTS`, and use strong `SECRET_KEY`.
- **Database:**: replace SQLite with PostgreSQL or managed DB for production.
- **Static/media hosting:**: use a CDN or cloud object storage for media and collected static files.
- **Security:**: enforce HTTPS, secure admin access, and store secrets in environment variables.

**Project Structure (high level)**
- `core/`, `services/`, `portfolio/`, `bookings/`, `contacts/`, `blog/`, `accounts/`: modular Django apps for features described in the requirements.
- `templates/` and `static/`: front-end assets and templates.

**Contributing**
- **Bug fixes & features:**: please fork, create a feature branch, and open a PR with a clear description and tests where appropriate.
- **Code style:**: follow existing project conventions and keep changes minimal and focused.

**License**
- Add a license file (e.g., MIT) at the project root if you wish to make this project open-source.

**Contact**
- For questions about this repository or deployment help, open an issue or reach out to the project owner.

---
Generated for the Nexus Events Django project. Update environment and deployment details before production use.
