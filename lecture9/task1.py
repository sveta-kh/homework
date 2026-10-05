# User Profile Creator

def create_user_profile(first_name, last_name, role = "Student", is_active = True):
    profile = {"F_name" : first_name, 
               "L_name" : last_name, 
               "Role" : role, 
               "Is Active" : is_active}
    return profile
print(create_user_profile("Svetlana", "Khutsishvili"))
print(create_user_profile ("Svetlana", "Khutsishvili", role = "Teacher", is_active = False))