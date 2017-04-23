import argparse
import json


class Diary(object):
    def __init__(self, students_data=None):
        # students_data:
        #{
        #   'STUDENT1':
        #       {
        #       'SUBJECT1': {
        #               'Attendance': N,
        #               'Grades': [N, N, N, ...]
        #           },
        #       'SUBJECT2': {
        #               'Attendance': N,
        #               'Grades': [N, N, N, ...]
        #           },
        #           ...
        #       },
        #   'STUDENT2':
        #       {
        #           ...
        #       },
        #       ...
        #}
        self.students_data = students_data or {}

    def add_student(self, student_data):
        # {
        #   'STUDENT':
        #       {
        #           'SUBJECT': 
        #               {
        #                   'Attendance': N,
        #                   'Grades': [N, N, N, ...]
        #               },
        #           ...
        #       }
        self.students_data.update(student_data)

    def add_grade(self, student, subject, grade):
        self.students_data[student][subject]['Grades'].append(grade)

    def summarize_attendance(self):
        return {stud: sum(v['Attendance'] for v in subj.values())
                for stud, subj in self.students_data.iteritems()}

    def summarize_grades(self):
        return {stud:
                    {s: float(sum(v['Grades']))/len(v['Grades'])
                     for s, v in subj.iteritems()}
                for stud, subj in self.students_data.iteritems()}

    @classmethod
    def from_json(cls, json_):
        dict_ = json.loads(json_)
        return Diary(dict_)

    def to_json(self):
        return json.dumps(self.students_data)

parser = argparse.ArgumentParser('Diary')
parser.add_argument('-i', dest='input', help='input file path')
parser.add_argument('-o', dest='output', help='output file path')


if __name__ == '__main__':
    args = parser.parse_args()

    students = '{}'
    if args.input is not None:
        with open(args.input) as input:
            print 'reading from: {}'.format(args.input)
            students = input.read()

    diary = Diary.from_json(students)

    from pprint import pprint
    pprint(diary.summarize_attendance())
    pprint(diary.summarize_grades())

    if args.output is not None:
        with open(args.output, 'w') as output:
            output.write(diary.to_json())
            print 'data written to: {}'.format(args.output)

