class Department:
    def __init__(self):
        try:
            f=open("group_b_demo.txt","r")
            s=f.read().splitlines()
            self.subj=s[0].split(",")
            self.topics=s[1].split(':')
            self.teachers=s[2].split(':')
            print(self.topics)
            print(self.teachers)
            f.close()
        except Exception as e:
            print (e)
    def get_subject(self):
        print("SUBJECTS :", self.subj)
    def get_subj_details(self,sub):
        sub_details=dict(zip(self.subj, self.topics))
        print ('Subject-topics:', sub_details)
        print ('Subject topics available')
        print (sub,':',sub_details.get(sub))
        dep_details=dict(zip(self.subj,self.teachers))
        print ('Teachers who are available for the subject')
        print ('Subject-teachers:',dep_details.get(sub))
        #return self.sub_details.get(subj),self.dep_details.get(subj)

class student(Department):
    def s_details(self):
        self.id=int(input('Enter your id:'))
        self.name=input('Enter your name:')
        self.email=input('Enter your frequently used email:')
        self.phn=input('Enter your mobile number:')
    def choose(self):
        self.get_subject()
        sub=input("Select the subject of your choice :")
        self.get_subj_details(sub)
        #t=input('Enter the topic you are choosing')
        #te=input('Enter the teacher you are choosing ')


student1=student()
student1.s_details()
student1.choose()