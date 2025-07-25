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

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4, Python 3.11
- **Database**: PostgreSQL (production), SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript (AJAX), Responsive Media Queries
- **Deployment**: Heroku with Gunicorn
- **Static Files**: WhiteNoise for efficient static file serving with cache-busting
- **Database Tools**: pgAdmin for database management
- **UI/UX**: Mobile-first responsive design with adaptive visual elements

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
│   ├── models.py          # Shop, QuestLog, QuestObjective, UserProfile
│   ├── views.py           # Business logic and XP calculations
│   ├── forms.py           # Django forms including CustomUserCreationForm
│   ├── urls.py            # URL routing
│   ├── admin.py           # Django admin configuration
│   └── templates/         # HTML templates with quest theme
├── shoppingquest/         # Django project settings
│   ├── settings.py        # Configuration with production support
│   ├── local_settings.py  # Local development overrides
│   └── wsgi.py           # WSGI configuration for deployment
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Python dependencies
├── Procfile             # Heroku deployment configuration
├── runtime.txt          # Python version specification
└── README.md           # This file
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
2. **Create Shops**: Add different stores where you shop (e.g., "Grocery Store", "Hardware Store")
3. **Add Objectives**: Create shopping list items for each shop with quantities and notes
4. **Complete Quests**: Check off items as you shop to earn XP with real-time notifications
5. **Level Up**: Watch your progress bars fill and advance through levels with celebration animations
6. **Manage**: Use the shop filter and management tools to stay organized
7. **Enjoy**: Experience responsive design that adapts beautifully to any device size

### 🎨 Visual Experience
- **Desktop (≥1025px)**: Large 480px decorative corner images with full opacity
- **Tablet (768px-1024px)**: Medium 360px images with subtle transparency
- **Mobile (481px-767px)**: Small 160px corner accents that don't interfere
- **Small Mobile (≤480px)**: Clean interface with decorative elements hidden for optimal usability

## 🎯 Recent Updates

### Version 2.0 - Enhanced Visual Experience
- ✨ **Responsive Decorative Elements**: Adaptive corner images that scale perfectly across all devices
- 🎊 **Celebration Modals**: Full-screen congratulations with detailed XP breakdown and level-up animations
- 📱 **Mobile-First Design**: Optimized touch interfaces with device-specific adaptations
- 🔄 **Smart Caching**: Cache-busting system ensures users always see the latest visual updates
- 🎨 **Progressive Enhancement**: Graceful degradation from rich desktop experience to clean mobile interface

## 🧪 Testing Features

- **User Registration**: Email-required account creation with automatic login
- **XP System**: Complete objectives to test the 10 XP + 30 XP bonus system
- **Shop Management**: Create, filter, and delete shops with full CRUD operations
- **Real-time Updates**: Experience AJAX notifications, progress updates, and celebration modals
- **Responsive Design**: Test adaptive layouts and decorative elements on different screen sizes
- **Mobile Optimization**: Verify touch-friendly interface and mobile-specific adaptations
- **Data Persistence**: All progress is saved to PostgreSQL database with transaction safety
- **Visual Feedback**: Interactive elements with hover effects, animations, and dynamic sizing

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
