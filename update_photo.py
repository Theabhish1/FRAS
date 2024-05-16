



#    ##########
#     def update_photo_sample():
#     # Assuming you have a function to identify the selected student, let's call it get_selected_student()
#         selected_student = selected_student()

#     # Check if a student is selected
#     if select_student is not None:
#         # Open a file dialog to select the new photo sample
#         file_path = filedialog.askopenfilename(title="Select Photo Sample", filetypes=[("Image Files", "*.jpg *.png")])

#         # Check if a file is selected
#         if file_path:
#             # Here you would update the photo sample for the selected student in your database
#             # For demonstration purposes, let's just print the file path
#             print("Updated photo sample:", file_path)
#         else:
#             print("No file selected.")
#     else:
#         print("No student selected.")




    # def select_student():
    # # Assuming you have a list of students, let's call it students_list
    # # For demonstration purposes, let's assume it's a list of student IDs
    #     students_list = [101, 102, 103, 104]  # Example list of student IDs

    # # Create a simple dialog box to select the student
    #     selected_student_id = simpledialog.askinteger("Select Student", "Enter Student ID:")
    
    # # Check if a student ID is entered
    #     if selected_student_id:
    #     # Check if the entered student ID exists in the list
    #         if selected_student_id in students_list:
    #         # Here you would retrieve the selected student's details from your database or data source
    #         # For demonstration purposes, let's just print the selected student's ID
    #             print("Selected Student ID:", selected_student_id)
    #         else:
    #             print("Student not found in the list.")
    #     else:
    #         print("No student ID entered.")




# # Example of how to call the select_student function
# select_student()



#""seacrch button workable
# def search_records():
#     selected_criteria = search_combo.get()
#     search_query =  search_entry.get()

#     if selected_criteria == "Select" or search_query == "":
#         messagebox.showerror("Error", "Please select a search criteria and enter a search query.")
#         return

#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             username="root",
#             password="Hi@itsabhish1",
#             database="face_recognition",
#         )
#         my_cursor = conn.cursor()

#         query = f"SELECT * FROM student WHERE {selected_criteria} LIKE %s"
#         my_cursor.execute(query, (f'%{search_query}%',))
#         result = my_cursor.fetchall()

#         if len(result) == 0:
#             messagebox.showinfo("Info", "No records found.")
#         else:
#             # Display or process the search results as needed
#             pass  # You can implement this part based on your requirements

#         conn.close()
#     except Exception as e:
#         messagebox.showerror("Error", f"Error: {str(e)}")

# # Modify the Search Button to call the search_records function
# search_btn = Button(search_frame, text="Search", width=14, font=("times new roman", 10, "bold"), bg="green", fg="white", command=search_records)
# search_btn.grid(row=0, column=3, padx=5)


            
