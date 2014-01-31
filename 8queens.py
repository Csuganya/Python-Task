class Board:
 def _init_(self):
  self.board=[[0 for x in range(8)] for y in range(8)]
  self.queens=[]
 def push_queen(self,coord):
  row,col=coord
  self.board[row][col] += QUEEN
  self.mark_queen(coord,1)
  self.queens.append(coord)
 def pop_queen(self):
  row,col = self.queens.pop() 
  self.mark_queen((row,col),-1)
  self.board[row][col] -= QUEEN
 def mark_queen(self,coord,mark):
  row, col=coord
  for x in range(1,8):
   if row-x >=0:
     self.board[row-x][col] +=mark           
     if col-x >=0:
      self.board[row-x][col-x] +=mark    
     if col+x <=7:
      self.board[row-x][col+x] +=mark   
   if row+x <=7:
    self.board[row+x][col] +=mark           
    if col-x >=0:
     self.board[row+x][col-x] +=mark   
    if col+x <= 7:
     self.board[row+x][col+x] +=mark   
   if col-x >= 0:
    self.board[row][col-x] +=mark           
   if col+x <=7:
    self.board[row][col+x] +=mark           
 QUEEN=100000
 def pprint(self):
  for x in range(8):
   for y in range(8):
    if self.board[x][y] == QUEEN:
     print("Q")
    else:
     print("_")
   print
 def list_valid_moves(self):
  valid_moves=[]
  for x in range(8):
   for y in range(8):
    if self.board[x][y] == 0:
     valid_moves.append((x, y))
  return valid_moves
 def solver(self):
  valid_moves=self.list_valid_moves()
  for valid_move in valid_moves:
   self.push_queen(valid_move)
   self.solver()
   if len(self.queens) == 8:
    return
   self.pop_queen()
  return
