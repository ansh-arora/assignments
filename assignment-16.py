#Q1
import re
emails=['zuck26@facbook.com','page33@google.com','jeff42@amazon.com']
out=[]
for e in emails:
    m = re.match(r'(.*)@(.*)[.](.*)',e, re.M|re.I)
    t=(m.group(1),m.group(2),m.group(3))
    out.append(t)
print(out)

#Q2
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
matches = re.findall(r'[bB]\S+',text)
print(matches)

#Q3
import re
sentence = "A, very very; irregular_sentence"
s = re.sub(r'[,;_]', " ",sentence)
print(s)

#Q4 Optional
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print ("original tweet:",tweet)
t = re.sub(r'(http\S+)|(@\S+)|(#\S+)|(cc:)|(RT\s)|[,.:!$%&*]', "", tweet)
print("cleared tweet:",t)