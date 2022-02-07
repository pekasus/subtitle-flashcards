engsubfile = 'big-lebowski/the-big-lebowski-subtitles-eng.srt'
russubfile = 'big-lebowski/the-big-lebowski-subtitles-rus.srt'

def parse_sample(text):
    text = text.split("\n\n")
    l1 = [l.split('\n', 2) for l in text]
    for l in l1:
        l[0] = int(l[0])
        l[1] = l[1].replace(',','.')
        l[1] = l[1].split(' --> ')
        l[1] = [i.split(':') for i in l[1]]
        l[1] = [float(i[0]) * 3600 + float(i[1]) * 60 + float(i[2]) for i in l[1]]
        l[2] = l[2].replace('\n', ' ')
    return l1

eng = parse_sample(open(engsubfile, 'r').read())
rus = parse_sample(open(russubfile, 'r').read())
rus = rus[2:]
for i in rus:
    i[0] -= 2

for i in range(len(eng)):
    print(f"{eng[i][2]} | {rus[i][2]}")
    input()

