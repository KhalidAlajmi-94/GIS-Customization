import arcpy
aWS= r"C:\Khalid\Exam-02\Exam_2.gdb"
arcpy.env.workspace=aWS

aFC=arcpy.ListFeatureClasses()
aFC.sort()
print "There are {} feature in this geodatabase! \n".format(len(aFC))
aFile= open(r"C:\Khalid\Exam-02\msg.txt", "w")
aFile.write("There are {} feature in this geodatabase! \n".format(len(aFC)))

for x in aFC:
    des= arcpy.Describe(x)
    aFeature=x+"_P"
    if des.SpatialReference.type=="Projected":
        aword=""
    else:
        arcpy.Exists(aFeature)
        arcpy.Delete_management(aFeature)
        arcpy.Project_management(x,aFeature,(3310))
        aword="it has been projected into {}".format(aFeature)

    print "{} has {} features, it is a {}. {}\n".format(x.lower(), arcpy.GetCount_management(x), des.shapeType.upper(), aword)
    aFile.write("{} has {} features, it is a {}. {}\n".format(x.lower(), arcpy.GetCount_management(x), des.shapeType.upper(), aword))

aFile.close()
   

 
   
  