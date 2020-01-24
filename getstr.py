import rpt
import sys


def main():
	if sys.argv:
		
		if len(sys.argv) < 3:
			print("Not enought parameters")
			return
		
		if not sys.argv[1].isdigit():
			print("No Step")
			return
			
		Symbol = sys.argv[2].upper()
		if len(Symbol) > 1:
			print("No single start symbol")
			return
			
		if not (sys.argv[2] == 'P' or sys.argv[2] == 'T' or sys.argv[2] == 'R' or sys.argv[2] == 'E'):
			print("No valid start symbol")
			return
			
		
		StartSymbol = -1
		Decimal = False
		
		if sys.argv[2] == 'P':
			StartSymbol = rpt.P
		if sys.argv[2] == 'R':
			StartSymbol = rpt.R
		if sys.argv[2] == 'T':
			StartSymbol = rpt.T
		if sys.argv[2] == 'E':
			StartSymbol = rpt.E
		##############################
		if len(sys.argv) == 4:
			Decimal = True
		##############################
		Cin = [StartSymbol]
		Pasos = int(sys.argv[1])
		print(Cin[0])
		for w in rpt.automata(Cin,Pasos):
			R = ''
			for e in w:
				R = R + str(e)
			if Decimal:
				print(int(R,4))
			else:
				print(R)

if __name__== "__main__":
	main()

