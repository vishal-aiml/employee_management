# Employee Management

A basic FastAPI project for generating and viewing employee data using PostgreSQL.

## Setup Instructions

1. **Clone the project**
```
git clone https://github.com/your-username/employee-management.git
cd employee-management
```

2. **Create a PostgreSQL database**
- Open pgAdmin or use any PostgreSQL client.
- Create a new database called `employeesdb`.

3. **Create a `.env` file**
```
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/employeesdb
```
Replace `your_password` with your actual PostgreSQL password.

4. **Install Python dependencies**
```
pip install -r requirements.txt
```

5. **Run the application**
```
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /employees/generate` → generate 200 fake employees
- `GET /employees/` → list employees (supports `?skip=&limit=`)
- `GET /employees/chart` → shows a chart by department
- `GET /health` → health check
- Swagger UI: `http://localhost:8000/docs`
---

## Contact

For any queries, feel free to reach out:

📧 Email: [vishalupadhyay091@gmail.com](mailto:vishalupadhyay091@gmail.com)  
🔗 GitHub: [https://github.com/vishal-aiml](https://github.com/vishal-aiml)
