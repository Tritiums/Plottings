import rhinoscriptsyntax as rs

for i in range(-10, 10):
    for j in range(-10, 10):
        rs.AddSphere([i*20,j*20,i*j], 10)
        rs.AddCylinder([i*20,j*20,i*j], 40, 1)
        
for i in range(-10, 10):
    for j in range(-10, 10):
        rs.AddSphere([i*20,j*20,i*j+40], 10)

rs.AddSphere([0, 0, 20], 50)
