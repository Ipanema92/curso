class Grid:
    
    def __init__(self,nx,ny,nz,ox,oy,oz,sx,sy,sz):
       
       self.ox = ox
       self.oy = oy
       self.oz = oz
       
       self.nx = nx
       self.ny = ny
       self.nz = nz
        
       self.sx = sx
       self.sy = sy
       self.sz = sz
    
    
    def number_of_blocks(self):
        
        return self.nx*self.ny*self.nz
    
    
    def autogrid(self,coordx,coordy,coordz,sx,sy,sz):
    
        self.ox=np.min(coordx)
        self.oy=np.min(coordy)
        self.oz=np.min(coordz)
    
        self.nx=int(((np.max(coordx)-np.min(coordx))/sx)+1)
        self.ny=int(((np.max(coordy)-np.min(coordy))/sy)+1)
        self.nz=int(((np.max(coordz)-np.min(coordz))/sz)+1)
    
        return