def list_classes():
    """
    Display all classes in the system.
    """

    print("=== Class List ===")

    # Example data (temporary until database connection is added)
    classes = [
        {"id": 1, "name": "Class A", "grade": "Grade 10", "year": "2024"},
        {"id": 2, "name": "Class B", "grade": "Grade 11", "year": "2024"},
    ]

    for cls in classes:
        print(f"ID: {cls['id']}, Name: {cls['name']}, Grade: {cls['grade']}, Year: {cls['year']}")

    print("End of class list.\n")
