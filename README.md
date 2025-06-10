## SIMPLY STORE - PYTHON DESKTOP APP

### Core Innovation: "Article Context" Workflow
**Core Concept:** Staff "logs into" an article/pallet and performs all actions from within this context.

```
Traditional Workflow:
Select Article → Choose Action → Enter Parameters

Simply Store Workflow:
Enter Article ID → "Log in" → All Actions Available
```

### Central UI Philosophy
**"Context-First" instead of "Action-First"**
- Staff thinks: "I'm working WITH this article"
- Not: "I'm performing an action ON an article"
- Pen and Paper Principle: "Flexible Working"

### Why This Approach Is Better:
- **🖊️ Simple:** Anyone can write an ID with a pen
- **💰 Cost-Effective:** No QR code printers or scanners needed
- **🔧 Flexible:** Staff can assign meaningful custom IDs
- **📱 Future-Proof:** OCR can be added later for automatic "reading"
- **🏭 Practical:** Many workshops and small warehouses already work this way

---

## TECHNICAL ARCHITECTURE (PYTHON)

### Framework & Tools
- **GUI Framework:** Tkinter (Python standard library)
- **Database:** SQLite3 + Python sqlite3 module
- **Architecture:** MVC Pattern (Model-View-Controller)
- **Additional:** ID-Code Generation, Pillow for image handling (future scanning)

### Project Structure
```
simply_store/
├── models/
│   ├── __init__.py
│   ├── article.py
│   ├── storage.py
│   ├── article_action.py
│   └── database.py
├── views/
│   ├── __init__.py
│   ├── main_window.py
│   ├── scan_window.py
│   ├── article_context_window.py
│   └── dashboard_window.py
├── controllers/
│   ├── __init__.py
│   ├── main_controller.py
│   ├── scan_controller.py
│   └── article_context_controller.py
├── services/
│   ├── __init__.py
│   ├── data_service.py
│   ├── id_service.py
│   └── demo_service.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── assets/
│   └── icons/
├── main.py
└── requirements.txt

### Typischer Inhalt einer `requirements.txt`:
```
tkinter
pillow
```
Um alle Pakete aus der `requirements.txt` zu installieren, verwende:

```bash
pip install -r requirements.txt
```
Mit dem Befehl

```bash
pip freeze > requirements.txt
```

werden alle aktuell installierten Pakete und deren Versionen in die `requirements.txt` geschrieben. So kann die Umgebung exakt reproduziert werden.

- **`requirements.txt`** = Liste aller benötigten Python-Pakete
- **Installation:** `pip install -r requirements.txt`
- **Aktualisieren:** `pip freeze > requirements.txt`



---

## CORE WORKFLOW: ARTICLE CONTEXT

### Article Context Window
**The Heart of the Application:**

```
┌──────────────────────────────────┐
│  📦 ARTICLE CONTEXT             │
│  ────────────────────────────── │
│  🏷️  Tool Box #A001            │
│  📍  Storage: Workshop Shelf 3  │
│  📊  Quantity: 1 piece         │
│  💰  Value: €45.00             │
│                                │
│  ACTIONS:                      │
│  [📦 Edit Details]             │
│  [📍 Relocate]                 │
│  [➕ Change Quantity]          │
│  [✂️  Split Unit]              │
│  [🔄 Merge Articles]           │
│  [📋 Show History]             │
│  [🖨️  Print New Label]         │
│                                │
│  [❌ Exit Context] [🏠 Home]    │
└──────────────────────────────────┘
```

### Key Features:
- **Cross-Platform:** Works on Windows, macOS, and Linux
- **Native Feel:** Uses system-native UI elements via Tkinter
- **Offline Support:** Local SQLite database
- **Lightweight:** No external dependencies beyond Python standard library
- **Extensible:** Easy to add new features and actions

---

## DESKTOP-FIRST DESIGN PRINCIPLES

### UI/UX Guidelines
- **Clear Layout:** Tkinter's grid system for organized interfaces
- **Keyboard Friendly:** Full keyboard navigation support
- **Consistent Styling:** Custom ttk.Style for professional appearance
- **Quick Navigation:** Keyboard shortcuts and intuitive flow
- **Responsive Design:** Proper window resizing and layout management

### Main Menu Structure
```
┌──────────────────────────────┐
│    📱 SIMPLY STORE          │
│                            │
│    [📱 SCAN ARTICLE]       │
│                            │
│    [📋 All Articles]       │
│    [🏪 Storage]            │
│    [📊 Dashboard]          │
│    [⚙️ Settings]           │
│                            │
│    [🎮 Load Demo]          │
└──────────────────────────────┘
```

---

## PYTHON-SPECIFIC ADVANTAGES

### Development Benefits
- **Rapid Prototyping:** Python's simplicity allows quick iteration
- **Rich Ecosystem:** Easy integration of additional libraries
- **Cross-Platform:** Same code runs on Windows, macOS, Linux
- **Maintainable:** Clean, readable code structure
- **Testable:** Easy unit testing with Python's built-in unittest

### Technical Implementation
- **SQLite Integration:** Native Python sqlite3 support
- **Error Handling:** Python's exception handling for robust operation
- **Data Validation:** Type hints and validation for data integrity
- **Logging:** Built-in logging module for debugging and monitoring
- **Configuration:** Easy configuration management with JSON/INI files