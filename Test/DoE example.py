from doepy import build

x= build.full_fact(
{'Pressure':[40,55,70],
'Temperature':[290, 320, 350],
'Flow rate':[0.2,0.4],
'Time':[5,8]}
)

print(x)



y=build.space_filling_lhs(
{'Pressure':[40,55,70],
'Temperature':[290, 320, 350],
'Flow rate':[0.2,0.4],
'Time':[5,11]},
num_samples = 4
)

print(y)




z=build.full_fact(
    {'Treatment':[1,2,3,4],
     'Replicates1':[575,565,600,725],
     'Replicates2':[542,593,590,610],
     'Replicates3':[600,651,610,629],
     'Replicates4':[570,610,629,710],
     
     }
    )

print(z)