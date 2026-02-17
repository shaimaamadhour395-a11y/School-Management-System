def update_class(class_id, new_name=None, new_grade=None, new_year=None):
    """
    Update existing class details.
    """

    print("=== Update Class ===")
    print(f"Class ID: {class_id}")

    if new_name:
        print(f"Updated Name: {new_name}")

    if new_grade:
        print(f"Updated Grade Level: {new_grade}")

    if new_year:
        print(f"Updated Academic Year: {new_year}")

    print("Class updated successfully!\n")
