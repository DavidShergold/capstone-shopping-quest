# 🗡️ Shopping Quest

A gamified shopping list application built with Django. Transform your shopping into an epic quest with XP rewards, leveling system, and quest objectives!

## Features

- 🎯 **Quest System**: Create shopping lists as quest objectives
- ⚡ **Experience Points**: Earn 10 XP per completed item + 30 XP completion bonus
- ⭐ **Leveling System**: Progressive leveling with visual progress tracking
- 🏪 **Shop Management**: Organize quests by different shops
- 👤 **User Accounts**: Registration and login system
- 📱 **Responsive Design**: Works on desktop and mobile

## Live Demo

[Add your deployed URL here]

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/DavidShergold/capstone-shopping-quest.git
cd capstone-shopping-quest
```

2. Create virtual environment:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to start your shopping quest!

## Deployment

### Heroku Deployment

1. Install Heroku CLI and login
2. Create Heroku app:
```bash
heroku create your-app-name
```

3. Set environment variables:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
```

4. Deploy:
```bash
git push heroku main
```

5. Run migrations:
```bash
heroku run python manage.py migrate
```

## Technologies Used

- **Backend**: Django 5.2.4, Python 3.11
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Heroku, Gunicorn, WhiteNoise

## Game Mechanics

- **Objective Completion**: +10 XP per item
- **Quest Completion**: +30 XP bonus for completing all objectives in a shop
- **Leveling Formula**: Progressive XP requirements that increase with each level
- **Visual Progress**: Real-time progress bars and level badges

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
