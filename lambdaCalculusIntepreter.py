# λ Calculus Interpreter
# from: https://www.youtube.com/watch?v=n5x0LtpnSyM (Charles Fox, Mar 14 2022)

class Expression():
  pass

# name class built with identifier ID
class Name(Expression):
  def __init__(self, ID):
    self.ID = ID
  def __repr__(self):
    return str(self.ID)
  def makeSub(self, oldName, newExpr):
    return newExpr if self.ID == oldName.ID else self

# function class built with input variable Name and expression body to return
class Function(Expression):
  def __init__(self, variable, body):
    self.variable = variable
    self.body = body
  def __repr__(self):
    return "(\u03BB" + str(self.variable) + "." + str(self.body)+ ")"
  def makeSub(self, oldName, newExpr):
    return Function(self.variable, self.body.makeSub(oldName, newExpr))
  def eval(self, argument):
    return self.body.makeSub(self.variable, argument)

# application class built with operator Function and argument Expression
class Application(Expression):
  def __init__(self, operator, argument):
    self.operator = operator
    self.argument = argument
  def __repr__(self):
    return str(self.operator) + str(self.argument)
  def makeSub(self, oldName, newExpr):
    return Application(self.operator.makeSub(oldName,newExpr), self.argument.makeSub(oldName, newExpr))
  def eval(self):
    return self.operator.eval(self.argument)

# example expressions
x = Name("x")
y = Name("y")
I = Function(x,x)
T = Function(x, Function(y, x))
F = Function(x, Function(y, y))
IY = Application(I, y)
R = Application(Function(x, Application(x,x)), Function(x, Application(x,x)))

# display expression
for expr in (x,y,I,T,F,IY,R):
  print(f"Expr: {expr}")

# display application evaluations
for app in (IY, R):
    print(f"Application: {app} evaluates to -> {app.eval()}")


