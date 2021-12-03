import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
#print(mean)
#print(std_deviation)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
# print(median)
# print(mode)

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="stddeviation1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="stddeviation2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="stddeviation3"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="stddeviation1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="stddeviation2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="stddeviation3"))
fig.show()
listofdatawithinfirststandarddeviation=[result for result in dice_result if result>first_std_deviation_start and result<first_std_deviation_end ]
listofdatawithinsecondstandarddeviation=[result for result in dice_result if result>second_std_deviation_start and result<second_std_deviation_end ]
listofdatawithinthirdstandarddeviation=[result for result in dice_result if result>third_std_deviation_start and result<third_std_deviation_end ]

print("{}% of data lies within first_std_deviation".format(len(listofdatawithinfirststandarddeviation)*100.0/len(dice_result)))
print("{}% of data lies within second_std_deviation".format(len(listofdatawithinsecondstandarddeviation)*100.0/len(dice_result)))
print("{}% of data lies within third_std_deviation".format(len(listofdatawithinthirdstandarddeviation)*100.0/len(dice_result)))