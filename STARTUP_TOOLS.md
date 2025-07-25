# Shopping Quest - Startup Tools

This project includes several helpful tools to ensure a smooth development experience and prevent authentication issues like we encountered.

## 🛠️ Available Tools

### 1. **Environment Check** (`check_environment.py`)
Validates that all required Python packages are installed.

```bash
python check_environment.py
```

**Output:**
- ✅ Lists all dependencies and their status
- ❌ Reports missing packages
- 🔧 Suggests fix commands

### 2. **Startup Validation** (`test_startup.py`)
Runs comprehensive checks without starting the server.

```bash
python test_startup.py
```

**Checks:**
- Dependencies are installed
- Database migrations are up to date
- Django system configuration is valid
- All components are ready

### 3. **Quick Start** (`quick_start.py`)
Automated startup with validation and error handling.

```bash
python quick_start.py
```

**Features:**
- Runs environment validation
- Applies pending migrations automatically
- Starts development server on port 8002
- Provides helpful status messages

### 4. **Windows Batch Files**
- `quick_start.bat` - Simple Windows startup script
- `start_dev_server.bat` - Full-featured Windows startup

## 🔧 Troubleshooting

### Common Issues:

1. **"No module named 'dj_database_url'"**
   ```bash
   pip install -r requirements.txt
   ```

2. **Authentication problems**
   - Run startup validation: `python test_startup.py`
   - Check database state: `python manage.py showmigrations`
   - Create superuser if needed: `python manage.py createsuperuser`

3. **Virtual environment not active**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

## 🚀 Recommended Workflow

1. **First time setup:**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   ```

2. **Daily development:**
   ```bash
   python test_startup.py    # Validate everything
   python quick_start.py     # Start server
   ```

3. **After pulling updates:**
   ```bash
   pip install -r requirements.txt  # Update dependencies
   python manage.py migrate          # Apply new migrations
   python quick_start.py             # Start server
   ```

## 🔒 Test Accounts

The system includes test accounts for development:

- **Superuser:** `sherg` (admin access)
- **Test User:** `testuser` / `testpass123`

## 🌐 Live Deployment

Production app: https://shopping-quest-david-198f3e2fc835.herokuapp.com/

---

These tools help prevent the authentication issues we experienced and ensure a consistent development environment!
