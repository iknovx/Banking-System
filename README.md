# Banking System

A Python console application for managing bank accounts, backed by MySQL. Built as a learning project to explore persistent storage, transactional integrity, and layered application structure.

## Features

- **User management** — create, look up, update, and delete user profiles
- **Accounts & balances** — persistent storage of users, transactions, and deposits in MySQL
- **Money transfers** — transfer flow designed around row locking (`SELECT ... FOR UPDATE`) to prevent race conditions on concurrent balance updates
- **Deposits** — track deposits against user accounts
- **Layered architecture** — separation between models, validation logic, and database access
- **Environment-based configuration** — connection settings loaded from environment variables, keeping credentials out of source code

## Tech Stack

- **Language:** Python
- **Database:** MySQL
- **Interface:** CLI (console-based)

## Project Structure

```
banking-system/
├── db.py           # MySQL connection and queries
├── models.py       # Data models (User, Account, Transaction, etc.)
├── validation.py   # Input and business-rule validation
├── main.py         # CLI entry point
├── .env.example    # Example environment configuration
└── requirements.txt
```

*(Adjust the tree above to match your actual file layout.)*

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Server
- `pip` for installing dependencies

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/iknovx/Banking-System.git
   cd Banking-System
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables
   ```bash
   cp .env.example .env
   ```
   Then fill in your MySQL credentials (host, user, password, database name).

4. Set up the database
   - Create a MySQL database
   - Run the schema/migration script (if provided) to create the required tables (users, transactions, deposits)

5. Run the application
   ```bash
   python main.py
   ```

## How Transfers Work

To keep balances consistent under concurrent access, transfers lock the involved rows during the update using `SELECT ... FOR UPDATE` inside a transaction. This prevents two operations from reading a stale balance and causing incorrect debits/credits.

## Roadmap / Ideas

- [ ] Transaction history view
- [ ] Unit tests for transfer and validation logic
- [ ] Basic authentication for user sessions
- [ ] Export transaction history to CSV

## Author

**Dzmitry Yudzenka** ([@iknovx](https://github.com/iknovx))
BTS SIO SLAM student, learning backend development and moving toward data engineering.

## License

This project is for learning purposes. Feel free to explore and adapt it.
