# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiaoyangpublic@163.com

from Tkinter import *

def add_courses(course_name_ent, course_start_time_ent,
                course_end_time_ent, course_time_cost_ent):
    pass
    

def create_add_courses_interface():
    add_courses_dialog = Toplevel()
    add_courses_dialog.title('Add Courses Information')

    row = Frame(add_courses_dialog)
    course_name_label = Label(row, text='Course Name:', width=20)
    course_name_entry = Entry(row)
    row.pack(side=TOP,fill=BOTH, expand=YES)
    course_name_label.pack(side=LEFT, fill=BOTH, expand=YES)
    course_name_entry.pack(side=RIGHT, fill=BOTH, expand=YES)

    row = Frame(add_courses_dialog)
    course_start_time_label = Label(row, text='Start Time:', width=20)
    course_start_time_entry = Entry(row)
    row.pack(side=TOP,fill=BOTH, expand=YES)
    course_start_time_label.pack(side=LEFT, fill=BOTH, expand=YES)
    course_start_time_entry.pack(side=RIGHT, fill=BOTH, expand=YES)

    row = Frame(add_courses_dialog)
    course_end_time_label = Label(row, text='End Time:', width=20)
    course_end_time_entry = Entry(row)
    row.pack(side=TOP,fill=BOTH, expand=YES)
    course_end_time_label.pack(side=LEFT, fill=BOTH, expand=YES)
    course_end_time_entry.pack(side=RIGHT, fill=BOTH, expand=YES)

    row = Frame(add_courses_dialog)
    course_time_cost_label = Label(row, text='Cost Time:', width=20)
    course_time_cost_entry = Entry(row)
    row.pack(side=TOP,fill=BOTH, expand=YES)
    course_time_cost_label.pack(side=LEFT, fill=BOTH, expand=YES)
    course_time_cost_entry.pack(side=RIGHT, fill=BOTH, expand=YES)

    add_course_btn = Button(add_courses_dialog, text='Add',
                            command=(lambda: add_courses(course_name_entry,
                                                         course_start_time_entry,
                                                         course_end_time_entry,
                                                         course_time_cost_entry)))
    add_course_btn.pack(side=BOTTOM, expand=YES, fill=BOTH)

if __name__ == '__main__':
    root = Tk()
    root.title('Plan4Courses')
    add_courses_btn = Button(root, text='Add Courses', command=create_add_courses_interface)
    del_courses_btn = Button(root, text='Delete Courses')
    gen_courses_cost_btn = Button(root, text='Generate Courses Cost')
    add_courses_btn.pack(fill=BOTH, expand=YES)
    del_courses_btn.pack(fill=BOTH, expand=YES)
    gen_courses_cost_btn.pack(fill=BOTH, expand=YES)
    root.mainloop()
