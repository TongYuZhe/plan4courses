# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiadw_public@163.com

from Tkinter import *
import pickle, datetime

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'purple']

def get_date(str_date):
    year, month, day = map(int, str_date.split('-'))
    return datetime.date(year, month, day)

class Course:
    def __init__(self, course_name, course_start_time,
                 course_end_time, course_time_cost):
        self.name = course_name
        self.start_time = course_start_time
        self.end_time = course_end_time
        self.time_cost = course_time_cost

def add_courses(course_info_list,courses):
    # Bug 1: After we add course information into courses list,
    #        we should clear all course information entries' information
    # Bug 2: What if user input illegal information, such as text in
    #        date entry?
    course_name, start_time, end_time, time_cost = course_info_list
    course = Course(course_name.get(), get_date(start_time.get()),
                    get_date(end_time.get()), int(time_cost.get()))
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
        time_list = []
        for course in courses:
            time_list += [course.start_time, course.end_time]
        days = (max(time_list) - min(time_list)).days
        return days*10 + 100
    else:
        return 100

def get_time_cost(courses, time):
    cost = 0
    for course in courses:
        if course.start_time == time:
            cost += course.time_cost
        elif course.end_time == time:
            cost -= course.time_cost
    return cost

def get_periods(courses):
    times = set()
    for course in courses:
        times.add(course.start_time)
        times.add(course.end_time)
    times_seq = sorted(list(times))
    cost, period, periods = 0, [], []
    for time in times_seq:
        if not period:
            period.append(time)
            cost += get_time_cost(courses, time)
        else:
            period.append(time)
            periods.append((period, cost))
            period = period[1:]
            cost += get_time_cost(courses, time)
    return periods            

def draw_courses_schedule(courses):
    courses_schedule_graph = Toplevel()
    width = get_width(courses)
    height = get_height(courses)
    canvas = Canvas(courses_schedule_graph, width=width, height=height, bg='white')
    periods = get_periods(courses)
    # Draw periods
    canvas.create_line(50, 20, 50, height-20)
    canvas.create_line(50, 20, width-20, 20)
    for i, period in enumerate(periods):
        if i == 0: start_x = 51
        canvas.create_polygon(start_x, 21,
                              start_x+(period[0][1]-period[0][0]).days*10, 21,
                              start_x+(period[0][1]-period[0][0]).days*10, 21+period[1]*10,
                              start_x, 21+period[1]*10, fill = COLORS[i%len(COLORS)])
        start_x += (period[0][1]-period[0][0]).days*10
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
    try:
        courses = pickle.load(open('courses_info.txt', 'r'))
    except EOFError, IOError:
        print e
        courses = []
    except:
        print('Unexpected Error!')
        exit(0)
        
    create_main_interface(courses)

    # Store courses information into local file
    courses_info_file = open('courses_info.txt', 'w')
    pickle.dump(courses, courses_info_file)
    courses_info_file.close()
    
