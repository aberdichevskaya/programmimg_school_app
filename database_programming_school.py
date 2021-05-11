#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pyodbc
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select, insert, update
from sqlalchemy import and_
import json
import requests
import sys
import time
from requests.exceptions import HTTPError


# In[224]:


class DataBase:
    def __init__(self):
        try:
            self.__token = 'c761d6331014ee2e925b6d8606a679d8868dcaac52004d10b0bbbcd98af9315ff1d51c8df9bcb0ce19bfad7ebf395851'
            self.Base = automap_base()
            self.engine = create_engine(
                'mssql+pyodbc://server-admin:Pass12345@programming-school-server.database.windows.net:1433/programmingSchool?driver=ODBC+Driver+17+for+SQL+Server')
            self.Base.prepare(self.engine, reflect=True)
        except Exception as err:
            print(f'Error occurred: {err}')
    
    
    
    def login(self, login, password):
        Student = self.Base.classes.Students
        Teacher = self.Base.classes.Teachers
        with Session(self.engine, future=True) as session:
            statement1 = select(Student).where(and_(Student.Login==login, Student.Password==password))
            result1 = session.execute(statement1).scalars().all()
            statement2 = select(Teacher).where(and_(Teacher.Login==login, Teacher.Password==password))
            result2 = session.execute(statement2).scalars().all()
            if len(result1) == 1 and len(result2) == 0:
                self.__user_id = result1[0].Id
                self.__is_student = 1
                return 1
            elif len(result2) == 1 and len(result1) == 0:
                self.__user_id = result2[0].Id
                self.__is_student = 0
                return 0
        return -1
            
        
        
    def __check_login(self, login):
        Student = self.Base.classes.Students
        Teacher = self.Base.classes.Teachers
        with Session(self.engine, future=True) as session:
            statement1 = select(Student).where(Student.Login==login)
            result1 = session.execute(statement1).scalars().all()
            statement2 = select(Teacher).where(Teacher.Login==login)
            result2 = session.execute(statement2).scalars().all()
            if len(result1) + len(result2) > 0:
                return 'Логин не является уникальным'
        return 1
        
        
    
    def registration(self, lastname, firstname, patronymic, grade, school, city, email, phone, login, password):
        Student = self.Base.classes.Students
        
        with Session(self.engine, future=True) as session:
            login_check = self.__check_login(login)
            if login_check != 1:
                return login_check
            
            try:
                session.add(Student(
                    LastName=lastname, FirstName=firstname, Patronymic=patronymic, Grade=grade, 
                    School=school, City=city, Email=email, Phone=phone, Login=login, Password=password))
                session.commit()
                
                statement = select(Student).where(Student.Login==login)
                result = session.execute(statement).scalars().one()
                self.__user_id = result.Id
                self.__is_student = 1
                
            except Exception as err:
                return f'Error occurred: {err}'
            
        return 1
    
    
    
    def send_request_to_group(self, group_name):
        GroupRequest = self.Base.classes.GroupRequests
        Group = self.Base.classes.Groups
        StudentToGroup = self.Base.classes.StudentsToGroups
    
        with Session(self.engine, future=True) as session:           
            try:               
                statement = select(Group).where(Group.Name==group_name)
                group = session.execute(statement).scalars().one()
                
                if group.Id == 10:
                    session.add(GroupRequest(StudentId=self.__user_id, GroupId=group.Id, StatusId=2))
                    session.add(StudentToGroup(StudentId=self.__user_id, GroupId=group.Id))
                else:
                    session.add(GroupRequest(StudentId=self.__user_id, GroupId=group.Id))
                session.commit()
                
            except Exception as err:
                return f'Error occurred: {err}'
            
        return 1
    
    
    
    def get_all_groups(self):
        Group = self.Base.classes.Groups
        group_names = []
        with Session(self.engine, future=True) as session:
            statement = select(Group)
            groups = session.execute(statement).scalars().all()
            for gr in groups:
                group_names.append(gr.Name)
        return group_names
    
    
    
    def get_topics(self):
        StudentToGroup = self.Base.classes.StudentsToGroups
        AvailableTopic = self.Base.classes.AvailableTopics
        Topic = self.Base.classes.Topics
        Section = self.Base.classes.Sections
        
        topic_titles = []
        with Session(self.engine, future=True) as session:
            
            try:
                if self.__is_student == 1:
                    statement = select(StudentToGroup).where(StudentToGroup.StudentId==self.__user_id)
                    student_groups = session.execute(statement).scalars().all()
                    student_groups_set = set()
                    for group in student_groups:
                        student_groups_set.add(group.GroupId)

                    statement = select(AvailableTopic)
                    topics = session.execute(statement).scalars().all()
                    student_available_topics_set = set()
                    for topic in topics:
                        if topic.GroupId in student_groups_set:
                            student_available_topics_set.add(topic.TopicId)

                    statement = select(Topic)
                    topics = session.execute(statement).scalars().all()
                    for topic in topics:
                        if topic.Id in student_available_topics_set:
                            statement = select(Section).where(Section.Id==topic.SectionId)
                            section_title = session.execute(statement).scalars().one()
                            topic_titles.append(section_title.Title+'. '+topic.Title)
                            
                else:
                    statement = select(Topic)
                    topics = session.execute(statement).scalars().all()
                    for topic in topics:
                        statement = select(Section).where(Section.Id==topic.SectionId)
                        section_title = session.execute(statement).scalars().one()
                        topic_titles.append(section_title.Title+'. '+topic.Title)
                        
            except Exception as err:
                return f'Error occurred: {err}'
                    
        return topic_titles
            

    
    def get_user_role(self):
        return self.__is_student
            
        
    
    def get_problem_compilers(self, problem_title):
        Problem = self.Base.classes.Problems
        CompilerToProblem = self.Base.classes.CompilersToProblems
        Compiler = self.Base.classes.Compilers
        
        problem_compilers = []
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Problem).where(Problem.Title==problem_title)
                problem = session.execute(statement).scalars().one()
                
                statement = select(CompilerToProblem).where(CompilerToProblem.ProblemId==problem.Id)
                correct_compilers = session.execute(statement).scalars().all()
                correct_compiler_ids = []
                for cmp in correct_compilers:
                    correct_compiler_ids.append(cmp.CompilerId)
                    
                statement = select(Compiler).where(Compiler.Id.in_(correct_compiler_ids))
                compilers = session.execute(statement).scalars().all()
                for cmp in compilers:
                    problem_compilers.append((cmp.IdOnTestSystem, cmp.Compiler))
                
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
        return 1, problem_compilers
            
        
        
    def __get_final_verdict(self, v1, v2):
        if v1 == 2 or v2 == 2:
            return 2
        if v1 == 9 or v2 == 9:
            return 9
        return v2
        
        
        
    def __get_verdict_color(self, v):
        if v == 2:
            return 1
        if v == 9:
            return 2
        if v == 1:
            return 0
        if v == 10:
            return 0
        return 3
        
        
    def __get_problem_verdicts(self, problem_ids):
        Solution = self.Base.classes.Solutions
        
        problem_inds = {}
        for i in range(len(problem_ids)):
            problem_inds[problem_ids[i]] = i
        verdicts_to_problems = {}
        problem_verdicts = [10 for i in range(len(problem_ids))]
        
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Solution).where(and_(Solution.StudentId==self.__user_id, Solution.ProblemId.in_(problem_ids)))
                solutions = session.execute(statement).scalars().all()
                
                for s in solutions:
                    if s.ProblemId in verdicts_to_problems:
                        verdicts_to_problems[s.ProblemId] = self.__get_final_verdict(verdicts_to_problems[s.ProblemId], s.VerdictId)
                    else:
                        verdicts_to_problems[s.ProblemId] = s.VerdictId
                
                for item in verdicts_to_problems.items():
                    ind = problem_inds[item[0]]
                    problem_verdicts[ind] = item[1]
                    
                for i in range(len(problem_verdicts)):
                    problem_verdicts[i] = self.__get_verdict_color(problem_verdicts[i])
                
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
            return 1, problem_verdicts
         
            
            
    def __get_correct_topic_title(self, topic_title):
        correct_topic_title = ''
        for i in range(2, len(topic_title)):
            if topic_title[i-2] == '.':
                correct_topic_title = topic_title[i:]
                break
        return correct_topic_title   
            
                
     
    def get_problems_by_topic(self, topic_title):
        Topic = self.Base.classes.Topics
        TopicToProblem = self.Base.classes.TopicsToProblems
        Problem = self.Base.classes.Problems
        
        problem_titles = []
        problem_verdicts = []
        with Session(self.engine, future=True) as session:
            try:
                correct_topic_title = self.__get_correct_topic_title(topic_title)
                statement = select(Topic).where(Topic.Title==correct_topic_title)
                topic = session.execute(statement).scalars().one()
                
                statement = select(TopicToProblem).where(TopicToProblem.TopicId==topic.Id)
                topic_problem = session.execute(statement).scalars().all()
                if len(topic_problem) == 0:
                    return [], []
                topic_problem_ids = []
                for pr in topic_problem:
                    topic_problem_ids.append(pr.ProblemId)
                    
                statement = select(Problem).where(Problem.Id.in_(topic_problem_ids))
                problems = session.execute(statement).scalars().all()
                problem_ids = []
                for pr in problems:
                    problem_titles.append(pr.Title)
                    problem_ids.append(pr.Id)
                    
                flag, problem_verdicts = self.__get_problem_verdicts(problem_ids)
                if flag == 0:
                    return 0, problem_verdicts
                    
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
        return problem_titles, problem_verdicts
    
    
    
    def get_problem_statement(self, problem_title):
        Problem = self.Base.classes.Problems
        
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Problem).where(Problem.Title==problem_title)
                problem = session.execute(statement).scalars().one()
                self.__problem_id = problem.Id
                json_statement = json.loads(problem.StatementJson)
                return 1, json_statement
            except Exception as err:
                return 0, f'Error occurred: {err}'
    
    
   
    def get_lecture_by_topic(self, topic_title):
        Topic = self.Base.classes.Topics
        Lecture = self.Base.classes.Lectures
        
        problem_titles = []
        problem_verdicts = []
        with Session(self.engine, future=True) as session:
            try:
                correct_topic_title = self.__get_correct_topic_title(topic_title)
                statement = select(Topic).where(Topic.Title==correct_topic_title)
                topic = session.execute(statement).scalars().one()
                
                statement = select(Lecture).where(Lecture.TopicId==topic.Id)
                lecture = session.execute(statement).scalars().all()
                if (len(lecture) == 0):
                    return 1, json.dumps({'text':[]})
                lecture = lecture[0]
                json_text = json.loads(lecture.LectureJson)
                return 1, json_text
                    
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
        return problem_titles, problem_verdicts
    
    
    
    def get_all_requests_to_groups(self):
        GroupRequest = self.Base.classes.GroupRequests
        Student = self.Base.classes.Students
        Group = self.Base.classes.Groups
        
        requests = []
        with Session(self.engine, future=True) as session:
            try:
                statement = select(GroupRequest).where(GroupRequest.StatusId==1)
                request_items = session.execute(statement).scalars().all()
                for item in request_items:
                    statement = select(Student).where(Student.Id==item.StudentId)
                    student = session.execute(statement).scalars().one()
                    statement = select(Group).where(Group.Id==item.GroupId)
                    group = session.execute(statement).scalars().one()
                    requests.append((student.Id, student.LastName+' '+student.FirstName, group.Id, group.Name))
                
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
        return 1, requests
    
    
    
    def __change_request_status(self, student_id, group_id, new_status):
        GroupRequest = self.Base.classes.GroupRequests
        with Session(self.engine, future=True) as session:
            statement = update(GroupRequest).where(and_(GroupRequest.GroupId==group_id, GroupRequest.StudentId==student_id, GroupRequest.StatusId==1)).values(StatusId=new_status)
            result = session.execute(statement)
            session.commit()
    
    
   
    def accept_request(self, student_id, group_id):
        self.__change_request_status(student_id, group_id, 2)
        
        StudentToGroup = self.Base.classes.StudentsToGroups
        with Session(self.engine, future=True) as session:
            session.add(StudentToGroup(StudentId=student_id, GroupId=group_id))
            session.commit()
    
    
 
    def reject_request(self, student_id, group_id):
        self.__change_request_status(student_id, group_id, 3)
    
    
    
    def __get_problem_compilers(self, problem_id):
        try:
            resp = requests.get('https://contest.misis.ru/api/contest/1345/problems/'+problem_id+'/languages?token='+self.__token)
            resp.raise_for_status()
        except HTTPError as http_err:
            return 0, f'HTTP error occurred: {http_err}'
        except Exception as err:
            return 0, f'Error occurred: {err}'
        return 1, resp.json()    
    
    
    
    def add_problem(self, title, statement_json, level_id, id_on_test_system, topic_title, teacher_check=0):
        flag, compilers_json = self.__get_problem_compilers(id_on_test_system)
        if flag == 0:
            return 0, compilers_json
        
        Problem = self.Base.classes.Problems
        TopicToProblem = self.Base.classes.TopicsToProblems
        Topic = self.Base.classes.Topics
        Compiler = self.Base.classes.Compilers
        CompilerToProblem = self.Base.classes.CompilersToProblems

        topic_title = self.__get_correct_topic_title(topic_title)
        with Session(self.engine, future=True) as session:
            try:
                session.add(Problem(Title=title, StatementJson=statement_json, LevelId=level_id,
                                    IdOnTestSystem=id_on_test_system, TeacherCheck=teacher_check))
                session.commit()
                
                statement = select(Topic).where(Topic.Title==topic_title)
                topic = session.execute(statement).scalars().one()
                
                statement = select(Problem).where(Problem.Title==title)
                problem = session.execute(statement).scalars().one()
                
                session.add(TopicToProblem(ProblemId=problem.Id, TopicId=topic.Id))
                session.commit()
                
                for cmp in compilers_json:
                    statement = select(Compiler).where(Compiler.IdOnTestSystem==cmp['id'])
                    cur_compiler = session.execute(statement).scalars().all()
                    if len(cur_compiler) == 0:
                        session.add(Compiler(Compiler=cmp['name'], IdOnTestSystem=cmp['id']))
                        session.commit()
                        statement = select(Compiler).where(Compiler.IdOnTestSystem==cmp['id'])
                        cur_compiler = session.execute(statement).scalars().all()
                    cur_compiler = cur_compiler[0]
                    
                    session.add(CompilerToProblem(ProblemId=problem.Id, CompilerId=cur_compiler.Id))
                    session.commit()
                    
            except Exception as err:
                return f'Error occurred: {err}'
            
        return 1
    
    
    
    def __send_solution_to_contest(self, solution, problem_id, compiler_id):
        try:
            resp = requests.post('https://contest.misis.ru/api/contest/1345/solutions?token='+self.__token,
                                data={'contestId': '1345', 'languageId': compiler_id,
                                      'solution': solution, 'symbolIndex': problem_id})
            resp.raise_for_status()
        except HTTPError as http_err:
            return 0, f'HTTP error occurred: {http_err}'
        except Exception as err:
            return 0, f'Error occurred: {err}'
        
        return 1, resp.json()['id']
    
    
    
    def __check_solution_status(self, solution_id):
        try:
            resp = requests.get('https://contest.misis.ru/api/contest/1345/solutions/my?token='+self.__token,
                                params={'contestId':1345, 'count':100, 'offset':0, 'select':'my'})
            resp.raise_for_status()
        except HTTPError as http_err:
            return 0, f'HTTP error occurred: {http_err}'
        except Exception as err:
            return 0, f'Error occurred: {err}'
        
        resp = resp.json()
        for solution in resp['solutions']:
            if solution['id'] == solution_id:
                return 1, solution['verdict']
        return 0, 'Решение не найдено'
    
    
    
    def __get_verdict_by_contest_verdict(self, contest_verdict):
        Verdict = self.Base.classes.Verdicts
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Verdict).where(Verdict.Verdict==contest_verdict['name'])
                verdict = session.execute(statement).scalars().all()
                if len(verdict) == 0:
                    return 1, 11
                return 1, verdict[0].Id
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
            
          
    def get_all_solutions_by_student(self):
        Solution = self.Base.classes.Solutions
        Verdict = self.Base.classes.Verdicts
        solutions_list = []
        
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Solution).where(and_(Solution.StudentId==self.__user_id, Solution.ProblemId==self.__problem_id))
                solutions = session.execute(statement).scalars().all()
                for s in solutions:
                    statement = select(Verdict).where(Verdict.Id==s.VerdictId)
                    verdict = session.execute(statement).scalars().one()
                    solutions_list.append((s.Id, verdict.Verdict))
                return 1, solutions_list
            except Exception as err:
                return 0, f'Error occurred: {err}'
    
    

    def send_solution(self, solution, compiler_id):
        Problem = self.Base.classes.Problems
        Solution = self.Base.classes.Solutions
        
        with Session(self.engine, future=True) as session:
            try:
                statement = select(Problem).where(Problem.Id==self.__problem_id)
                problem = session.execute(statement).scalars().one()
                flag, solution_id = self.__send_solution_to_contest(solution, problem.IdOnTestSystem, compiler_id)
                if flag == 0:
                    return 0, solution_id
                
                while True:
                    time.sleep(5)
                    flag, verdict = self.__check_solution_status(solution_id)
                    if flag == 0:
                        return 0, verdict
                    if verdict != None:
                        break
                
                flag, verdict_id = self.__get_verdict_by_contest_verdict(verdict)
                if flag == 0:
                    return 0, verdict_id
                session.add(Solution(StudentId=self.__user_id, ProblemId=problem.Id, VerdictId=verdict_id, Code=solution))
                session.commit()
                    
            except Exception as err:
                return 0, f'Error occurred: {err}'
            
        return self.get_all_solutions_by_student()
    
    
    
    def open_topic_for_group(self, topic_title, group_name):
        Topic = self.Base.classes.Topics
        Group = self.Base.classes.Groups
        AvTopic = self.Base.classes.AvailableTopics
        
        with Session(self.engine, future=True) as session:
            try:
                correct_topic_title = self.__get_correct_topic_title(topic_title)
                statement = select(Topic).where(Topic.Title==correct_topic_title)
                topic = session.execute(statement).scalars().one()
                
                statement = select(Group).where(Group.Name==group_name)
                group = session.execute(statement).scalars().one()
                
                statement = select(AvTopic).where(and_(AvTopic.GroupId==group.Id, AvTopic.TopicId==topic.Id))
                result = session.execute(statement).scalars().all()
                if len(result) == 0:
                    session.add(AvTopic(GroupId=group.Id, TopicId=topic.Id))
                    session.commit()
                    
            except Exception as err:
                return f'Error occurred: {err}'
            
        return 1
    
    
    
    def add_new_group(self, name):
        Group = self.Base.classes.Groups
        with Session(self.engine, future=True) as session:
            try:
                session.add(Group(Name=name))
                session.commit()
            except Exception as err:
                return f'Error occurred: {err}'
        return 1


# In[ ]:




