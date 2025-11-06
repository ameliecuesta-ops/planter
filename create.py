import math
class Vase_carre:
    def __init__(self,pdir, pstyle, pwidth, plength, pheight, pnbdrain, phandles):
        self.dir = pdir
        self.style = pstyle       
        self.width = pwidth
        self.length = plength
        self.height = pheight
        self.nbdrain= pnbdrain
        self.handles= phandles
        
        self.vertices = []
        self.faces = []
        

    def create_point(self):
            self.vertices.append([-self.width/2,0, self.length/2])   #bas_NO 1
            self.vertices.append([self.width/2,0, self.length/2])    #bas_NE 2
            self.vertices.append([self.width/2,0, -self.length/2])   #bas_SE 3
            self.vertices.append([-self.width/2,0, -self.length/2])  #bas_SO 4
            
            self.vertices.append([-self.width/2,self.height, self.length/2])   #haut_NO 5
            self.vertices.append([self.width/2,self.height, self.length/2])    #haut_NE 6
            self.vertices.append([self.width/2,self.height, -self.length/2])   #haut_SE 7
            self.vertices.append([-self.width/2,self.height, -self.length/2])  #haut_SO 8
            
            if (self.width<self.length):bord_top=self.width/8
            elif (self.width>=self.length):bord_top=self.length/8
            self.vertices.append([-self.width/2+bord_top ,self.height*0.25, self.length/2-bord_top])   #bas_NO 9
            self.vertices.append([self.width/2-bord_top,self.height*0.25, self.length/2-bord_top])    #bas_NE 10
            self.vertices.append([self.width/2-bord_top,self.height*0.25, -self.length/2+bord_top])   #bas_SE 11
            self.vertices.append([-self.width/2+bord_top,self.height*0.25, -self.length/2+bord_top])  #bas_SO 12
            
            self.vertices.append([-self.width/2+bord_top,self.height, self.length/2-bord_top])   #haut_NO  13
            self.vertices.append([self.width/2-bord_top,self.height, self.length/2-bord_top])    #haut_NE  14
            self.vertices.append([self.width/2-bord_top,self.height, -self.length/2+bord_top])   #haut_SE  15
            self.vertices.append([-self.width/2+bord_top,self.height, -self.length/2+bord_top])  #haut_SO  16
            
            self.vertices.append([-self.width/4,self.height*7/8, self.length/2])   #handle_NO  17
            self.vertices.append([self.width/4,self.height*7/8, self.length/2])    #handle_NE  18
            self.vertices.append([self.width/4,self.height*6/8, self.length/2])   #handle_SE  19
            self.vertices.append([-self.width/4,self.height*6/8, self.length/2])  #handle_SO  20
                
            self.vertices.append([-self.width/4,self.height*7/8, self.length/2-bord_top*0.75])   #handle_NO_int  21
            self.vertices.append([self.width/4,self.height*7/8, self.length/2-bord_top*0.75])    #handle_NE_int  22
            self.vertices.append([self.width/4,self.height*6/8, self.length/2-bord_top*0.75])   #handle_SE_int   23
            self.vertices.append([-self.width/4,self.height*6/8, self.length/2-bord_top*0.75])  #handle_SO_int  24
            
            self.vertices.append([-self.width/4,self.height*7/8, -self.length/2])   #handle_NO  25
            self.vertices.append([self.width/4,self.height*7/8, -self.length/2])    #handle_NE  26
            self.vertices.append([self.width/4,self.height*6/8, -self.length/2])   #handle_SE   27
            self.vertices.append([-self.width/4,self.height*6/8, -self.length/2])  #handle_SO  28
                
            self.vertices.append([-self.width/4,self.height*7/8, -self.length/2+bord_top*0.75])   #handle_NO_int  29
            self.vertices.append([self.width/4,self.height*7/8, -self.length/2+bord_top*0.75])    #handle_NE_int  30
            self.vertices.append([self.width/4,self.height*6/8, -self.length/2+bord_top*0.75])   #handle_SE_int   31
            self.vertices.append([-self.width/4,self.height*6/8, -self.length/2+bord_top*0.75])  #handle_SO_int  32
            
            self.vertices.append([self.width*0.05,self.height*0.25,-self.length*0.05])  #drain_NO_int 33
            self.vertices.append([self.width*0.05,self.height*0.25,self.length*0.05])   #drain_NE_int 34
            self.vertices.append([-self.width*0.05,self.height*0.25,self.length*0.05])  #drain_SE_int 35
            self.vertices.append([-self.width*0.05,self.height*0.25,-self.length*0.05]) #drain_SO_int 36
            self.vertices.append([self.width*0.05,0,-self.length*0.05])  #drain_NO_ext 37
            self.vertices.append([self.width*0.05,0,self.length*0.05])  #drain_NE_ext 38
            self.vertices.append([-self.width*0.05,0,self.length*0.05]) #drain_SE_ext 39
            self.vertices.append([-self.width*0.05,0,-self.length*0.05])  #drain_SO_ext 40 
            
            if (self.handles==0):
                self.faces.append([5,6,2,1])    # bord N ext
                self.faces.append([6,7,3,2])    # bord E ext
                self.faces.append([7,8,4,3])    # bord S ext
                self.faces.append([8,5,1,4])    # bord O ext
            else:
                self.faces.append([21,22,23,24])
                self.faces.append([17,21,22,18])
                self.faces.append([18,22,23,19])
                self.faces.append([19,23,24,20])
                self.faces.append([20,24,21,17])
                
                self.faces.append([5,17,18,6])
                self.faces.append([5,17,20,19,18,6,2,1])
                
                self.faces.append([29,30,31,32])
                self.faces.append([25,29,30,26])
                self.faces.append([26,30,31,27])
                self.faces.append([27,31,32,28])
                self.faces.append([28,32,29,25])
                
                self.faces.append([7,26,25,8])
                self.faces.append([7,26,27,28,25,8,4,3])
                
                self.faces.append([6,7,3,2])    # bord E ext
                self.faces.append([8,5,1,4])    # bord O ext   
            
            if (self.nbdrain == 0):
                self.faces.append([1,2,3,4])    # Fond ext    
                self.faces.append([9,10,11,12])    # Fond int
            elif (self.nbdrain == 1):   
                self.faces.append([33,37,38,34])
                self.faces.append([34,38,39,35])
                self.faces.append([35,39,40,36])
                self.faces.append([36,40,37,33])
                        
                self.faces.append([9,35,34,10])    # Fond int 
                self.faces.append([9,35,36,33,34,10,11,12])    # Fond int 
                
                self.faces.append([1,39,38,2])
                self.faces.append([1,39,40,37,38,2,3,4])
            
            
            self.faces.append([13,14,10,9])    # bord N int
            self.faces.append([14,15,11,10])    # bord E int
            self.faces.append([15,16,12,11])    # bord S int
            self.faces.append([16,13,9,12])    # bord O int
            
            self.faces.append([8,16,15,7])    # bord int top
            self.faces.append([8,5,6,7,15,14,13,16])    # bord ext top   
            
            
            
    
    def create_object(self):
        path= ""+self.dir+"/"+self.style+"_"+str(self.width)+"_"+str(self.length)+"_"+str(self.height)+"_"+str(self.nbdrain)+"_"+str(self.handles)+"_"+"vase.obj"
        with open(path, "w") as f:
            for v in self.vertices:
                f.write(f"v {v[0]} {v[1]} {v[2]}\n")
            for face in self.faces:
                f.write("f " + " ".join(map(str, face)) + "\n")
        print("ficheir écrit dans " + path )
        return path    
        
class Vase_rond:
    def __init__(self,pdir, pstyle, pwidth, pheight, pnbdrain, phandles):
        self.dir = pdir
        self.style = pstyle       
        self.width = pwidth
        self.height = pheight
        self.nbdrain= pnbdrain
        self.handles= phandles
        
        self.vertices = []
        self.faces = []
        

    def create_point(self):    
        for i in range(36):          #de 1 à 36   dessous ext
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width / 2.0) * math.cos(angle_rad)
            z = (self.width / 2.0) * math.sin(angle_rad)
            y = 0.0
            self.vertices.append([x, y, z])    
            
          
        for i in range(36):          #de 37 à 72  dessus ext
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width / 2.0) * math.cos(angle_rad)
            z = (self.width / 2.0) * math.sin(angle_rad)
            y = self.height
            self.vertices.append([x, y, z]) 
        
        bord_top=self.width/8
        for i in range(36):          #de 73 à 108    dessus int
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width / 2.0 -bord_top) * math.cos(angle_rad)
            z = (self.width / 2.0 -bord_top) * math.sin(angle_rad)
            y = self.height
            self.vertices.append([x, y, z]) 
            
        for i in range(36):          #de 109 à 144    dessous int
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width / 2.0 -bord_top) * math.cos(angle_rad)
            z = (self.width / 2.0 -bord_top) * math.sin(angle_rad)
            y = self.height*0.25
            self.vertices.append([x, y, z])   
        
        for i in range(36):          #de 145 à 180     drain int
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width *0.05) * math.cos(angle_rad)
            z = (self.width *0.05) * math.sin(angle_rad)
            y = self.height*0.25
            self.vertices.append([x, y, z])  
        
        for i in range(36):          #de 181 à 216    drain ext
            angle_deg = i * 10
            angle_rad = math.radians(angle_deg)
            x = (self.width *0.05) * math.cos(angle_rad)
            z = (self.width *0.05) * math.sin(angle_rad)
            y = 0.0
            self.vertices.append([x, y, z])  
        
        if (self.nbdrain==0):
            self.faces.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])        
            self.faces.append([37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73])
        if (self.nbdrain==1): 
            self.faces.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181])
            self.faces.append([19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,1,181,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199,198])
            
            self.faces.append([109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,163,162,161,160,159,158,157,156,155,154,153,152,151,150,149,148,147,146,145])
            self.faces.append([127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,109,145,180,179,178,177,176,175,174,173,172,171,170,169,168,167,166,165,164,163])
            
            self.faces.append([145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,199,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181])
            self.faces.append([163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,145,181,216,215,214,213,212,211,210,209,208,207,206,205,204,203,202,201,200,199])
            
            
            
            
            
        #self.faces.append([55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,37,73,108,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91])
        #self.faces.append([37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])
        #self.faces.append([55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,37,1,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19])
        
        
        
        
        return 0
            
            
    
    def create_object(self):
        path= ""+self.dir+"/"+self.style+"_"+str(self.width)+"_"+str(self.width)+"_"+str(self.height)+"_"+str(self.nbdrain)+"_"+str(self.handles)+"_"+"vase.obj"
        with open(path, "w") as f:
            for v in self.vertices:
                f.write(f"v {v[0]} {v[1]} {v[2]}\n")
            for face in self.faces:
                f.write("f " + " ".join(map(str, face)) + "\n")
        print("ficheir écrit dans " + path )
        return path        

def create_vase_carre (folder:str,style:str,width:int,length:int,height:int,nbdrain:int,handles:int):
    temp= Vase_carre(folder,style,width,length,height,nbdrain,handles)
    temp.create_point()
    return temp.create_object() 
    
def create_vase_rond (folder:str,style:str,width:int,height:int,nbdrain:int,handles:int):
    temp= Vase_rond(folder,style,width,height,nbdrain,handles)
    temp.create_point()
    return temp.create_object() 



def demo():
    temp= Vase_carre("HeliotropicPlanter/static/data","carré",2,2,4,1,0)
    temp.create_point()
    temp.create_object()
    temp= Vase_carre("HeliotropicPlanter/static/data","carré",2,2,4,0,1)
    temp.create_point()
    temp.create_object()
    temp= Vase_carre("HeliotropicPlanter/static/data","carré",2,2,4,0,0)
    temp.create_point()
    temp.create_object()
    temp= Vase_rond("HeliotropicPlanter/static/data","rond",3,5,1,1)
    temp.create_point()
    temp.create_object()
    
    
def main():
    demo()
    temp= Vase_rond("HeliotropicPlanter/static/data","rond",3,5,1,1)
    temp.create_point()
    temp.create_object()
    temp= Vase_rond("HeliotropicPlanter/static/data","rond",3,5,0,1)
    temp.create_point()
    temp.create_object()
    
    
if __name__ == "__main__":
    main()