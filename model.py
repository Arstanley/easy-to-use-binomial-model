# def traverse(root):
#     current_level = [root]
#     while current_level:
#         print(' '.join(str(node) for node in current_level))
#         next_level = list()
#         for n in current_level:
#             if n.h:
#                 next_level.append(n.h)
#             if n.t:
#                 next_level.append(n.t)
#         current_level = next_level

class Node:

	def __init__(self, x):
		self.val = x
		self.h = None
		self.t = None

	def __str__(self):
		return str(self.val)

class binomial_model:

	def __init__(self, s_0, u, d, r):
		"""
		input:
			s_0: Stock price at t_0
			u: Up factor
			d: Down factor
			r: Risk-free interest rate
		"""

		# Parameter set up
		self.s_0 = s_0
		self.u = u
		self.d = d
		self.r = r

		# Calculate p_tilta and q_tilta
		self.p_til = (1 + r - d) / (u - d)
		self.q_til = (u - 1 - r) / (u - d)

		self.root = Node(self.s_0)

	def build_binary_tree(self, cur, depth):
	
		if (depth == 0):
			return None

		cur.h = self.build_binary_tree(Node(cur.val * self.u), depth-1)
		cur.t = self.build_binary_tree(Node(cur.val * self.d), depth-1)	

		return cur

	
	def calc_v0(self, k, T):
		"""
		input:
			k: Strike price
			T: Term length
		"""

		# T+=1 in order to match the notation in book
		T += 1

		self.root = self.build_binary_tree(self.root, T)		

		# Recursively calculate the option price
		
		ret = self.get_v0(self.root, k)

		return ret 

	def get_v0(self, cur, k):
		"""
		Input: 
			cur: current node 
		"""
		if not cur.h and not cur.t:
			if cur.val >= k:
				return cur.val-k
			else:
				return 0	
		
		v_1 = self.get_v0(cur.h, k)
		v_2 = self.get_v0(cur.t, k)

		return (1 / (1+self.r)) * (self.p_til * v_1 + self.q_til * v_2)




