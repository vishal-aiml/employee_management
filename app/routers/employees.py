from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List

from app.crud import get_employees, get_employee_count_by_department
from app.schemas import EmployeeObjectResponse
from app.database import get_db
from app.utils.faker_generator import generate_fake_employees

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/generate")
def generate(db: Session = Depends(get_db)):
    generate_fake_employees(db, 200)
    return {"message": "Generated 200 fake employees"}

@router.get("/", response_model=List[EmployeeObjectResponse])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_employees(db, skip, limit)

@router.get("/chart", response_class=HTMLResponse)
def get_chart(db: Session = Depends(get_db)):
    data = get_employee_count_by_department(db)    
    labels = [dept for dept, _ in data]
    values = [count for _, count in data]
    html_content = f"""
    <html>
    <head>
        <title>Employee Department Chart</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    </head>
    <body>
        <h2>Employee Chart</h2>
        <canvas id="employee_chart_view" width="400" height="200"></canvas>
        <script>
            const chart_data = document.getElementById('employee_chart_view').getContext('2d');
            const employee_chart = new Chart(chart_data, {{
                type: 'bar',
                data: {{
                    labels: {labels},
                    datasets: [{{
                        label: 'Total Employees',
                        data: {values},
                        backgroundColor: 'white',
                        borderColor: 'black',
                        borderWidth: 1
                    }}]
                }}
            }});
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)