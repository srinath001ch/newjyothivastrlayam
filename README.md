# NEW JYOTHI VASTRALAYAM — Premium Saree Shop Website

A complete, premium, single-project **Django 5** website for **NEW JYOTHI VASTRALAYAM**, a saree shop
located at Bodrai Bazar, Nakerkal, Nalgonda. Built as one Django project with server-rendered
Django Templates (no React/Next.js/Vue), styled with Tailwind CSS, and animated using GSAP,
AOS, and Swiper.js.

Customers browse a luxury black-gold catalogue and order directly on **WhatsApp** — there is no
cart, checkout, payment gateway, user registration, reviews, wishlist, coupons, or inventory
tracking, by design. The shop owner manages everything through a custom, password-protected
dashboard at `/dashboard/`.

---

## ✨ Features

### Public Website
- **Home** — animated hero banner, marquee strip, featured sarees carousel, category grid,
  latest sarees, About preview with animated counters, contact section with embedded Google Map.
- **Collection** — search, filter by category, sort by price/name, pagination.
- **Product Details** — image gallery (Swiper), price, fabric, description, and a big
  **"Order on WhatsApp"** button that opens a pre-filled WhatsApp message.
- **About** — shop story, values, call to action.
- **Contact** — contact form (saved to DB + visible in dashboard), store info, embedded map,
  direct WhatsApp button.
- Floating WhatsApp button on every page, glassmorphism navbar, mobile-first responsive design,
  GSAP scroll animations, AOS reveal animations, image reveal effects, parallax hero, hover
  tilt effects on product cards.

### Owner Dashboard (`/dashboard/`)
A fully custom (non-Django-admin) dashboard styled to match the website:
- Secure login/logout (Django's built-in auth, custom templates).
- Dashboard home with quick stats (total sarees, active, featured, categories) and recent activity.
- **Sarees:** add / edit / delete, upload multiple images per saree, mark a primary image,
  set price, mark featured/active, assign category.
- **Categories:** add / edit / delete, upload a category image, set display order.
- **Messages:** view messages submitted through the Contact page, with a one-click
  "Reply on WhatsApp" link.

Django's built-in admin is also available at `/django-admin/` as a technical fallback, but the
shop owner is expected to use the friendly `/dashboard/`.

---

## 🧱 Tech Stack

| Layer          | Technology                          |
|----------------|--------------------------------------|
| Backend        | Django 5 (Python)                    |
| Database       | SQLite (default, zero setup)         |
| Templates      | Django Templates (server-rendered)   |
| Styling        | Tailwind CSS (CDN)                   |
| Animation      | GSAP + ScrollTrigger, AOS            |
| Carousels      | Swiper.js                            |
| Images         | Pillow (image handling)              |

No React, Next.js, or Vue is used anywhere in this project.

---

## 📁 Project Structure

```
newjyothi/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── db.sqlite3                 # created after migrate
│
├── newjyothi/                 # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── shop/                      # Main application
│   ├── models.py              # Category, Saree, SareeImage, ContactMessage
│   ├── views.py                # Public views + dashboard (custom admin) views
│   ├── urls.py
│   ├── admin.py                # Django admin registration (fallback)
│   ├── forms.py                # Styled ModelForms + image formset
│   ├── context_processors.py   # Injects shop name/phone/address into all templates
│   └── management/commands/seed_data.py   # Optional demo-data seeder
│
├── templates/
│   ├── base.html                # Public site layout (navbar, footer, WhatsApp button)
│   ├── shop/
│   │   ├── home.html
│   │   ├── collection.html
│   │   ├── product_detail.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── _product_card.html  # Reusable saree card partial
│   └── dashboard/
│       ├── dashboard_base.html # Sidebar layout for the dashboard
│       ├── login.html
│       ├── dashboard_home.html
│       ├── saree_list.html
│       ├── saree_form.html     # Add/Edit saree + image formset
│       ├── category_list.html
│       ├── category_form.html
│       ├── confirm_delete.html
│       └── messages.html
│
├── static/
│   ├── css/style.css           # Premium black/white/gold theme, glassmorphism, animations
│   └── js/animations.js        # GSAP, AOS, Swiper, tilt, parallax, mobile menu logic
│
└── media/                      # Uploaded saree & category images (created at runtime)
    ├── sarees/
    └── categories/
```

---

## 🚀 Getting Started

### 1. Requirements
- Python 3.10+

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Create the shop owner's login (superuser)
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username and password — this is what you'll use to log in at
`/dashboard/login/`.

### 5. (Optional) Load sample demo data
This adds 6 categories and 8 sample sarees (without images) so you can see how the site looks
immediately:
```bash
python manage.py seed_data
```
Add images to these sarees from the dashboard for the best look, or delete them and add your
own real sarees.

### 6. Run the development server
```bash
python manage.py runserver
```

- Website: http://127.0.0.1:8000/
- Owner Dashboard: http://127.0.0.1:8000/dashboard/login/
- Django Admin (fallback): http://127.0.0.1:8000/django-admin/

---

## 🛍️ Managing the Shop (For the Owner)

1. Go to `/dashboard/login/` and log in with the superuser account you created.
2. **Add categories first** (e.g. "Kanjivaram Silk", "Banarasi Silk") from **Categories → Add Category**.
3. **Add sarees** from **Manage Sarees → Add New Saree**:
   - Fill in name, category, price, fabric, and description.
   - Upload one or more images, and tick "Primary" on the main image.
   - Tick "Show in Featured Sarees section" to feature it on the homepage.
   - Tick "Active" to make it visible on the website (uncheck to hide without deleting).
4. Edit or delete any saree/category at any time from their respective list pages.
5. Check **Messages** to see enquiries submitted through the Contact page, and reply directly
   on WhatsApp with one click.

---

## 💬 WhatsApp Ordering

Every saree's "Order on WhatsApp" button opens:
```
https://wa.me/919533813859
```
with a pre-filled message:
```
Hello New Jyothi Vastralayam,
I want to order this saree.
Product: <Saree Name>
Price: Rs. <Price>
My Name:
My Mobile:
```
The customer only needs to fill in their name and mobile number and hit send — no cart, no
checkout, no payment gateway involved.

---

## 🏬 Business Details

- **Shop:** NEW JYOTHI VASTRALAYAM
- **Phone / WhatsApp:** 9533813859
- **Address:** Bodrai Bazar, Nakerkal, Nalgonda.

These details are centrally defined in `newjyothi/settings.py` (`SHOP_NAME`, `SHOP_PHONE`,
`SHOP_WHATSAPP`, `SHOP_ADDRESS`) and automatically appear across the whole site via
`shop/context_processors.py` — update them there if the business details ever change.

---

## 📝 Notes

- `DEBUG = True` and a development `SECRET_KEY` are set for local/demo use. Before deploying
  to a live server, set `DEBUG = False`, move the secret key to an environment variable, set
  `ALLOWED_HOSTS`, and serve static/media files properly (e.g. via WhiteNoise + a cloud storage
  bucket, or Nginx).
- The database is SQLite by default — no separate database server is required.
- All animation libraries (Tailwind, GSAP, AOS, Swiper) are loaded via CDN, so an internet
  connection is required in the browser to see full styling/animations.
