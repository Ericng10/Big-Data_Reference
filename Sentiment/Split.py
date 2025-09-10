import pandas as pd
df = pd.read_excel('Skytrax.xlsx', sheet_name='Skytrax')
df_review = df[['review_text','pos_neu_neg_review_score']]
df_positive = df_review[df_review['pos_neu_neg_review_score'] == 'pos']
df_negative = df_review[df_review['pos_neu_neg_review_score'] == 'neg']

for x, i in enumerate (df_positive['review_text']):
    outfile = open('positive/'+'pos_'+str(x+1),'w', encoding="utf-8")
    outfile.write(str(i))
    outfile.close()

for x, i in enumerate (df_negative['review_text']):
    outfile = open('negative/'+'neg_'+str(x+1),'w', encoding="utf-8")
    outfile.write(str(i))
    outfile.close()
