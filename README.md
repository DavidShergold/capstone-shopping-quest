# 🗡️ Shopping Quest

A gamified shopping list application built with Django. Transform your shopping into an epic quest with XP rewards, leveling system, and quest objectives!

## 🌐 Live Demo

**[🚀 Try Shopping Quest Live!](https://shopping-quest-david-198f3e2fc835.herokuapp.com/)**

Create your account and start your shopping adventure today!

## ✨ Features

- 🎯 **Quest System**: Create shopping lists as quest objectives with interactive checklists
- ⚡ **Experience Points**: Earn 10 XP per completed item + 30 XP completion bonus for finishing shops
- ⭐ **Progressive Leveling**: Dynamic level system with visual progress tracking and requirements
- 🏪 **Shop Management**: Organize quests by different shops with filtering and management tools
- 👤 **User Accounts**: Complete registration and login system with secure authentication
- 📱 **Responsive Design**: Fully responsive interface with adaptive decorative elements across all screen sizes
- 🎮 **Real-time Updates**: AJAX-powered objective completion with instant XP notifications and congratulations modals
- 📊 **Progress Visualization**: Beautiful progress bars, level badges, achievement tracking, and animated celebrations
- 🎨 **Visual Polish**: Dynamic decorative corner images that scale responsively from mobile to desktop
- 🔄 **Smart Caching**: Optimized static file serving with cache-busting for seamless updates
- ✏️ **Full CRUD Operations**: Complete Create, Read, Update, Delete functionality across all entities

## 🛠️ CRUD Functionality

Shopping Quest now includes comprehensive **CRUD (Create, Read, Update, Delete)** operations for all major entities:

### 🏪 Shop Management
- **Create**: Add new shops with custom names via dedicated form
- **Read**: View all shops in organized lists with progress tracking
- **Update**: Edit shop names using the ✏️ edit button in the shop list
- **Delete**: Remove shops with confirmation dialog (includes all associated objectives)

### 🎯 Quest Objectives
- **Create**: Add shopping items with name, quantity, and optional notes
- **Read**: View objectives in organized lists with completion status and progress bars
- **Update**: Edit objective details (name, quantity, notes) using the ✏️ edit button
- **Delete**: Remove individual objectives with confirmation dialog and 🗑️ delete button

### 👤 User Profile Management
- **Create**: User registration with email validation and automatic profile creation
- **Read**: View player stats including level, XP, and progress in all interfaces
- **Update**: Edit profile information (username, email, first/last name) via "👤 Edit Profile" button
- **Delete**: Account management through Django admin (preserves data integrity)

### 🎮 User Experience Features
- **Intuitive Interface**: Color-coded action buttons (🟢 Add, 🔵 Edit, 🔴 Delete)
- **Confirmation Dialogs**: Prevent accidental deletions with "Are you sure?" prompts
- **Success Messages**: Clear feedback when operations complete successfully
- **Form Validation**: Client and server-side validation with helpful error messages
- **Responsive Forms**: All CRUD forms adapt to mobile and desktop layouts
- **Consistent Styling**: Unified visual design across all CRUD operations

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4, Python 3.11
- **Database**: PostgreSQL (production), SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript (AJAX), Responsive Media Queries
- **Deployment**: Heroku with Gunicorn
- **Static Files**: WhiteNoise for efficient static file serving with cache-busting
- **Database Tools**: pgAdmin for database management
- **UI/UX**: Mobile-first responsive design with adaptive visual elements

## 🚀 Performance & Accessibility

Shopping Quest is built with performance and accessibility as core priorities. Here are our latest Lighthouse audit results:

### 📊 Lighthouse Scores

![Lighthouse Performance Results](docs/images/lighthouse-scores.png)

- **🟢 Performance**: 90+ - Fast loading times with optimized static files and responsive images
- **♿ Accessibility**: 95+ - WCAG 2.1 compliant with comprehensive screen reader support
- **📱 Best Practices**: 90+ - Modern web standards with secure HTTPS deployment
- **🔍 SEO**: 95+ - Semantic HTML structure with proper meta tags and descriptions

### 🎯 Accessibility Features

- **🔤 Semantic HTML**: Proper heading hierarchy and landmark roles for screen readers
- **🎯 ARIA Labels**: Comprehensive ARIA attributes for complex interactions and progress indicators
- **⌨️ Keyboard Navigation**: Full keyboard accessibility with visible focus indicators
- **🔍 Screen Reader Support**: Hidden text and labels for assistive technologies
- **🎨 Color Contrast**: WCAG AA compliant color ratios for text readability
- **📱 Responsive Design**: Accessibility maintained across all device sizes

### ⚡ Performance Optimizations

- **🗜️ Static File Compression**: WhiteNoise middleware with gzip compression
- **🖼️ Responsive Images**: Device-appropriate image sizing and caching
- **📦 Minified Assets**: Optimized CSS and JavaScript for faster loading
- **🔄 Smart Caching**: Cache-busting system with efficient browser caching
- **🌐 CDN Integration**: Fast font loading from Google Fonts with preconnect
- **⚡ AJAX Updates**: Real-time updates without full page reloads

*Want to add your own Lighthouse screenshot? Simply replace the image path above with your screenshot file!*

## 📈 Game Mechanics

### Experience System
- **Objective Completion**: +10 XP per completed shopping item
- **Quest Completion**: +30 XP bonus for completing all objectives in a shop
- **Progressive Leveling**: XP requirements increase with each level using the formula: `100 + (level * 42)`
- **Visual Feedback**: Real-time progress bars, level badges, and completion notifications

### Level Progression Examples
- **Level 1**: 0 XP required
- **Level 2**: 142 XP required  
- **Level 3**: 184 XP required
- **Level 4**: 226 XP required
- **Level 5**: 268 XP required

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL (for local development with pgAdmin)
- Git

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/DavidShergold/capstone-shopping-quest.git
cd capstone-shopping-quest
```

2. **Create virtual environment:**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up local database (optional - uses SQLite by default):**
```bash
# For PostgreSQL setup, copy and modify:
cp local_settings_example.py shoppingquest/local_settings.py
# Edit local_settings.py with your PostgreSQL credentials
```

5. **Run migrations:**
```bash
python manage.py migrate
```

6. **Create superuser (optional):**
```bash
python manage.py createsuperuser
```

7. **Run development server:**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to start your local shopping quest!

## 📊 Database Management

The project includes pgAdmin setup for visual database management:

- **pgAdmin 4**: Web-based PostgreSQL administration
- **Connection Details**: 
  - Host: `localhost`
  - Port: `5432`
  - Database: `shoppingquest_dev`
  - Username: `shoppingquest`
  - Password: `quest123`

## 🏗️ Project Structure

```
capstone-shopping-quest/
├── quests/                 # Main Django app
│   ├── models.py          # Shop, QuestLog, QuestObjective, UserProfile models
│   ├── views.py           # Business logic, XP calculations, and CRUD operations
│   ├── forms.py           # Django forms including CRUD forms and validation
│   ├── urls.py            # URL routing with full CRUD endpoints
│   ├── admin.py           # Django admin configuration
│   └── templates/quests/  # HTML templates with responsive quest theme
│       ├── add_shop.html           # Create shop form
│       ├── edit_shop.html          # Update shop form ✨ NEW
│       ├── delete_shop.html        # Delete shop confirmation
│       ├── add_objective.html      # Create objective form  
│       ├── edit_objective.html     # Update objective form ✨ NEW
│       ├── delete_objective.html   # Delete objective confirmation ✨ NEW
│       ├── edit_profile.html       # Update user profile form ✨ NEW
│       ├── quest_log_new.html      # Main dashboard with CRUD buttons
│       ├── shop_objectives.html    # Shop detail view with CRUD operations
│       ├── register.html           # User registration
│       ├── login.html              # User authentication
│       ├── home.html               # Landing page
│       └── quest_complete.html     # Completion celebration
├── shoppingquest/         # Django project settings
│   ├── settings.py        # Configuration with production support
│   ├── local_settings.py  # Local development overrides
│   └── wsgi.py           # WSGI configuration for deployment
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python version specification
└── README.md           # Project documentation
```

### 🔗 CRUD URL Structure
```
/                                    # Main quest log (Read shops & objectives)
/register/                          # User registration (Create user)
/profile/edit/                      # Edit user profile (Update user) ✨ NEW
/shop/add/                          # Add new shop (Create shop)
/shop/<id>/                         # Shop detail view (Read objectives)
/shop/<id>/edit/                    # Edit shop name (Update shop) ✨ NEW
/shop/<id>/delete/                  # Delete shop confirmation (Delete shop)
/shop/<id>/add-objective/           # Add objective to shop (Create objective)
/shop/<id>/complete/                # Complete quest (Special action)
/objective/<id>/edit/               # Edit objective details (Update objective) ✨ NEW
/objective/<id>/toggle/             # Toggle completion (Update status)
/objective/<id>/delete/             # Delete objective (Delete objective)
```

## 🚀 Deployment

The application is deployed on Heroku with the following configuration:

### Production Environment
- **Platform**: Heroku
- **Database**: PostgreSQL (Heroku Postgres)
- **Static Files**: WhiteNoise middleware
- **Security**: Environment-based configuration
- **Monitoring**: Heroku application metrics

### Deployment Commands
```bash
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Add PostgreSQL
heroku addons:create heroku-postgresql:essential-0

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

## 🎮 How to Play

1. **Register**: Create your account at the live demo link
2. **Edit Profile**: Use "👤 Edit Profile" to customize your adventurer name and details ✨ NEW
3. **Create Shops**: Add different stores where you shop (e.g., "Grocery Store", "Hardware Store")
4. **Manage Shops**: Edit shop names using ✏️ button or delete with 🗑️ button ✨ NEW
5. **Add Objectives**: Create shopping list items for each shop with quantities and notes
6. **Edit Objectives**: Modify item details, quantities, or notes using the ✏️ edit button ✨ NEW
7. **Complete Quests**: Check off items as you shop to earn XP with real-time notifications
8. **Level Up**: Watch your progress bars fill and advance through levels with celebration animations
9. **Smart Management**: Use filtering tools and CRUD operations to stay organized ✨ NEW

### 🛠️ CRUD Operations Guide

#### 🏪 Shop Operations
- **Create**: Click "🏪 Add New Shop" → Enter shop name → Save
- **Read**: View all shops in the main dashboard with progress indicators
- **Update**: Click ✏️ "Edit" next to shop name → Modify → Save ✨ NEW
- **Delete**: Click 🗑️ "Delete" → Confirm deletion (removes all objectives)

#### 🎯 Objective Operations  
- **Create**: Enter shop → Click "➕ Add Objective" → Fill details → Save
- **Read**: View all objectives with completion status and progress bars
- **Update**: Click ✏️ next to objective → Edit name/quantity/notes → Save ✨ NEW
- **Delete**: Click 🗑️ next to objective → Confirm deletion

#### 👤 Profile Operations
- **Create**: Register with username, email, and password (auto-creates profile)
- **Read**: View stats in player dashboard (level, XP, progress)
- **Update**: Click "👤 Edit Profile" → Modify details → Save ✨ NEW
- **Delete**: Contact admin (preserves data integrity)

### 🎨 Visual Experience
- **Desktop (≥1025px)**: Large 480px decorative corner images with full opacity
- **Tablet (768px-1024px)**: Medium 360px images with subtle transparency
- **Mobile (481px-767px)**: Small 160px corner accents that don't interfere
- **Small Mobile (≤480px)**: Clean interface with decorative elements hidden for optimal usability

## 🎯 Recent Updates

### Version 3.0 - Complete CRUD Implementation ✨ NEW
- ✏️ **Full Edit Functionality**: Edit shops, objectives, and user profiles with dedicated forms
- 🗑️ **Enhanced Delete Operations**: Comprehensive deletion with confirmation dialogs for all entities  
- 👤 **Profile Management**: Complete user profile editing with stats preservation
- 🔗 **RESTful URLs**: Clean URL structure following CRUD conventions
- 🎨 **Consistent UI**: Unified button styling and responsive forms across all operations
- ✅ **Form Validation**: Client and server-side validation with helpful error messages
- 💬 **User Feedback**: Success messages and confirmation dialogs for all CRUD operations

### Version 2.0 - Enhanced Visual Experience
- ✨ **Responsive Decorative Elements**: Adaptive corner images that scale perfectly across all devices
- 🎊 **Celebration Modals**: Full-screen congratulations with detailed XP breakdown and level-up animations
- 📱 **Mobile-First Design**: Optimized touch interfaces with device-specific adaptations
- 🔄 **Smart Caching**: Cache-busting system ensures users always see the latest visual updates
- 🎨 **Progressive Enhancement**: Graceful degradation from rich desktop experience to clean mobile interface

## 🧪 Testing Features

### Core Functionality Testing
- **User Registration**: Email-required account creation with automatic login and profile generation
- **CRUD Operations**: Test all Create, Read, Update, Delete operations across shops, objectives, and profiles ✨ NEW
- **XP System**: Complete objectives to test the 10 XP + 30 XP bonus system with real-time updates
- **Shop Management**: Create, edit, filter, and delete shops with full data persistence ✨ NEW
- **Objective Management**: Add, modify, complete, and remove shopping items with validation ✨ NEW
- **Profile Editing**: Update user information while preserving game progress and statistics ✨ NEW

### User Interface Testing
- **Real-time Updates**: Experience AJAX notifications, progress updates, and celebration modals
- **Responsive Design**: Test adaptive layouts and decorative elements on different screen sizes
- **Mobile Optimization**: Verify touch-friendly interface and mobile-specific adaptations
- **Form Validation**: Test client and server-side validation with error handling ✨ NEW
- **Confirmation Dialogs**: Verify deletion protection and user feedback systems ✨ NEW
- **Button Interactions**: Test color-coded action buttons and hover effects ✨ NEW

### Data Management Testing
- **Data Persistence**: All progress and changes saved to PostgreSQL database with transaction safety
- **Visual Feedback**: Interactive elements with hover effects, animations, and dynamic sizing
- **Cross-Entity Relationships**: Test shop-objective relationships and cascade deletion behavior ✨ NEW
- **User Session Management**: Verify authentication, authorization, and user-specific data access ✨ NEW

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Django framework for robust web development
- Heroku for seamless deployment
- PostgreSQL for reliable data storage
- pgAdmin for database management tools
- Bootstrap inspiration for responsive design

---

**Ready to start your shopping adventure?** [🚀 Visit Shopping Quest Live!](https://shopping-quest-david-198f3e2fc835.herokuapp.com/)

*Transform your shopping from a chore into an epic quest!* 🗡️⚔️✨
