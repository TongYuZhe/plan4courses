# Main Interface of Plan4Courses
# Author: Dawei Xia
# E-Mail: xiaoyangpublic@163.com

from Tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.title('Plan4Courses')
    add_courses_btn = Button(root, text='Add Courses')
    del_courses_btn = Button(root, text='Delete Courses')
    gen_courses_cost_btn = Button(root, text='Generate Courses Cost')
    add_courses_btn.pack(fill=BOTH, expand=YES)
    del_courses_btn.pack(fill=BOTH, expand=YES)
    gen_courses_cost_btn.pack(fill=BOTH, expand=YES)
    root.mainloop()
