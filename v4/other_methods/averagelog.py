import numpy as np
from numpy.linalg import norm

class AverageLog:
    def __init__(self, G):
        # C_s = Claim affrimé par la source s
        # S_c = Source qui affirme c
        # S_d = Source qui affirme les claim du Mutual ex set M_c
        # M_c = Mutual ex set du claim c
        # C_r = Claim affirmé par la source r
        self.init_trust = 1.0
        self.fixed_trust = 0.5
        
        self.G = G
        self.G.reset_graph([self.init_trust for i in range(len(self.G.mat_fs[0]))])
        self.G.trust_f = [self.fixed_trust for n in self.G.mat_fs]
        self.G.obj.update_trust(self.G.trust_f)
        self.mem_fact = []
        
    def trust_sources(self):
        """
        Compute the trust for the sources
        """
        # print(self.mem_fact)
        tmp_trust_s = [0 for i in self.G.trust_s]
        for i in range(len(self.G.trust_s)):
            cs = np.count_nonzero(self.G.sf[i] == 1)
            tmp_trust_s[i] = np.log(cs) * (sum(self.G.sf[i]*self.mem_fact)/cs)
        self.G.trust_s = tmp_trust_s
        
    def trust_fact(self):
        """
        Compute the trust for the facts
        """
        tmp_trust_f = [0 for i in self.G.trust_f]
        for i in range(len(self.G.trust_f)):
            tmp_trust_f[i] = sum(self.G.mat_fs[i]*self.G.trust_s)
        self.G.trust_f = tmp_trust_f
        
    def convergence(self):
        if self.G.iteration < 2:
            return False
        if self.G.iteration > 20:
            return True
        old = self.G.mem[1]
        current = self.G.mem[0]
        if sum(old) == 0 or sum(current) == 0:
            return True
        
        cos_sim = np.dot(current, old) / (norm(current)*norm(old))
        epsilon = 0.001
        if 1-cos_sim <= epsilon:
            return True
        return False
        
    def run(self):
        """
        Normalized by the max (same as Sums)
        """
        maxi = 0
        print(self.G.str_trust())
        while not self.convergence():
            self.G.iteration += 1
            
            self.mem_fact = self.G.trust_f

            self.trust_fact()
            maxi = max(self.G.trust_f)
            for i in range(len(self.G.trust_f)):
                self.G.trust_f[i] /= maxi
            self.G.obj.update_trust(self.G.trust_f)

            self.trust_sources()
            maxi = max(self.G.trust_s)
            for i in range(len(self.G.trust_s)):
                self.G.trust_s[i] /= maxi
                
            self.G.update_mem()
            print(self.G.str_trust())
            
    def run_noprint(self):
        maxi = 0
        while not self.convergence():
            self.G.iteration += 1
            
            self.mem_fact = self.G.trust_f
            
            self.trust_fact()
            maxi = max(self.G.trust_f)
            for i in range(len(self.G.trust_f)):
                self.G.trust_f[i] /= maxi
            self.G.obj.update_trust(self.G.trust_f)
            
            self.trust_sources()
            maxi = max(self.G.trust_s)
            for i in range(len(self.G.trust_s)):
                self.G.trust_s[i] /= maxi
                
            self.G.update_mem()
