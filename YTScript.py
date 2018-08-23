# -*- coding: utf-8 -*-
import time,os,re,getpass,platform,sys
from colored import fg,bg,attr
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
from typing import List
from stat import S_IREAD, S_IRGRP, S_IROTH,S_IWUSR
####################################################################################################################
class check:
	def isexint(s):
		try:
			if int(s) == float(s):
				return(True)
			else:
				return False
		except:
			return False
	def ispositiveint(s):
		try:
			int(s)
			if int(s) >= 0:
				return True
			else:
				return False
		except ValueError:
			return False #ispositiveint
	def isfile(s):
		try:
			with open(s,'r') as a:
				pass
			return True
		except FileNotFoundError:
			return False
	def isvar(s):
		try:
			globals()[s]
			return True
		except KeyError:
			return False
	def isstr(s):
		try:
			str(s)
			return True
		except ValueError:
			return False
	def isint(s):
		try:
			int(s)
			return True
		except ValueError:
			return False
	def isfloat(s):
		try:
			float(s)
			return True
		except ValueError:
			return False
	def iscomplax(s):
		try:
			complax(s)
			return True
		except ValueError:
			return False
	def isbool(s):
		try:
			bool(s)
			return True
		except ValueError:
			return False
	def isfullpath(s):
		if os.path.isabs(s):
			return True
		else:
			return False
	def isdir(s):
		if os.path.isdir(s):
			return True
		elif os.path.isabs(s):
			return True
		else:
			return False
class math:
	def add(a,b):
		ans = a+b
		return(ans)
	def min(a,b):
		ans = a-b
		return(ans)
	def mul(a,b):
		ans = a*b
		return ans
	def sq(a,b):
		ans = a**b
		return ans
	def div(a,b):
		ans = a/b
		return ans
	def mod(a,b):
		ans = a%b
		return ans
####################################################################################################################
class mode:
	def setrunmode(mode="stand"):
		global runmode
		if mode == "stand":
			runmode = "stand"
		elif mode == "fullarg":
			runmode = "fullarg"
		else:
			ct.error("Unknow Mode: Runmode")
	def setoutput(optype="print"):
		global outputtype
		if optype == "print":
			outputtype = "print"
		elif optype == "null":
			outputtype = "null"
		elif optype == "std":
			outputtype = "std"
		else:
			outputtype = "print"
class ct:
	def getvar(s):
		value = globals()[s]
		return value
	def getvartype(s):
		value = globals()[s]
		return type(value)
	def writevar(s,a,typ):
		if typ == "int":
			if check.isint(a):
				value = int(a)
			else:
				return 1
		elif typ == "str":
			if check.isstr(a):
				value = str(a)
			else:
				return 1
		elif typ == "float":
			if check.isfloat(a):
				value = float(a)
			else:
				return 1
		elif typ == "complax":
			if check.iscomplax(a):
				value = complax(a)
			else:
				return 1
		elif typ == "bool":
			if check.isbool(a):
				value = bool(a)
			else:
				return 1
		else:
			return 2
		globals()[s] = value
		return 0
	def getargs(s):
		argline = ""
		arglist = []
		argsplit = list(s)
		while argsplit != []:
			if argsplit[0] == "'":
				argspace = True
				del argsplit[0]
				while argspace:
					if argsplit[0] == "'":
						del argsplit[0]
						argspace = False
					else:
						argline = argline + argsplit[0]
						del argsplit[0]
					if len(argsplit) == 0:
						argspace = False
			elif argsplit[0] == " ":
				del argsplit[0]
			else:
				argspace = True
				while argspace:
					if argsplit[0] == " ":
						del argsplit[0]
						argspace = False
					else:
						argline = argline + argsplit[0]
						del argsplit[0]
					if len(argsplit) == 0:
						argspace = False
			arglist.append(argline)
			argline = ""
		del arglist[0]
		while "" in arglist:
			arglist.remove("")
		return arglist
	def fullargs(s):
		arg = list(s)
		dont = False
		while True:
			if arg[0] == " ":
				if dont == False:
					del arg[0]
					while arg[0] == " ":
						del arg[0]
				if dont:
					while arg[0] == " ":
						del arg[0]
					return arg
			if dont:
				while arg[0] != " ":
					del arg[0]
			if arg[0] != " ":
				dont = True
	def getcmd(s):
		argline = ""
		arglist = []
		argsplit = list(s)
		while argsplit != []:
			if argsplit[0] == "'":
				argspace = True
				del argsplit[0]
				while argspace:
					if argsplit[0] == "'":
						del argsplit[0]
						argspace = False
					else:
						argline = argline + argsplit[0]
						del argsplit[0]
					if len(argsplit) == 0:
						argspace = False
			elif argsplit[0] == " ":
				del argsplit[0]
			else:
				argspace = True
				while argspace:
					if argsplit[0] == " ":
						del argsplit[0]
						argspace = False
					else:
						argline = argline + argsplit[0]
						del argsplit[0]
					if len(argsplit) == 0:
						argspace = False
			arglist.append(argline)
			argline = ""
		while "" in arglist:
			arglist.remove("")
		return arglist[0]
	def output(text:str):
		if outputtype == "print":
			print(text)
		elif outputtype == "std":
			sys.stdout.write(text)
		elif outputtype == "null":
			pass
		else:
			raise "Unknow Output Type"
	def error(text:str):
		global index
		global scriptmode
		global filename
		global cmds
		global cmd
		global runtimeindex
		print("Error: " + fg(1) + text + attr('reset'))
		if scriptmode == False:
			filename = "[RUNTIME]"
			index = 0
			cmds = ['']
			cmds[0] = cmd
			print("At file " + attr("bold") +str(filename)+ attr("reset") +  ", at Line " + attr("bold") + str(runtimeindex) + attr("reset")+ "\n'" + fg(3) + str(cmds[index])+ attr('reset') + "'")
		else:
			print("At file " + attr("bold") +str(filename)+ attr("reset") +  ", at Line " + attr("bold") + str(index + 1) + attr("reset")+ "\n'" + fg(3) + str(cmds[index])+ attr('reset') + "'")
			scriptmode = False
		runtimeindex = runtimeindex + 1
	def init():
		global codevar
		global scriptmode
		mode.setoutput()
		mode.setrunmode()
		codevar = {}
		if 'scriptmode' not in globals():
			scriptmode = False
	def run(s):
		if ct.getcmd(s) == "init":
			ct.init()
		elif runmode == "stand":
			getattr(commands, ct.getcmd(s))(ct.getargs(s))
		elif runmode == "fullarg":
			getattr(commands, ct.getcmd(s))(ct.fullargs(s))
	def runscript(s):
		global index
		global scriptmode
		global filename
		global cmds
		filename = s
		scriptmode = True
		with open(s) as file:
			cmds = file.read().split('\n')
		index = 0
		tol = len(cmds) - 1
		while index <= tol:
			if scriptmode:
				if ct.getcmd(cmds[index]) == "if":
					ifargs =ct.getargs(cmds[index])
					if len(ifargs) == 3:
						if ifargs[0] in codevar and ifargs[2] in codevar:
							if ifargs[1] == "=":
								if codevar[ifargs[0]] == codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							elif ifargs[1] == ">":
								if codevar[ifargs[0]] > codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							elif ifargs[1] == "<":
								if codevar[ifargs[0]] < codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							elif ifargs[1] == ">=":
								if codevar[ifargs[0]] >= codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							elif ifargs[1] == "<=":
								if codevar[ifargs[0]] <= codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							elif ifargs[1] == "!=":
								if codevar[ifargs[0]] != codevar[ifargs[2]]:
									index = index + 1
								else:
									index = index + 2
							else:
								ct.error("Syntax Error")
						else:
							ct.error("Unknow Variable")
					else:
						ct.error("Syntax Error")
				if ct.getcmd(cmds[index]) == "goto":
					gotoarg = ct.getargs(cmds[index])
					if len(gotoarg) == 1:
						if check.isexint(gotoarg[0]):
							index = int(gotoarg[0]) - 1
						else:
							ct.error("Type Error: Not int")
					else:
						ct.error("Syntax Error")
				elif ct.getcmd(cmds[index]) == "exit":
					scriptmode = False
					index = 0
					cmds = ['']
					return 0
				else:
					ct.run(cmds[index])
					index = index + 1
			else:
				scriptmode = False
				index = 0
				cmds = ['']
				return 0
		scriptmode = False
		index = 0
		cmds = ['']
####################################################################################################################
class commands:
	def script(arg:List[str]):
		if len(arg) == 1:
			if check.isfile(arg[0]):
				ct.runscript(arg[0])
			else:
				ct.error("Cannot find File")
		else:
			ct.error("Syntax Error")
	def init(arg:List[str]):
		ct.init()
	def setmode(arg:List[str]):
		if len(arg) == 2:
			if arg[0] == "runmode":
				if arg[1] == "fullarg":
					mode.setrunmode("fullarg")
				elif arg[1] == "stand":
					mode.setrunmode()
				else:
					ct.error("Unknow Runmode")
			elif arg[0] == "output":
				if arg[1] == "std":
					mode.setoutput("std")
				elif arg[1] == "print":
					mode.setoutput("print")
				elif arg[1] == "null":
					mode.setoutput("null")
				else:
					ct.error("Unknow Outputmode")
			else:
				ct.error("Output Error: No such Mode")
		else:
			ct.error("Syntax Error")
	def output(args:List[str]):
		string = ""
		for arg in args:
			string = string + arg
		ct.output(string)
	def setvar(arg:List[str]):
		if len(arg) == 3:
			if arg[1] == "int":
				if check.isint(arg[2]):
					codevar[arg[0]] = int(arg[2])
				else:
					ct.error("Type Error: Not int")
			elif arg[1] == "str":
				codevar[arg[0]] = arg[2]
			elif arg[1] == "float":
				if check.isfloat(arg[2]):
					codevar[arg[0]] = float(arg[2])
				else:
					ct.error("Type Error: Not float")
			elif arg[1] == "bool":
				if arg[2] in ("True","true","1"):
					codevar[arg[0]] = True
				elif arg[2] in ("False","false","0"):
					codevar[arg[0]] = False
				else:
					ct.error("Type Error: Not bool")
			else:
				ct.error("Type Error: Unknow Type")
		else:
			ct.error("Syntax Error")
	def outputvar(arg:List[str]):
		if len(arg) == 1:
			if arg[0] in codevar:
				ct.output(str(codevar[arg[0]]))
			else:
				print("Variable Error: Variable Not Found")
		else:
			ct.error("Syntax Error")
	def setvarmath(arg:List[str]):
		if len(arg) == 4:
			if arg[1] in codevar:
				if arg[3] in codevar:
					if check.isfloat(codevar[arg[1]]):
						if check.isfloat(codevar[arg[3]]):
							if arg[2] == "+":
								codevar[arg[0]] = math.add(codevar[arg[1]],codevar[arg[3]])
							elif arg[2] == "-":
								codevar[arg[0]] = math.min(codevar[arg[1]],codevar[arg[3]])
							elif arg[2] == "*":
								codevar[arg[0]] = math.mul(codevar[arg[1]],codevar[arg[3]])
							elif arg[2] == "^":
								codevar[arg[0]] = math.sq(codevar[arg[1]],codevar[arg[3]])
							elif arg[2] == "/":
								codevar[arg[0]] = math.div(codevar[arg[1]],codevar[arg[3]])
							elif arg[2] == "%":
								codevar[arg[0]] = math.mod(codevar[arg[1]],codevar[arg[3]])
							else:
								ct.error("Syntax Error")
						else:
							ct.error("Type Error: Not Float or Int")
					else:
						ct.error("Type Error: Not Float or Int")
				else:
					ct.error("Unknow Variable")
			else:
				ct.error("Unknow Variable")
		else:
			ct.error("No")
	def copyvar(arg:List[str]):
		if len(arg) == 2:
			if arg[0] in codevar:
				codevar[arg[1]] = codevar[arg[0]]
			else:
				ct.error("Unknow Source Variable")
		else:
			ct.error("Syntax Error")
	def inputvar(arg:List[str]):
		if len(arg) == 3:
			value = input(arg[2])
			if arg[1] == "int":
				if check.isint(value):
					codevar[arg[0]] = int(value)
				else:
					ct.error("Type Error: Not int")
			elif arg[1] == "str":
				codevar[arg[0]] = str(value)
			elif arg[1] == "float":
				if check.isfloat(value):
					codevar[arg[0]] = float(value)
				else:
					ct.error("Type Error: Not float")
			elif arg[1] == "bool":
				if value in ("True","true","1"):
					codevar[arg[0]] = True
				elif arg[2] in ("False","false","0"):
					codevar[arg[0]] = False
				else:
					ct.error("Type Error: Not bool")
			else:
				ct.error("Type Error: Unknow Type")
		else:
			ct.error("Syntax Error")
	def outputnl(arg:List[str]):
		ct.output("\n")
	def goto(arg:List[str]):
		pass
	def exit(arg:List[str]):
		exit()
	def _pass(arg:List[str]):
		pass
	def sleep(arg:List[str]):
		if len(arg) == 1:
			if check.isfloat(arg[0]):
				time.sleep(float(arg[0]))
			else:
				ct.error("Type Error: Not Float")
		else:
			ct.error("Syntax error")
	def os(arg:List[str]):
		torun = ""
		for i in arg:
			torun = torun + str(i)
		os.system(i)
####################################################################################################################
print("YTscript Runtime Ver Beta 1.2")
runtimeindex = 1
while True:
	try:
		cmd = input(fg(4)+str(runtimeindex)+">"+attr('reset'))
		ct.run(cmd)
		runtimeindex = runtimeindex + 1
	except AttributeError:
		ct.error("Undefined")
	except Exception as e:
		print("Indernal Error: "+ str(e))
