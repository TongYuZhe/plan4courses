# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiaoyangpublic@163.com

from Tkinter import *

def create_add_courses_interface():
    add_courses_dialog = Toplevel()
    add_courses_dialog.title('Add Courses Information')
    course_name_label = Label(add_courses_dialog, text='Course Name:')
    course_name_entry = Entry(add_courses_dialog)
    course_name_label.pack(side=LEFT, fill=BOTH, expand=YES)
    course_name_entry.pack(side=RIGHT, fill=BOTH, expand=YES)

def add_courses():
    create_add_courses_interface()

if __name__ == '__main__':
    root = Tk()
    root.title('Plan4Courses')
    add_courses_btn = Button(root, text='Add Courses', command=add_courses)
    del_courses_btn = Button(root, text='Delete Courses')
    gen_courses_cost_btn = Button(root, text='Generate Courses Cost')
    add_courses_btn.pack(fill=BOTH, expand=YES)
    del_courses_btn.pack(fill=BOTH, expand=YES)
    gen_courses_cost_btn.pack(fill=BOTH, expand=YES)
    root.mainloop()
