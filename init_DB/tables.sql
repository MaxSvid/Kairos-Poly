--- Proxies Settings --- 
CREATE TABLE IF NOT EXIST network_proxies (
    id SERIAL PRIMARY KEY,
);

CREATE TABLE IF NOT EXIST wallets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    wallet_address VARCHAR(42) UNIQUE NOT NULL,
    wallet_type VARCHAR(20) NOT NULL,
    signature_type INT DEFAULT 0,     
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--- Telegram Bot ---
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT,
    joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);