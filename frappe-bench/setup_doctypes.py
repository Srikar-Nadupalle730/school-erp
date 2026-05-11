import frappe

def create_doctypes():
    frappe.init(site='school.local')
    frappe.connect()

    frappe.conf.developer_mode = 1

    doctypes_to_create = [
        {
            "doctype": "DocType",
            "name": "School Student",
            "module": "School ERP",
            "custom": 0,
            "autoname": "format:STU-{YYYY}-{####}",
            "fields": [
                {"fieldname": "first_name", "label": "First Name", "fieldtype": "Data", "reqd": 1},
                {"fieldname": "last_name", "label": "Last Name", "fieldtype": "Data"},
                {"fieldname": "email", "label": "Email", "fieldtype": "Data", "options": "Email"},
                {"fieldname": "enrollment_date", "label": "Enrollment Date", "fieldtype": "Date"},
                {"fieldname": "grade", "label": "Grade", "fieldtype": "Select", "options": "9th Grade\n10th Grade\n11th Grade\n12th Grade"}
            ],
            "permissions": [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}]
        },
        {
            "doctype": "DocType",
            "name": "School Teacher",
            "module": "School ERP",
            "custom": 0,
            "autoname": "format:TCH-{YYYY}-{####}",
            "fields": [
                {"fieldname": "first_name", "label": "First Name", "fieldtype": "Data", "reqd": 1},
                {"fieldname": "last_name", "label": "Last Name", "fieldtype": "Data"},
                {"fieldname": "subject", "label": "Primary Subject", "fieldtype": "Data"},
                {"fieldname": "email", "label": "Email", "fieldtype": "Data", "options": "Email"}
            ],
            "permissions": [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}]
        },
        {
            "doctype": "DocType",
            "name": "School Course",
            "module": "School ERP",
            "custom": 0,
            "fields": [
                {"fieldname": "course_name", "label": "Course Name", "fieldtype": "Data", "reqd": 1},
                {"fieldname": "teacher", "label": "Assigned Teacher", "fieldtype": "Link", "options": "School Teacher"}
            ],
            "permissions": [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}]
        },
        {
            "doctype": "DocType",
            "name": "School Attendance",
            "module": "School ERP",
            "custom": 0,
            "fields": [
                {"fieldname": "date", "label": "Date", "fieldtype": "Date", "reqd": 1},
                {"fieldname": "student", "label": "Student", "fieldtype": "Link", "options": "School Student", "reqd": 1},
                {"fieldname": "status", "label": "Status", "fieldtype": "Select", "options": "Present\nAbsent\nLate", "reqd": 1}
            ],
            "permissions": [{"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1}]
        }
    ]

    for dt in doctypes_to_create:
        if not frappe.db.exists("DocType", dt["name"]):
            print(f"Creating DocType {dt['name']}...")
            doc = frappe.get_doc(dt)
            doc.insert()
            print(f"DocType {dt['name']} created successfully.")
        else:
            print(f"DocType {dt['name']} already exists.")

    frappe.db.commit()
    print("All DocTypes setup complete.")

if __name__ == "__main__":
    create_doctypes()
