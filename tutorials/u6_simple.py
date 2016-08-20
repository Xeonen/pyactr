"""
Testing utilities of production rules and changes in utilities. It corresponds to 'testing_simple' in Lisp ACT-R, unit 6.
"""

import warnings

import pyactr as actr

class Model(object):

    def __init__(self, **kwargs):
        self.m = actr.ACTRModel(**kwargs)

        self.dm = self.m.DecMem()

        self.m.dmBuffer("retrieval", self.dm)

        g = self.m.goal("g")
        g.add(actr.makechunk(typename="start", state="start"))

        self.m.productionstring(name="one", string="""
        =g>
        isa     start
        state   'start'
        ==>
        =g>
        isa     change
        state   'change'""", utility=1)

        self.m.productionstring(name="two", string="""
        =g>
        isa     start
        state   'start'
        ==>
        =g>
        isa     dontchange
        state   'start'""", utility=5)

        self.m.productionstring(name="three", string="""
        =g>
        isa     change
        state   'change'
        ==>
        ~g>""", reward=10)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    m = Model(subsymbolic=True, utility_noise=10, utility_learning=True)
    sim = m.m.simulation(realtime=True)
    print(m.m._ACTRModel__productions)
    sim.run(1)
    print(m.m._ACTRModel__productions)
    print(m.dm)

