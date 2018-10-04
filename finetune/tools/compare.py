import csv

bench_mark_dic = {}

path1 = "977.csv"
with open(path1,"r") as f:
    csv_read = csv.reader(f)
    for line in csv_read:
        #print(line) 
        bench_mark_dic[line[0]]=line[1]

		
my_submit_dic = {}

path2 = "submit.csv"
with open(path2,"r") as f:
    csv_read = csv.reader(f)
    for line in csv_read:
        #print(line) 
        my_submit_dic[line[0]]=line[1]

		
correct_cnt = 0

for key in bench_mark_dic:
    if bench_mark_dic[key] == my_submit_dic[key]:
       correct_cnt = correct_cnt+1
	   
print("-"*40)
print("|accuracy:",str(correct_cnt)+"/"+str(440))
print("-"*40)

