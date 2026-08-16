# Project Plan for Client's HFT and Tracker Bot

## Guide 

Dima use private repo to get CLAUDE.md and /skills, /rules/ /agents, /commands for backend and Notion sprint board

Rules:
    1. Break down sprints and document changes with OpenSpec
    2. Use specific branch for work
    3. Update handoff

- Pgadmin server is on different repo for connection and proxies configurations
- Wallets analysis and behavioral pattern recognition in other repo will be connect it after API will be finished
- For right now use credentials and wallets list from Excel 


1. Connect demo pgadmin4 database from different docker-compose that share kairos_vps_network

2. Build telegram bot for /polymarket folder to track wallets movements and positions from database list 

3. Create own API with FastAPI from polymarket api on specific wallets for dashboard pipeline to analyse metrics

4. Work on feature to add new wallets to the bot for team members and storing them in the database, but in separate tables with specific access roles, so that they are not mixed with wallets which only accessible for public use, but are used within the team for trading and testing.

5. Create for each folder /bot and /polymarket seperate Dockerfile for VPS and connect thru docker-compose on same kairos_vps_network 

6. Need to add claude AI Agent for testing and RAG system with optimize GPU for local model