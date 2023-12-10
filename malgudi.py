

malgudi = ['Swami', 'and', 'Friends', 'is', 'the', 'first', 'trilogy', 'book', 'set', 'in', 'Malgudi', 'an', 'imaginary', 'village', 'in', 'South', 'India', 'Swami', 'a', 'compassionate', 'yet', 'energetic', 'child', 'and', 'his', 'two', 'friends', 'Rajam', 'the', 'boy', 'everyone', 'looks', 'up', 'to', 'in', 'class', 'and', 'Mani', 'the', 'huge', 'bruiser', 'everyone', 'fears', 'play', 'crucial', 'parts', 'in', 'the', 'plot', 'They', 'get', 'into', 'different', 'misadventures', 'as', 'they', 'go', 'around', 'town', 'looking', 'for', 'something', 'to', 'do.', 'He', 'shuddered', 'at', 'the', 'very', 'thought', 'of', 'going', 'to', 'school', 'The', 'first', 'few', 'words', 'of', 'the', 'book', 'describe', 'how', 'much', 'he', 'hates', 'school', 'The', 'first', 'chapter', 'describes', 'the', 'Albert', 'Mission', 'School', 'and', 'its', 'faculty', 'Mr.', 'Pillai,', 'the', 'history', 'teacher', 'is', 'well-liked', 'by', 'the', 'students', 'while', 'Ebenezer', 'the', 'scriptures', 'instructor', 'is', 'hated', 'by', 'everybody', 'even', 'Swami.', 'The', 'text', 'master', 'dislikes', 'Hindu', 'gods', 'which', 'irritates', 'Swamis', 'father', 'who', 'then', 'sends', 'a', 'letter', 'to', 'the', 'principal', 'about', 'the', 'isolation', 'that', 'the', 'Hindu', 'boys', 'in', 'the', 'class', 'experience', 'when', 'Ebenezer', 'criticizes', 'Krishna', 'Mani', 'is', 'introduced', 'in', 'this', 'chapter', 'Mani', 'is', 'massive,', 'and', 'his', 'physique', 'outweighs', 'his', 'intelligence', 'Somu', 'Samuel', 'and', 'Sankar', 'are', 'some', 'of', 'his', 'other', 'buddies']

d={}
s=set(malgudi)
max=0
answer=''
for x in s:
    d[x]=0
    
for x in malgudi:
    d[x]=d[x]+1
    if d[x]>max:
        max=d[x]
        answer = x



print(d)
print(max)
print(answer)