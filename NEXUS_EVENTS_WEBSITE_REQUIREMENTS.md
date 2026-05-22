# Nexus Events Ltd Website Requirements

## 1. Project Overview
Nexus Events Ltd requires a professional website to showcase event management services in Uganda, attract clients, and provide easy ways for customers to inquire, book, and engage online.

## 2. Project Objectives
- Promote Nexus Events Ltd services and brand.
- Showcase past events and portfolio.
- Enable clients to request and book event services.
- Provide company information and contact details.
- Improve online visibility and credibility.

## 3. Target Users
- Individuals planning events (weddings, parties, trade shows, concerts, caucuses, etc.).
- Corporate organizations.
- NGOs and institutions.
- General public seeking event services.

## 4. Functional Requirements

### 4.1 Frontend (User Interface)
- Responsive design for mobile, tablet, and desktop.
- Clean, modern, and user-friendly layout.
- Fast-loading pages.
- Clear call-to-action elements on key pages.

### 4.2 Website Pages
1. **Home Page**
   - Company introduction.
   - Service highlights.
   - Featured events.
   - CTA buttons: `Book Now`, `Contact Us`.

2. **About Us Page**
   - Company background.
   - Mission, vision, and values.
   - Team information.

3. **Services Page**
   - List of services (event planning, decoration, media coverage, etc.).
   - Service descriptions and images.

4. **Portfolio / Gallery**
   - Images and videos of past events.
   - Categorized galleries (weddings, corporate, concerts, etc.).

5. **Booking / Inquiry Page**
   - Online booking form with fields:
     - Name
     - Contact
     - Event Type
     - Date
     - Location
     - Budget
     - Message
   - Form submission confirmation.

6. **Contact Page**
   - Contact form.
   - Company address, phone, and email.
   - Google Maps embedded location.

7. **Blog / News**
   - Articles for event tips, updates, and company announcements.

## 5. Backend Requirements (Django)
- Django-based backend with a manageable and secure architecture.
- User-friendly content management via Django Admin.
- Admin can manage services, gallery items, blog posts, and bookings.
- Database stores:
  - Customer inquiries
  - Event bookings
  - Media references (images/videos)
- Authentication system for admin/staff users.
- Email notifications for new bookings and contact inquiries.

## 6. Non-Functional Requirements
- **Performance:** Fast page load and optimized media handling.
- **Security:** CSRF protection, XSS mitigation, secure form validation.
- **Scalability:** Support growth in traffic and content.
- **Usability:** Intuitive navigation and basic accessibility compliance.
- **Reliability:** Minimal downtime and consistent operation.

## 7. Database Requirements (Suggested Models)
- `User` / `Admin` (Django auth models)
- `Service`
- `GalleryItem`
- `Booking`
- `ContactMessage`
- `BlogPost`

## 8. Integrations
- SMTP email service for notifications.
- Google Maps embed/API for location display.
- Social media links (Facebook, Instagram, X, TikTok, LinkedIn where applicable).

## 9. Additional Requirements
- Online payment integration for bookings.
- Optional client dashboard/account system.
- Live chat support.
- Event calendar display and management.

## 10. Recommended Django App Structure
Suggested modular app split:
- `core` (home, about, static pages)
- `services` (service listings/details)
- `portfolio` (gallery/media)
- `bookings` (booking forms and requests)
- `contacts` (contact form/messages)
- `blog` (news/articles)
- `accounts` (optional client accounts/dashboard)

## 11. Suggested Data Model Fields

### Service
- `title`, `slug`, `short_description`, `full_description`
- `featured_image`
- `is_active`, `created_at`, `updated_at`

### GalleryItem
- `title`, `category`, `media_type` (image/video), `media_file` or `external_url`
- `description`, `event_date`
- `is_featured`, `created_at`

### Booking
- `full_name`, `email`, `phone`
- `event_type`, `event_date`, `location`, `budget`
- `message`, `status` (new/in_review/confirmed/completed/cancelled)
- `created_at`, `updated_at`

### ContactMessage
- `full_name`, `email`, `phone`
- `subject`, `message`
- `is_resolved`, `created_at`

### BlogPost
- `title`, `slug`, `excerpt`, `content`
- `featured_image`, `is_published`, `published_at`
- `author`, `created_at`, `updated_at`

## 12. Security and Compliance Checklist
- Enable Django CSRF middleware.
- Use Django template auto-escaping (default).
- Validate and sanitize form inputs server-side.
- Restrict admin URL access and use strong staff credentials.
- Enforce HTTPS in production.
- Store secrets in environment variables (`.env`), not in source code.

## 13. Deployment and Operations (Recommended)
- Hosting: VPS or managed cloud service.
- Database: PostgreSQL (recommended for production).
- Media/static handling: cloud object storage or proper server setup.
- Logging and monitoring for errors and uptime.
- Scheduled backups for database and media.

## 14. Milestones (Suggested)
- **Phase 1:** UI design + core pages + basic content.
- **Phase 2:** Booking/contact forms + admin management.
- **Phase 3:** Portfolio/blog modules + email notifications.
- **Phase 4:** Payment integration + client dashboard + live chat/calendar.
- **Phase 5:** Testing, optimization, deployment, and handover.

## 15. Acceptance Criteria
- All required pages are functional and responsive.
- Booking and contact forms save data and trigger notification emails.
- Admin can manage services, gallery, blog posts, and booking inquiries.
- Security basics (CSRF, validation, auth restrictions) are in place.
- Site is deployable in a production-ready configuration.

## 16. Conclusion
The Nexus Events Ltd website will be a secure, scalable, and professional digital platform built with Django and Python to promote services, engage clients, and streamline event booking workflows.
