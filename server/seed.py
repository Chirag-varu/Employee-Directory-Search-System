"""
Script to seed the database with sample employee data.
Run this after setting up the database.
"""
from datetime import date
from app.database.connection import SessionLocal, engine
from app.database.models import Base, Employee

# Sample employee data
SAMPLE_EMPLOYEES = [
    {"name": "Rahul Sharma", "email": "rahul.sharma@company.com", "department": "Engineering", "designation": "Software Engineer", "date_of_joining": date(2023, 1, 15)},
    {"name": "Priya Patel", "email": "priya.patel@company.com", "department": "Engineering", "designation": "Senior Developer", "date_of_joining": date(2022, 6, 1)},
    {"name": "Amit Kumar", "email": "amit.kumar@company.com", "department": "Marketing", "designation": "Marketing Manager", "date_of_joining": date(2021, 3, 10)},
    {"name": "Sneha Gupta", "email": "sneha.gupta@company.com", "department": "HR", "designation": "HR Executive", "date_of_joining": date(2023, 4, 20)},
    {"name": "Vikram Singh", "email": "vikram.singh@company.com", "department": "Engineering", "designation": "Tech Lead", "date_of_joining": date(2020, 8, 5)},
    {"name": "Neha Verma", "email": "neha.verma@company.com", "department": "Finance", "designation": "Financial Analyst", "date_of_joining": date(2022, 11, 12)},
    {"name": "Rajesh Mehta", "email": "rajesh.mehta@company.com", "department": "Sales", "designation": "Sales Executive", "date_of_joining": date(2023, 2, 28)},
    {"name": "Anita Desai", "email": "anita.desai@company.com", "department": "Engineering", "designation": "QA Engineer", "date_of_joining": date(2021, 9, 15)},
    {"name": "Karan Malhotra", "email": "karan.malhotra@company.com", "department": "Marketing", "designation": "Content Strategist", "date_of_joining": date(2022, 7, 22)},
    {"name": "Pooja Reddy", "email": "pooja.reddy@company.com", "department": "HR", "designation": "HR Manager", "date_of_joining": date(2019, 5, 1)},
    {"name": "Suresh Iyer", "email": "suresh.iyer@company.com", "department": "Engineering", "designation": "DevOps Engineer", "date_of_joining": date(2022, 1, 10)},
    {"name": "Deepa Nair", "email": "deepa.nair@company.com", "department": "Finance", "designation": "Accountant", "date_of_joining": date(2023, 6, 5)},
    {"name": "Arun Krishnan", "email": "arun.krishnan@company.com", "department": "Engineering", "designation": "Frontend Developer", "date_of_joining": date(2023, 3, 18)},
    {"name": "Meera Joshi", "email": "meera.joshi@company.com", "department": "Sales", "designation": "Sales Manager", "date_of_joining": date(2020, 12, 1)},
    {"name": "Rohit Agarwal", "email": "rohit.agarwal@company.com", "department": "Engineering", "designation": "Backend Developer", "date_of_joining": date(2022, 9, 8)},
    {"name": "Kavita Chopra", "email": "kavita.chopra@company.com", "department": "Marketing", "designation": "Digital Marketing Specialist", "date_of_joining": date(2023, 5, 12)},
    {"name": "Sanjay Bhatt", "email": "sanjay.bhatt@company.com", "department": "Finance", "designation": "Finance Manager", "date_of_joining": date(2021, 7, 8)},
    {"name": "Ritu Singh", "email": "ritu.singh@company.com", "department": "Engineering", "designation": "Full Stack Developer", "date_of_joining": date(2022, 10, 20)},
    {"name": "Manish Rao", "email": "manish.rao@company.com", "department": "Sales", "designation": "Business Development Manager", "date_of_joining": date(2021, 2, 15)},
    {"name": "Divya Menon", "email": "divya.menon@company.com", "department": "HR", "designation": "Talent Acquisition Specialist", "date_of_joining": date(2023, 8, 1)},
    {"name": "Nikhil Kapoor", "email": "nikhil.kapoor@company.com", "department": "Engineering", "designation": "Data Engineer", "date_of_joining": date(2022, 4, 10)},
    {"name": "Swati Kulkarni", "email": "swati.kulkarni@company.com", "department": "Marketing", "designation": "Brand Manager", "date_of_joining": date(2021, 11, 25)},
    {"name": "Arjun Nambiar", "email": "arjun.nambiar@company.com", "department": "Engineering", "designation": "Mobile Developer", "date_of_joining": date(2023, 1, 30)},
    {"name": "Anjali Saxena", "email": "anjali.saxena@company.com", "department": "Finance", "designation": "Budget Analyst", "date_of_joining": date(2022, 8, 15)},
    {"name": "Vishal Thakur", "email": "vishal.thakur@company.com", "department": "Sales", "designation": "Account Executive", "date_of_joining": date(2023, 4, 5)},
    {"name": "Madhuri Patil", "email": "madhuri.patil@company.com", "department": "HR", "designation": "Employee Relations Manager", "date_of_joining": date(2020, 6, 12)},
    {"name": "Ashish Pandey", "email": "ashish.pandey@company.com", "department": "Engineering", "designation": "Cloud Architect", "date_of_joining": date(2021, 12, 1)},
    {"name": "Rekha Bose", "email": "rekha.bose@company.com", "department": "Marketing", "designation": "Social Media Manager", "date_of_joining": date(2022, 3, 18)},
    {"name": "Gaurav Mishra", "email": "gaurav.mishra@company.com", "department": "Engineering", "designation": "Security Engineer", "date_of_joining": date(2023, 7, 10)},
    {"name": "Lakshmi Iyer", "email": "lakshmi.iyer@company.com", "department": "Finance", "designation": "Tax Consultant", "date_of_joining": date(2021, 9, 22)},
    {"name": "Tarun Jain", "email": "tarun.jain@company.com", "department": "Sales", "designation": "Regional Sales Manager", "date_of_joining": date(2020, 10, 5)},
    {"name": "Nisha Ghosh", "email": "nisha.ghosh@company.com", "department": "HR", "designation": "Compensation Analyst", "date_of_joining": date(2022, 12, 8)},
    {"name": "Aditya Pillai", "email": "aditya.pillai@company.com", "department": "Engineering", "designation": "Machine Learning Engineer", "date_of_joining": date(2023, 2, 14)},
    {"name": "Shweta Dubey", "email": "shweta.dubey@company.com", "department": "Marketing", "designation": "Product Marketing Manager", "date_of_joining": date(2021, 5, 20)},
    {"name": "Ravi Khandelwal", "email": "ravi.khandelwal@company.com", "department": "Engineering", "designation": "Systems Engineer", "date_of_joining": date(2022, 7, 30)},
    {"name": "Tina Kapoor", "email": "tina.kapoor@company.com", "department": "Finance", "designation": "Investment Analyst", "date_of_joining": date(2023, 9, 11)},
    {"name": "Karthik Reddy", "email": "karthik.reddy@company.com", "department": "Sales", "designation": "Sales Operations Manager", "date_of_joining": date(2021, 4, 16)},
    {"name": "Pallavi Deshmukh", "email": "pallavi.deshmukh@company.com", "department": "HR", "designation": "Learning & Development Manager", "date_of_joining": date(2022, 2, 28)},
    {"name": "Mohit Ahluwalia", "email": "mohit.ahluwalia@company.com", "department": "Engineering", "designation": "Network Engineer", "date_of_joining": date(2023, 6, 19)},
    {"name": "Asha Nair", "email": "asha.nair@company.com", "department": "Marketing", "designation": "SEO Specialist", "date_of_joining": date(2021, 8, 7)},
    {"name": "Pranav Shah", "email": "pranav.shah@company.com", "department": "Engineering", "designation": "Site Reliability Engineer", "date_of_joining": date(2022, 5, 25)},
    {"name": "Deepika Bansal", "email": "deepika.bansal@company.com", "department": "Finance", "designation": "Payroll Manager", "date_of_joining": date(2023, 3, 9)},
    {"name": "Sameer Vohra", "email": "sameer.vohra@company.com", "department": "Sales", "designation": "Key Account Manager", "date_of_joining": date(2020, 11, 14)},
    {"name": "Poornima Rao", "email": "poornima.rao@company.com", "department": "HR", "designation": "HR Business Partner", "date_of_joining": date(2022, 9, 3)},
    {"name": "Varun Bhatia", "email": "varun.bhatia@company.com", "department": "Engineering", "designation": "Database Administrator", "date_of_joining": date(2021, 10, 21)},
    {"name": "Shreya Menon", "email": "shreya.menon@company.com", "department": "Marketing", "designation": "Email Marketing Specialist", "date_of_joining": date(2023, 4, 17)},
    {"name": "Harish Kumar", "email": "harish.kumar@company.com", "department": "Engineering", "designation": "DevSecOps Engineer", "date_of_joining": date(2022, 6, 13)},
    {"name": "Ananya Sharma", "email": "ananya.sharma@company.com", "department": "Finance", "designation": "Financial Controller", "date_of_joining": date(2021, 1, 5)},
    {"name": "Vivek Malhotra", "email": "vivek.malhotra@company.com", "department": "Sales", "designation": "Channel Sales Manager", "date_of_joining": date(2023, 10, 2)},
    {"name": "Sunita Verma", "email": "sunita.verma@company.com", "department": "HR", "designation": "Diversity & Inclusion Manager", "date_of_joining": date(2020, 3, 28)},
]


def seed_database():
    """Seed the database with sample employees."""
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Clear existing data
        existing_count = db.query(Employee).count()
        if existing_count > 0:
            print(f"Clearing {existing_count} existing employees...")
            db.query(Employee).delete()
            db.commit()
        
        # Insert sample employees
        for emp_data in SAMPLE_EMPLOYEES:
            employee = Employee(**emp_data)
            db.add(employee)
        
        db.commit()
        print(f"Successfully seeded {len(SAMPLE_EMPLOYEES)} employees!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
