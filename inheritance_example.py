class company: # base class
    def __init__(self,eid,name,age,experience):
        self.name=name
        self.age=age
        self.eid=eid
        self.experience=experience
    def department(self,dept_type):
        try:
            if dept_type=='HR':
                print(self.name,'belogns to HR')
            elif dept_type=='Marketing':
                print(self.name,'belongs to marketing')
            elif dept_type=='Dev':
                print(self.name,'belongs to devlopment')
            elif dept_type=='Tech support':
                print(self.name,'belongs to tech support')
            else:
                print('invalid department')
        except company as e:
            print(e)
    def employement(self,emp_type): #base class method
        try:
            if emp_type=='full time':
                print(self.name,'you will get full salary')
            elif emp_type=='part time':
                print(self.name,'you will get half salary')
            elif emp_type=='contract':
                print(self.name,'however will get full salary but you are not a perminant employee')
            else:
                print(self.name,'plese choose correct employement type')
        except company as e:
            print(e)


class employee(company): #child class
    pass
emp_obj=employee('TE036','naga',23,1)
emp_obj.department('Dev')
emp_obj.employement('full time')