class emp:
    company_name1='TESSRAC private limited'
    company_name2='INSPIREDGE solutions'
    def __init__(self,name,employee_id,desg):
        self.name=name
        self.eid=employee_id
        self.desg=desg
emp_obj1=emp('naga','T0036','junior software engineer')
emp_obj2=emp('raviteja','IE0036','software engineer')
print(emp_obj1.name,'belongs to ',emp_obj1.company_name1)

print(emp_obj2.name,' belongs to ',emp_obj2.company_name2)