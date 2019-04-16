student_scores = []
total_score = ['平均']
title = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']


with open('/Users/apple/Downloads/report.txt','r') as f:
    f.readline()
    lines = f.readlines()

for i in lines:
    s_total = 0
    s_avg = 0
    score = i.split()

    for j in score[1:]:
        s_total += int(j)

    s_avg = round(s_total/len(score[1:]),1)
    score.append(str(s_total))
    score.append(str(s_avg))
    student_scores.append(score)

student_scores.sort(key=lambda student_scores:student_scores[10],reverse=1)

for i in range(1,len(score)-1):
    t_total = 0
    t_avg = 0

    for j in student_scores:
        t_total += int(j[i])

    t_avg = t_total // len(student_scores)
    total_score.append(str(t_avg))

total_last = 0
avg_last = 0
for i in student_scores:
    total_last += float(i[-1])

avg_last = round(total_last/len(student_scores),1)
total_score.append(str(avg_last))

student_scores.insert(0,total_score)

for i in range(len(student_scores)):
    student_scores[i].insert(0,str(i))

for i in range(len(student_scores)):
    for j in range(2,len(student_scores[0])-1):
        if int(student_scores[i][j]) < 60:
            student_scores[i][j] = '不及格'

for i in range(len(student_scores)):
    if float(student_scores[i][-1]) < 60:
        student_scores[i][-1] = '不及格'

output = ' '.join(title)+'\n'
for i in student_scores:
    output += ' '.join(i)+'\n'

with open('/Users/apple/Downloads/new_report.txt','w') as f:
    f.writelines(output)
