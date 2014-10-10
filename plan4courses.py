# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiaoyangpublic@163.com

from Tkinter import *

class Course:
    def __init__(self, course_name, course_start_time,
                 course_end_time, course_time_cost):
        self.name = course_name
        self.start_time = course_start_time
        self.end_time = course_end_time
        self.time_cost = course_time_cost

def add_courses(course_info_list,courses):
    course_name, start_time, end_time, time_cost = course_info_list
    course = Course(course_name.get(), start_time.get(),
                    end_time.get(), time_cost.get())
    courses.append(course)
    print courses[0].name

def make_course_info_form():
    add_courses_dialog = Toplevel()
    add_courses_dialog.title('Add Courses')
    course_info_list = ['Course Name', 'Start Time', 'End Time', 'Time Cost']
    course_info_ent_list = []
    for course_info_name in course_info_list:
        row = Frame(add_courses_dialog)
        label = Label(row, text=course_info_name, width=20)
        entry = Entry(row)
        course_info_ent_list.append(entry)
        row.pack(side=TOP,fill=BOTH, expand=YES)
        label.pack(side=LEFT, fill=BOTH, expand=YES)
        entry.pack(side=RIGHT, fill=BOTH, expand=YES)
    return add_courses_dialog, course_info_ent_list
        

def create_add_courses_interface(courses):
    add_courses_dialog, course_info_ent_list = make_course_info_form()
    add_course_btn = Button(add_courses_dialog, text='Add',
                            command=(lambda: add_courses(course_info_ent_list, courses)))
    add_course_btn.pack(side=BOTTOM, expand=YES, fill=BOTH)

def create_main_interface(courses):
    root = Tk()
    root.title('Plan4Courses')
    add_courses_btn = Button(root, text='Add Courses', command=(lambda:create_add_courses_interface(courses)))
    del_courses_btn = Button(root, text='Delete Courses')
    gen_courses_cost_btn = Button(root, text='Generate Courses Cost')
    add_courses_btn.pack(fill=BOTH, expand=YES)
    del_courses_btn.pack(fill=BOTH, expand=YES)
    gen_courses_cost_btn.pack(fill=BOTH, expand=YES)
    root.mainloop()

if __name__ == '__main__':
    # Load configuration
    courses = []

    create_main_interface(courses)
    
