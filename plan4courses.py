# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiaoyangpublic@163.com

from Tkinter import *
import pickle

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

def onPress(states, i):
    states[i] = True

def del_courses(states, courses):
    for i, state in enumerate(states):
        if state: del courses[i]

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

def create_del_courses_interface(courses):
    del_courses_dialog = Toplevel()
    states = [False]*len(courses)
    for course in courses:
        var = IntVar()
        row = Frame(del_courses_dialog)
        chkbtn = Checkbutton(row, text = course.name, variable = var,
                             command=(lambda i=courses.index(course): onPress(states, i)))
        row.pack(side=TOP,fill=BOTH,expand=YES)
        chkbtn.pack(side=LEFT)
    delbtn = Button(del_courses_dialog, text="Delete", command=(lambda: del_courses(states, courses)))
    delbtn.pack(expand=YES, fill=BOTH)
    
def get_height(courses):
    height = sum([int(course.time_cost) for course in courses])
    return height*10+100

def get_width(courses):
    if courses:
        time_list = [map(int, course.start_time.split('-')) for course in courses]
        for i in range(3):
            sorted(time_list, key=lambda e:e[i])
        year = time_list[-1][0] - time_list[0][0]
        month = time_list[-1][1] - time_list[0][1]
        day = time_list[-1][2] - time_list[0][2]
        width = (year*365+month*30+day)*10+100
        return width
    else:
        return 100

def get_periods(courses):
    pass

def draw_courses_schedule(courses):
    courses_schedule_graph = Toplevel()
    width = get_width(courses)
    height = get_height(courses)
    canvas = Canvas(courses_schedule_graph, width=width, height=height, bg='white')
    periods = get_periods(courses)
    # Draw periods
    canvas.pack()
    
def create_main_interface(courses):
    root = Tk()
    root.title('Plan4Courses')
    root.minsize(width=250, height=150)
    add_courses_btn = Button(root, text='Add Courses', command=(lambda:create_add_courses_interface(courses)))
    del_courses_btn = Button(root, text='Delete Courses', command=(lambda:create_del_courses_interface(courses)))
    gen_courses_cost_btn = Button(root, text='Generate Courses Cost', command=(lambda:draw_courses_schedule(courses)))
    add_courses_btn.pack(fill=BOTH, expand=YES)
    del_courses_btn.pack(fill=BOTH, expand=YES)
    gen_courses_cost_btn.pack(fill=BOTH, expand=YES)
    root.mainloop()

if __name__ == '__main__':
    # Load courses information
    courses_info_file = open('courses_info.txt', 'r')
    try:
        courses = pickle.load(courses_info_file)
    except EOFError:
        courses = []
    except:
        print('Unexpected Error!')
        exit(0)
        
    create_main_interface(courses)

    # Store courses information into local file
    pickle.dump(courses, open('courses_info.txt', 'w'))
    courses_info_file.close()
    
