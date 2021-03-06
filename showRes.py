import numpy, matplotlib, matplotlib.pyplot
fig, ax = matplotlib.pyplot.subplots()
ax.plot(*[[[[[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""][j][i] for j in range(len([[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]))] for i in range(min([len(x) for x in [[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]]))][i] for i in range(len([[[[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""][j][i] for j in range(len([[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]))] for i in range(min([len(x) for x in [[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]]))])) if i != 1])
ax.set_xscale('log')
ax.set_yscale('log')
ax.set(xlabel='Number of nodes', ylabel='Time (s)',title='Testcase results (log scale)')
ax.grid()
fig.savefig("resLog.png")
fig, ax = matplotlib.pyplot.subplots()
ax.plot(*[[[[[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""][j][i] for j in range(len([[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]))] for i in range(min([len(x) for x in [[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]]))][i] for i in range(len([[[[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""][j][i] for j in range(len([[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]))] for i in range(min([len(x) for x in [[float(r) for r in x.split()] for x in open("res").read().split("\n") if x.strip() != ""]]))])) if i != 1])
ax.set(xlabel='Number of nodes', ylabel='Time (s)',title='Testcase results (linear scale)')
ax.grid()
fig.savefig("resLin.png")
matplotlib.pyplot.show()
