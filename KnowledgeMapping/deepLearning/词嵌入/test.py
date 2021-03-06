import gensim


model = gensim.models.Word2Vec.load("./model/corpus.model")

model.most_similar("警察")

"""
[('警员', 0.6961891651153564),
 ('保安人员', 0.6414757370948792),
 ('警官', 0.6149201989173889),
 ('消防员', 0.6082159876823425),
 ('宪兵', 0.6013336181640625),
 ('保安', 0.5982533693313599),
 ('武警战士', 0.5962344408035278),
 ('公安人员', 0.5880240201950073),
 ('民警', 0.5878666639328003),
 ('刑警', 0.5800305604934692)]
"""



model.similarity('男人','女人')
"""
Out: 0.8909852730435042

"""


model.most_similar(positive=['女人', '丈夫'], negative=['男人'], topn=1)
"""
Out: [('妻子', 0.7788498997688293)]
"""